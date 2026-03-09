#!/usr/bin/env python3
"""
Script de verificação do sistema de monitoramento
Verifica se todos os componentes estão rodando corretamente
"""

import requests
import time
import sys

def check_service(name, url, expected_status=200):
    """Verifica se um serviço está respondendo"""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == expected_status:
            print(f"✓ {name}: OK (Status {response.status_code})")
            return True
        else:
            print(f"✗ {name}: FALHA (Status {response.status_code}, esperado {expected_status})")
            return False
    except requests.exceptions.ConnectionError:
        print(f"✗ {name}: OFFLINE (não foi possível conectar)")
        return False
    except requests.exceptions.Timeout:
        print(f"✗ {name}: TIMEOUT (demorou mais de 5 segundos)")
        return False
    except Exception as e:
        print(f"✗ {name}: ERRO ({str(e)})")
        return False

def check_prometheus_targets():
    """Verifica se os targets do Prometheus estão UP"""
    try:
        response = requests.get('http://localhost:9090/api/v1/targets', timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                active_targets = data['data']['activeTargets']
                all_up = True
                
                print("\nTargets do Prometheus:")
                for target in active_targets:
                    job = target['labels']['job']
                    health = target['health']
                    if health == 'up':
                        print(f"  ✓ {job}: UP")
                    else:
                        print(f"  ✗ {job}: DOWN")
                        all_up = False
                
                return all_up
    except Exception as e:
        print(f"✗ Erro ao verificar targets: {e}")
        return False

def check_metrics_content(url):
    """Verifica se o endpoint de métricas tem conteúdo válido"""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            content = response.text
            # Verificar se tem métricas
            lines = [line for line in content.split('\n') if line and not line.startswith('#')]
            if len(lines) > 0:
                return True, len(lines)
            else:
                return False, 0
        return False, 0
    except:
        return False, 0

def main():
    print("=" * 60)
    print("Verificação do Sistema de Monitoramento")
    print("=" * 60)
    print()
    
    results = []
    
    print("Verificando serviços principais...")
    print("-" * 60)
    
    # Verificar Prometheus
    results.append(check_service("Prometheus", "http://localhost:9090/-/healthy"))
    
    # Verificar Grafana
    results.append(check_service("Grafana", "http://localhost:3000/api/health"))
    
    # Verificar Metrics Exporter
    result = check_service("Metrics Exporter", "http://localhost:8000/metrics")
    results.append(result)
    
    if result:
        has_content, count = check_metrics_content("http://localhost:8000/metrics")
        if has_content:
            print(f"  → {count} métricas sendo exportadas")
        else:
            print(f"  → AVISO: Endpoint respondeu mas sem métricas")
    
    # Verificar API Monitor
    result = check_service("API Monitor", "http://localhost:8001/metrics")
    results.append(result)
    
    if result:
        has_content, count = check_metrics_content("http://localhost:8001/metrics")
        if has_content:
            print(f"  → {count} métricas sendo exportadas")
        else:
            print(f"  → AVISO: Endpoint respondeu mas sem métricas")
    
    print()
    
    # Verificar targets do Prometheus
    print("Verificando integração Prometheus...")
    print("-" * 60)
    time.sleep(1)  # Aguardar um pouco para Prometheus atualizar
    targets_ok = check_prometheus_targets()
    results.append(targets_ok)
    
    print()
    print("=" * 60)
    
    # Resumo
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✓ Todos os testes passaram ({passed}/{total})")
        print()
        print("Sistema funcionando corretamente! 🎉")
        print()
        print("Próximos passos:")
        print("  1. Acesse o Grafana: http://localhost:3000")
        print("  2. Login: admin / admin")
        print("  3. Veja o dashboard 'Infrastructure Monitoring'")
        print()
        return 0
    else:
        print(f"✗ Alguns testes falharam ({passed}/{total} passaram)")
        print()
        print("Solução de problemas:")
        print("  1. Verifique se todos os serviços foram iniciados")
        print("  2. Execute: docker-compose ps")
        print("  3. Verifique os logs: docker-compose logs")
        print("  4. Certifique-se de que as portas não estão ocupadas")
        print()
        return 1

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nVerificação cancelada pelo usuário")
        sys.exit(1)
