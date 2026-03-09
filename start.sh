#!/bin/bash

echo "========================================"
echo "Iniciando Sistema de Monitoramento"
echo "========================================"
echo

# Verificar se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "ERRO: Python3 não encontrado. Por favor, instale o Python 3.8 ou superior."
    exit 1
fi

# Verificar se o Docker está rodando
if ! docker info &> /dev/null; then
    echo "ERRO: Docker não está rodando. Por favor, inicie o Docker."
    exit 1
fi

# Criar ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativar ambiente virtual
echo "Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
echo "Instalando dependências Python..."
pip install -r requirements.txt

# Copiar arquivo .env se não existir
if [ ! -f ".env" ]; then
    echo "Criando arquivo .env..."
    cp .env.example .env
    echo "IMPORTANTE: Configure as APIs no arquivo .env"
fi

# Iniciar Docker Compose (Prometheus e Grafana)
echo
echo "Iniciando Prometheus e Grafana..."
docker-compose up -d

# Aguardar serviços iniciarem
echo "Aguardando serviços iniciarem..."
sleep 5

# Iniciar exporters Python
echo
echo "Iniciando Metrics Exporter e API Monitor..."
python3 metrics_exporter.py &
METRICS_PID=$!
python3 api_monitor.py &
API_PID=$!

echo
echo "========================================"
echo "Sistema iniciado com sucesso!"
echo "========================================"
echo
echo "Acesse os serviços:"
echo "  - Grafana:    http://localhost:3000 (admin/admin)"
echo "  - Prometheus: http://localhost:9090"
echo "  - Métricas:   http://localhost:8000/metrics"
echo "  - API Health: http://localhost:8001/metrics"
echo
echo "PIDs dos processos:"
echo "  - Metrics Exporter: $METRICS_PID"
echo "  - API Monitor: $API_PID"
echo
echo "Para parar o sistema:"
echo "  - Pressione Ctrl+C"
echo "  - Execute: docker-compose down"
echo "  - Execute: kill $METRICS_PID $API_PID"
echo "========================================"

# Aguardar interrupção
wait
