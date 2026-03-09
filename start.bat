echo ========================================
echo Iniciando Sistema de Monitoramento
echo ========================================
echo.

REM Verificar se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python não encontrado. Por favor, instale o Python 3.8 ou superior.
    pause
    exit /b 1
)

REM Verificar se o Docker está rodando
docker info >nul 2>&1
if errorlevel 1 (
    echo ERRO: Docker não está rodando. Por favor, inicie o Docker Desktop.
    pause
    exit /b 1
)

REM Criar ambiente virtual se não existir
if not exist "venv" (
    echo Criando ambiente virtual...
    python -m venv venv
)

REM Ativar ambiente virtual
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Instalar dependências
echo Instalando dependências Python...
pip install -r requirements.txt

REM Copiar arquivo .env se não existir
if not exist ".env" (
    echo Criando arquivo .env...
    copy .env.example .env
    echo IMPORTANTE: Configure as APIs no arquivo .env
)

REM Iniciar Docker Compose (Prometheus e Grafana)
echo.
echo Iniciando Prometheus e Grafana...
docker-compose up -d

REM Aguardar serviços iniciarem
echo Aguardando serviços iniciarem...
timeout /t 5 /nobreak >nul

REM Iniciar exporters Python em novas janelas
echo.
echo Iniciando Metrics Exporter...
start "Metrics Exporter" cmd /k "venv\Scripts\activate.bat && python metrics_exporter.py"

echo Iniciando API Monitor...
start "API Monitor" cmd /k "venv\Scripts\activate.bat && python api_monitor.py"

echo.
echo ========================================
echo Sistema iniciado com sucesso!
echo ========================================
echo.
echo Acesse os serviços:
echo   - Grafana:    http://localhost:3000 (admin/admin)
echo   - Prometheus: http://localhost:9090
echo   - Métricas:   http://localhost:8000/metrics
echo   - API Health: http://localhost:8001/metrics
echo.
echo Para parar o sistema, execute: stop.bat
echo ========================================
pause
