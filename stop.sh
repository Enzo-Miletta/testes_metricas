#!/bin/bash

echo "========================================"
echo "Parando Sistema de Monitoramento"
echo "========================================"
echo

echo "Parando Docker Compose (Prometheus e Grafana)..."
docker-compose down

echo
echo "Matando processos Python..."
pkill -f metrics_exporter.py
pkill -f api_monitor.py

echo
echo "Sistema parado com sucesso!"
echo "========================================"
