# docs/

Este diretório contém documentação adicional, imagens e recursos.

## Estrutura

```
docs/
├── images/              # Screenshots e diagramas
│   ├── dashboard-main.png
│   ├── prometheus-queries.png
│   ├── system-metrics.png
│   ├── api-monitoring.png
│   └── ...
├── architecture/        # Diagramas de arquitetura
│   └── system-diagram.png
└── examples/            # Exemplos de configuração
    ├── custom-metrics.py
    ├── custom-alerts.yml
    └── custom-dashboard.json
```

## Adicionando Screenshots

Para adicionar screenshots ao projeto:

1. Capture a imagem do sistema rodando
2. Salve em `docs/images/` com um nome descritivo
3. Referencie no README ou SCREENSHOTS.md

### Exemplo

```markdown
![Meu Dashboard](docs/images/meu-dashboard.png)
```

## Diagrama de Arquitetura

```
┌─────────────────┐
│  Sistema Alvo   │
│   (Servidor)    │
└────────┬────────┘
         │
    ┌────▼────┐
    │ Metrics │
    │ Exporter│ :8000
    └────┬────┘
         │
    ┌────▼────┐
    │   API   │
    │ Monitor │ :8001
    └────┬────┘
         │
    ┌────▼────────┐
    │ Prometheus  │ :9090
    │  (Storage)  │
    └────┬────────┘
         │
    ┌────▼────────┐
    │   Grafana   │ :3000
    │ (Dashboard) │
    └─────────────┘
```

## Recursos Adicionais

- [Guia de Contribuição](../CONTRIBUTING.md)
- [Guia Rápido](../QUICKSTART.md)
- [Extensão de Métricas](../EXTENDING.md)
