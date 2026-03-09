#!/usr/bin/env python3
"""
API de Exemplo para Testes
Uma API simples para testar o sistema de monitoramento
"""

from flask import Flask, jsonify
import time
import random

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def home():
    return jsonify({
        'message': 'API de Exemplo - Sistema de Monitoramento',
        'status': 'running',
        'uptime_seconds': round(time.time() - start_time, 2)
    })

@app.route('/health')
def health():
    """Endpoint de health check"""
    health_status = {
        'status': 'healthy',
        'timestamp': time.time(),
        'uptime': round(time.time() - start_time, 2),
        'service': 'example-api'
    }
    return jsonify(health_status), 200

@app.route('/api/status')
def status():
    """Endpoint de status com informações detalhadas"""
    return jsonify({
        'status': 'ok',
        'version': '1.0.0',
        'uptime_seconds': round(time.time() - start_time, 2),
        'timestamp': time.time()
    }), 200

@app.route('/api/slow')
def slow():
    """Endpoint que demora para responder (para testar tempo de resposta)"""
    delay = random.uniform(1, 3)
    time.sleep(delay)
    return jsonify({
        'message': 'Resposta lenta',
        'delay_seconds': round(delay, 2)
    }), 200

@app.route('/api/error')
def error():
    """Endpoint que retorna erro (para testar monitoramento de erros)"""
    error_codes = [400, 500, 503]
    code = random.choice(error_codes)
    return jsonify({
        'error': 'Erro simulado',
        'code': code
    }), code

@app.route('/api/data')
def data():
    """Endpoint com dados fictícios"""
    return jsonify({
        'users': random.randint(100, 1000),
        'active_sessions': random.randint(10, 100),
        'requests_per_minute': random.randint(50, 500),
        'timestamp': time.time()
    }), 200

if __name__ == '__main__':
    print("=" * 50)
    print("API de Exemplo - Sistema de Monitoramento")
    print("=" * 50)
    print("\nEndpoints disponíveis:")
    print("  - http://localhost:5000/")
    print("  - http://localhost:5000/health")
    print("  - http://localhost:5000/api/status")
    print("  - http://localhost:5000/api/slow (resposta lenta)")
    print("  - http://localhost:5000/api/error (retorna erros)")
    print("  - http://localhost:5000/api/data")
    print("\nPara monitorar esta API, adicione no .env:")
    print("MONITORED_APIS=http://localhost:5000/health")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=False)
