# Security Policy

## Versões Suportadas

Atualmente mantemos suporte de segurança para as seguintes versões:

| Versão | Suportada          |
| ------ | ------------------ |
| 1.0.x  | :white_check_mark: |

## Reportar uma Vulnerabilidade

Se você descobrir uma vulnerabilidade de segurança neste projeto, por favor nos avise o mais rápido possível.

### Como Reportar

**NÃO crie uma issue pública** para vulnerabilidades de segurança.

Em vez disso:

1. **Email**: Envie detalhes para [seu-email@example.com] (substitua por seu email)
2. **GitHub Security**: Use o recurso de [Security Advisories](../../security/advisories/new) do GitHub

### Informações a Incluir

Por favor, inclua o máximo de informações possível:

- Tipo de vulnerabilidade
- Localização do código afetado (arquivo e linha)
- Passos para reproduzir
- Impacto potencial
- Possíveis soluções (se tiver)

### Processo de Resposta

1. **Confirmação**: Confirmaremos o recebimento em 48 horas
2. **Avaliação**: Avaliaremos a vulnerabilidade em 7 dias
3. **Correção**: Trabalharemos em uma correção
4. **Release**: Lançaremos uma versão corrigida
5. **Divulgação**: Divulgaremos os detalhes após o patch

### Política de Divulgação

- Aguardamos pelo menos 90 dias antes de divulgar publicamente
- Creditaremos o descobridor (se desejar)
- Publicaremos um security advisory detalhado

## Boas Práticas de Segurança

### Para Usuários

- ✅ Sempre use a versão mais recente
- ✅ Configure senhas fortes para Grafana
- ✅ Use HTTPS em produção
- ✅ Limite acesso às portas de monitoramento
- ✅ Mantenha o arquivo `.env` seguro e fora do Git
- ✅ Atualize as imagens Docker regularmente

### Para Desenvolvedores

- ✅ Nunca commite credenciais
- ✅ Use variáveis de ambiente para dados sensíveis
- ✅ Valide e sanitize inputs
- ✅ Mantenha dependências atualizadas
- ✅ Faça code review de segurança

## Dependências

Monitoramos vulnerabilidades em nossas dependências:

- `prometheus-client`
- `psutil`
- `flask`
- `requests`
- `python-dotenv`

Use `pip audit` ou `safety check` para verificar vulnerabilidades.

## Contato

Para questões não urgentes de segurança, abra uma issue ou entre em contato através das discussões do projeto.

---

**Obrigado por ajudar a manter este projeto seguro! 🔒**
