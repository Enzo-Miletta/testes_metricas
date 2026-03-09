#!/usr/bin/env python3
"""
Sistema de Monitoramento de Infraestrutura
Exporta métricas de sistema para o Prometheus
"""

import time
import psutil
import os
from prometheus_client import start_http_server, Gauge, Counter, Info
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações
EXPORTER_PORT = int(os.getenv('EXPORTER_PORT', 8000))
EXPORTER_HOST = os.getenv('EXPORTER_HOST', '0.0.0.0')
COLLECTION_INTERVAL = int(os.getenv('COLLECTION_INTERVAL', 15))

# Métricas de CPU
cpu_usage_percent = Gauge('system_cpu_usage_percent', 'Uso de CPU em porcentagem')
cpu_count = Gauge('system_cpu_count', 'Número de CPUs')
cpu_freq = Gauge('system_cpu_frequency_mhz', 'Frequência da CPU em MHz')

# Métricas de Memória
memory_total = Gauge('system_memory_total_bytes', 'Memória total em bytes')
memory_available = Gauge('system_memory_available_bytes', 'Memória disponível em bytes')
memory_used = Gauge('system_memory_used_bytes', 'Memória usada em bytes')
memory_percent = Gauge('system_memory_usage_percent', 'Uso de memória em porcentagem')

# Métricas de Disco
disk_total = Gauge('system_disk_total_bytes', 'Espaço total em disco', ['mountpoint'])
disk_used = Gauge('system_disk_used_bytes', 'Espaço usado em disco', ['mountpoint'])
disk_free = Gauge('system_disk_free_bytes', 'Espaço livre em disco', ['mountpoint'])
disk_percent = Gauge('system_disk_usage_percent', 'Uso de disco em porcentagem', ['mountpoint'])

# Métricas de Rede
network_bytes_sent = Counter('system_network_bytes_sent_total', 'Total de bytes enviados')
network_bytes_recv = Counter('system_network_bytes_received_total', 'Total de bytes recebidos')
network_packets_sent = Counter('system_network_packets_sent_total', 'Total de pacotes enviados')
network_packets_recv = Counter('system_network_packets_received_total', 'Total de pacotes recebidos')

# Métricas de Processos
process_count = Gauge('system_process_count', 'Número de processos em execução')

# Informações do sistema
system_info = Info('system', 'Informações do sistema')

def collect_system_info():
    """Coleta informações estáticas do sistema"""
    import platform
    system_info.info({
        'hostname': platform.node(),
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor()
    })

def collect_cpu_metrics():
    """Coleta métricas de CPU"""
    cpu_usage_percent.set(psutil.cpu_percent(interval=1))
    cpu_count.set(psutil.cpu_count())
    
    freq = psutil.cpu_freq()
    if freq:
        cpu_freq.set(freq.current)

def collect_memory_metrics():
    """Coleta métricas de memória"""
    mem = psutil.virtual_memory()
    memory_total.set(mem.total)
    memory_available.set(mem.available)
    memory_used.set(mem.used)
    memory_percent.set(mem.percent)

def collect_disk_metrics():
    """Coleta métricas de disco"""
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            mountpoint = partition.mountpoint
            
            disk_total.labels(mountpoint=mountpoint).set(usage.total)
            disk_used.labels(mountpoint=mountpoint).set(usage.used)
            disk_free.labels(mountpoint=mountpoint).set(usage.free)
            disk_percent.labels(mountpoint=mountpoint).set(usage.percent)
        except PermissionError:
            # Ignorar partições sem permissão
            continue

def collect_network_metrics():
    """Coleta métricas de rede"""
    net = psutil.net_io_counters()
    
    # Para Counter, precisamos usar inc() com a diferença
    # Como estamos usando _total, o Prometheus calculará a taxa
    network_bytes_sent._value.set(net.bytes_sent)
    network_bytes_recv._value.set(net.bytes_recv)
    network_packets_sent._value.set(net.packets_sent)
    network_packets_recv._value.set(net.packets_recv)

def collect_process_metrics():
    """Coleta métricas de processos"""
    process_count.set(len(psutil.pids()))

def collect_all_metrics():
    """Coleta todas as métricas"""
    try:
        collect_cpu_metrics()
        collect_memory_metrics()
        collect_disk_metrics()
        collect_network_metrics()
        collect_process_metrics()
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Métricas coletadas com sucesso")
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Erro ao coletar métricas: {e}")

def main():
    """Função principal"""
    print(f"Iniciando Metrics Exporter na porta {EXPORTER_PORT}...")
    
    # Coletar informações do sistema (uma vez)
    collect_system_info()
    
    # Iniciar servidor HTTP para Prometheus
    start_http_server(EXPORTER_PORT, addr=EXPORTER_HOST)
    print(f"Exporter rodando em http://{EXPORTER_HOST}:{EXPORTER_PORT}/metrics")
    print(f"Intervalo de coleta: {COLLECTION_INTERVAL} segundos")
    
    # Loop de coleta
    while True:
        collect_all_metrics()
        time.sleep(COLLECTION_INTERVAL)

if __name__ == '__main__':
    main()
