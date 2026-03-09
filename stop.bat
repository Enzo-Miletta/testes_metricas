@echo off
echo ========================================
echo Parando Sistema de Monitoramento
echo ========================================
echo.

echo Parando Docker Compose (Prometheus e Grafana)...
docker-compose down

echo.
echo Sistema parado com sucesso!
echo.
echo NOTA: Os processos Python devem ser fechados manualmente
echo nas janelas que foram abertas.
echo ========================================
pause
