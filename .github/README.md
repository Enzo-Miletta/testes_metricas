# GitHub Configuration

Este diretório contém toda a configuração relacionada ao GitHub.

## 📁 Estrutura

```
.github/
├── workflows/              # GitHub Actions (CI/CD)
│   ├── python-app.yml     # Tests e lint do código Python
│   └── markdown-lint.yml  # Lint dos arquivos Markdown
│
├── ISSUE_TEMPLATE/         # Templates de Issues
│   ├── bug_report.md      # Para reportar bugs
│   ├── feature_request.md # Para sugerir features
│   ├── question.md        # Para fazer perguntas
│   └── config.yml         # Configuração e links
│
└── PULL_REQUEST_TEMPLATE.md # Template de Pull Requests
```

## 🔄 Workflows (GitHub Actions)

### python-app.yml

Executa automaticamente em cada push ou PR:

- ✅ Testa em múltiplos sistemas operacionais (Ubuntu, Windows)
- ✅ Testa em múltiplas versões Python (3.8, 3.9, 3.10, 3.11)
- ✅ Instala dependências
- ✅ Executa flake8 para verificar código
- ✅ Compila arquivos Python
- ✅ Valida Docker Compose

### markdown-lint.yml

Valida arquivos Markdown:

- ✅ Verifica formatação
- ✅ Garante qualidade da documentação
- ✅ Mantém consistência

## 📝 Issue Templates

### Bug Report

Template estruturado para reportar bugs incluindo:

- Descrição do problema
- Passos para reproduzir
- Comportamento esperado vs atual
- Ambiente (OS, Python, Docker)
- Logs e screenshots

### Feature Request

Template para sugerir novas funcionalidades:

- Descrição da feature
- Problema que resolve
- Solução proposta
- Alternativas consideradas
- Exemplos de uso

### Question

Template para perguntas:

- Pergunta clara
- Contexto
- O que já tentou
- Ambiente (se relevante)

### Config

Configura links úteis na página de criação de issues:

- 📚 Documentação
- ⚡ Guia Rápido
- 💬 Discussions
- 🔒 Reportar Vulnerabilidade

## 🔀 Pull Request Template

Template completo para PRs incluindo:

- Descrição da mudança
- Tipo de mudança (bug, feature, docs, etc)
- Checklist de verificação
- Instruções de teste
- Issues relacionadas

## 🚀 Como Usar

### Criar uma Issue

1. Vá para a aba **Issues** do repositório
2. Clique em **New Issue**
3. Escolha o template apropriado
4. Preencha as informações solicitadas
5. Submeta a issue

### Criar um Pull Request

1. Fork o repositório
2. Crie um branch (`git checkout -b feature/MinhaFeature`)
3. Faça commit das mudanças
4. Push para o branch
5. Abra um Pull Request
6. O template será aplicado automaticamente

### Visualizar Actions

1. Vá para a aba **Actions** do repositório
2. Veja o status dos workflows
3. Clique em um run para ver detalhes

## ⚙️ Personalização

### Modificar Workflows

Edite os arquivos em `workflows/`:

```yaml
# Adicionar mais versões do Python
python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']

# Adicionar mais sistemas operacionais
os: [ubuntu-latest, windows-latest, macos-latest]

# Adicionar mais steps
- name: Meu Step
  run: comando-aqui
```

### Modificar Templates

Edite os arquivos `.md` em `ISSUE_TEMPLATE/`:

- Adicione ou remova seções
- Personalize labels
- Ajuste assignees

## 📊 Status Badges

Adicione badges ao README para mostrar status:

```markdown
![CI](https://github.com/usuario/repo/workflows/Python%20Application%20Tests/badge.svg)
![Markdown](https://github.com/usuario/repo/workflows/Markdown%20Linter/badge.svg)
```

## 🔒 Segurança

- Workflows só executam em branches autorizadas
- Secrets do GitHub são usados para credenciais
- PRs de forks têm permissões limitadas

## 📚 Recursos

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Issue Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)
- [Workflow Syntax](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)

---

**Dica**: Explore a aba Actions do repositório após o primeiro push para ver os workflows em ação!
