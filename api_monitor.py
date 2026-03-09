#!/usr/bin/env python3
"""
Monitor de APIs
Verifica disponibilidade e tempo de resposta de APIs
"""

import time
import requests
import os
from prometheus_client import start_http_server, Gauge, Counter
from dotenv import load_dotenv
from urllib.parse import urlparse

# Carregar variáveis de ambiente
load_dotenv()

# Configurações
API_MONITOR_PORT = int(os.getenv('API_MONITOR_PORT', 8001))
EXPORTER_HOST = os.getenv('EXPORTER_HOST', '0.0.0.0')
COLLECTION_INTERVAL = int(os.getenv('COLLECTION_INTERVAL', 15))
MONITORED_APIS = os.getenv('MONITORED_APIS', '').split(',')

# Métricas de API
api_up = Gauge('api_up', 'Status da API (1=UP, 0=DOWN)', ['url', 'name'])
api_response_time = Gauge('api_response_time_seconds', 'Tempo de resposta da API em segundos', ['url', 'name'])
api_status_code = Gauge('api_status_code', 'Código de status HTTP da API', ['url', 'name'])
api_requests_total = Counter('api_requests_total', 'Total de requisições', ['url', 'name', 'status'])

def get_api_name(url):
    """Extrai um nome amigável da URL"""
    parsed = urlparse(url)
    hostname = parsed.hostname or 'unknown'
    path = parsed.path.replace('/', '_').strip('_') or 'root'
    return f"{hostname}_{path}"

def check_api(url):
    """Verifica uma API"""
    name = get_api_name(url)
    
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        response_time = time.time() - start_time
        
        # Atualizar métricas
        api_up.labels(url=url, name=name).set(1)
        api_response_time.labels(url=url, name=name).set(response_time)
        api_status_code.labels(url=url, name=name).set(response.status_code)
        
        # Status: success (2xx), client_error (4xx), server_error (5xx), redirect (3xx)
        if 200 <= response.status_code < 300:
            status = 'success'
        elif 300 <= response.status_code < 400:
            status = 'redirect'
        elif 400 <= response.status_code < 500:
            status = 'client_error'
        else:
            status = 'server_error'
        
        api_requests_total.labels(url=url, name=name, status=status).inc()
        
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {url} - UP (Status: {response.status_code}, Tempo: {response_time:.3f}s)")
        
    except requests.exceptions.Timeout:
        api_up.labels(url=url, name=name).set(0)
        api_requests_total.labels(url=url, name=name, status='timeout').inc()
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {url} - DOWN (Timeout)")
        
    except requests.exceptions.ConnectionError:
        api_up.labels(url=url, name=name).set(0)
        api_requests_total.labels(url=url, name=name, status='connection_error').inc()
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {url} - DOWN (Connection Error)")
        
    except Exception as e:
        api_up.labels(url=url, name=name).set(0)
        api_requests_total.labels(url=url, name=name, status='error').inc()
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {url} - DOWN (Error: {e})")

def check_all_apis():
    """Verifica todas as APIs configuradas"""
    for api_url in MONITORED_APIS:
        api_url = api_url.strip()
        if api_url:
            check_api(api_url)

def main():
    """Função principal"""
    print(f"Iniciando API Monitor na porta {API_MONITOR_PORT}...")
    
    # Validar APIs configuradas
    if not any(MONITORED_APIS):
        print("AVISO: Nenhuma API configurada para monitoramento!")
        print("Configure as APIs na variável MONITORED_APIS no arquivo .env")
    else:
        print(f"APIs monitoradas: {len([url for url in MONITORED_APIS if url.strip()])}")
        for api_url in MONITORED_APIS:
            if api_url.strip():
                print(f"  - {api_url.strip()}")
    
    # Iniciar servidor HTTP para Prometheus
    start_http_server(API_MONITOR_PORT, addr=EXPORTER_HOST)
    print(f"Exporter rodando em http://{EXPORTER_HOST}:{API_MONITOR_PORT}/metrics")
    print(f"Intervalo de verificação: {COLLECTION_INTERVAL} segundos")
    
    # Loop de verificação
    while True:
        check_all_apis()
        time.sleep(COLLECTION_INTERVAL)

if __name__ == '__main__':
    main()
