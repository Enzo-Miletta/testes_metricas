# 🖥️ Sistema de Monitoramento de Infraestrutura

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-required-2496ED.svg?logo=docker)](https://www.docker.com/)
[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?logo=Prometheus&logoColor=white)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-F46800?logo=grafana&logoColor=white)](https://grafana.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

Sistema completo de monitoramento de infraestrutura com dashboards em tempo real usando Python, Prometheus e Grafana.

<p align="center">
  <img src="https://img.shields.io/badge/Status-Em%20Produção-success" alt="Status">
  <img src="https://img.shields.io/badge/Manutenção-Ativa-green" alt="Manutenção">
</p>

---

## 📖 Índice

- [Funcionalidades](#-funcionalidades)
- [Stack Tecnológica](#️-stack-tecnológica)
- [Requisitos](#-requisitos)
- [Instalação e Execução](#-instalação-e-execução)
- [Dashboard Grafana](#-dashboard-grafana)
- [Configuração](#️-configuração)
- [Métricas Coletadas](#-métricas-coletadas)
- [Troubleshooting](#-troubleshooting)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)
- [Contato](#-contato)

## 📋 Funcionalidades

- ✅ Monitoramento de CPU (uso, frequência, número de cores)
- ✅ Monitoramento de Memória (total, usada, disponível)
- ✅ Monitoramento de Disco (espaço usado, livre, por partição)
- ✅ Monitoramento de Rede (bytes/pacotes enviados e recebidos)
- ✅ Monitoramento de Processos
- ✅ Health Check de APIs (disponibilidade e tempo de resposta)
- ✅ Dashboard visual no Grafana
- ✅ Sistema de alertas configurável
- ✅ Métricas históricas com Prometheus

## 🛠️ Stack Tecnológica

- **Backend**: Python 3.8+
- **Métricas**: Prometheus
- **Visualização**: Grafana
- **Containerização**: Docker & Docker Compose
- **Bibliotecas Python**:
  - `prometheus-client` - Exportação de métricas
  - `psutil` - Coleta de informações do sistema
  - `requests` - Monitoramento de APIs
  - `flask` - Servidor HTTP

## 📦 Requisitos

- Python 3.8 ou superior
- Docker Desktop
- 2GB de RAM disponível (preferencialmente 15GB de RAM disponível)
- Portas 3000, 8000, 8001 e 9090 disponíveis

## 🚀 Instalação e Execução

### Windows

1. **Clone ou baixe o projeto**

2. **Configure as APIs a serem monitoradas**

   ```bash
   # Copie o arquivo de exemplo
   copy .env.example .env
   
   # Edite o arquivo .env e adicione suas APIs
   # Exemplo: MONITORED_APIS=http://localhost:3000/health,http://api.github.com
   ```

3. **Execute o script de inicialização**

   ```bash
   start.bat
   ```

   O script irá:
   - Criar ambiente virtual Python
   - Instalar dependências
   - Iniciar Prometheus e Grafana (Docker)
   - Iniciar coletores de métricas

4. **Acesse os dashboards**
   - **Grafana**: <http://localhost:3000>
     - Usuário: `admin`
     - Senha: `admin`
   - **Prometheus**: <http://localhost:9090>
   - **Métricas do Sistema**: <http://localhost:8000/metrics>
   - **Métricas de APIs**: <http://localhost:8001/metrics>

### Linux/Mac

1. **Instalar dependências**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configurar variáveis de ambiente**

   ```bash
   cp .env.example .env
   # Edite o arquivo .env conforme necessário
   ```

3. **Iniciar serviços**

   ```bash
   # Terminal 1: Docker Compose
   docker-compose up -d
   
   # Terminal 2: Metrics Exporter
   python metrics_exporter.py
   
   # Terminal 3: API Monitor
   python api_monitor.py
   ```

## 📊 Dashboard Grafana

O dashboard inclui:

### Gauges (Indicadores)

- **Uso de CPU** - Percentual de uso com limites de alerta
- **Uso de Memória** - Percentual de uso com limites de alerta
- **Uso de Disco** - Percentual por partição
- **Status das APIs** - Indicador UP/DOWN para cada API

### Gráficos Temporais

- **Histórico de CPU** - Evolução do uso ao longo do tempo
- **Uso de Memória (Bytes)** - Memória usada vs. disponível
- **Tempo de Resposta das APIs** - Latência de cada endpoint
- **Tráfego de Rede** - Bytes enviados/recebidos por segundo

## ⚙️ Configuração

### Ajustar Intervalo de Coleta

Edite o arquivo `.env`:

```bash
# Intervalo em segundos (padrão: 15)
COLLECTION_INTERVAL=15
```

### Adicionar APIs para Monitorar

Edite o arquivo `.env`:

```bash
# Separe múltiplas APIs por vírgula
MONITORED_APIS=http://localhost:3000/health,http://api.exemplo.com/status,http://example.com
```

### Configurar Alertas

Edite o arquivo `alerts.yml` para personalizar:

- Limites de CPU, memória e disco
- Tempo de resposta de APIs
- Tempos de espera antes de disparar alertas

Exemplo:

```yaml
- alert: HighCPUUsage
  expr: system_cpu_usage_percent > 80  # Altere o limite aqui
  for: 5m  # Tempo antes de disparar
```

## 📈 Métricas Coletadas

### Sistema

- `system_cpu_usage_percent` - Uso de CPU (%)
- `system_cpu_count` - Número de CPUs
- `system_cpu_frequency_mhz` - Frequência da CPU
- `system_memory_total_bytes` - Memória total
- `system_memory_used_bytes` - Memória usada
- `system_memory_available_bytes` - Memória disponível
- `system_memory_usage_percent` - Uso de memória (%)
- `system_disk_total_bytes` - Espaço total em disco
- `system_disk_used_bytes` - Espaço usado em disco
- `system_disk_free_bytes` - Espaço livre em disco
- `system_disk_usage_percent` - Uso de disco (%)
- `system_network_bytes_sent_total` - Bytes enviados
- `system_network_bytes_received_total` - Bytes recebidos
- `system_process_count` - Número de processos

### APIs

- `api_up` - Status da API (1=UP, 0=DOWN)
- `api_response_time_seconds` - Tempo de resposta
- `api_status_code` - Código HTTP retornado
- `api_requests_total` - Total de requisições por status
