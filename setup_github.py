#!/usr/bin/env python3
"""
Script de configuração inicial do projeto
Prepara o projeto para publicação no GitHub
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header(text):
    """Imprime um cabeçalho formatado"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")

def print_step(step, total, description):
    """Imprime um passo da configuração"""
    print(f"[{step}/{total}] {description}")

def check_git():
    """Verifica se o Git está instalado"""
    try:
        subprocess.run(['git', '--version'], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_docker():
    """Verifica se o Docker está rodando"""
    try:
        subprocess.run(['docker', 'info'], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_python_version():
    """Verifica a versão do Python"""
    version = sys.version_info
    return version.major == 3 and version.minor >= 8

def customize_readme():
    """Ajuda a customizar o README"""
    print("\n📝 Customizando README.md...")
    
    username = input("Digite seu username do GitHub (ou Enter para pular): ").strip()
    if username:
        readme_path = Path("README.md")
        if readme_path.exists():
            content = readme_path.read_text(encoding='utf-8')
            content = content.replace('seu-usuario', username)
            readme_path.write_text(content, encoding='utf-8')
            print(f"✓ README atualizado com username: {username}")
    
    name = input("Digite seu nome para os autores (ou Enter para pular): ").strip()
    if name:
        readme_path = Path("README.md")
        if readme_path.exists():
            content = readme_path.read_text(encoding='utf-8')
            content = content.replace('**Seu Nome**', f'**{name}**')
            readme_path.write_text(content, encoding='utf-8')
            print(f"✓ Nome do autor atualizado: {name}")

def customize_security():
    """Ajuda a customizar o SECURITY.md"""
    print("\n🔒 Customizando SECURITY.md...")
    
    email = input("Digite seu email de contato (ou Enter para pular): ").strip()
    if email:
        security_path = Path("SECURITY.md")
        if security_path.exists():
            content = security_path.read_text(encoding='utf-8')
            content = content.replace('[seu-email@example.com]', email)
            content = content.replace('seu-email@example.com', email)
            security_path.write_text(content, encoding='utf-8')
            print(f"✓ SECURITY.md atualizado com email: {email}")

def check_env_file():
    """Verifica se o arquivo .env existe"""
    env_path = Path(".env")
    env_example_path = Path(".env.example")
    
    if not env_path.exists() and env_example_path.exists():
        print("\n⚠️  Arquivo .env não encontrado")
        create = input("Deseja criar .env a partir do .env.example? (s/N): ").strip().lower()
        if create == 's':
            import shutil
            shutil.copy(env_example_path, env_path)
            print("✓ Arquivo .env criado")
            print("  Não se esqueça de adicionar suas APIs no arquivo .env")
    elif env_path.exists():
        print("✓ Arquivo .env já existe")

def check_gitignore():
    """Verifica se o .gitignore está correto"""
    gitignore_path = Path(".gitignore")
    if gitignore_path.exists():
        content = gitignore_path.read_text()
        if ".env" in content:
            print("✓ .gitignore está configurado corretamente")
            return True
    print("⚠️  Verificar .gitignore manualmente")
    return False

def init_git_repo():
    """Inicializa o repositório Git"""
    if not Path(".git").exists():
        print("\n📦 Inicializando repositório Git...")
        init = input("Deseja inicializar o repositório Git? (s/N): ").strip().lower()
        if init == 's':
            try:
                subprocess.run(['git', 'init'], check=True)
                print("✓ Repositório Git inicializado")
                
                subprocess.run(['git', 'add', '.'], check=True)
                print("✓ Arquivos adicionados ao staging")
                
                subprocess.run([
                    'git', 'commit', '-m', 
                    'Initial commit: Sistema de Monitoramento de Infraestrutura'
                ], check=True)
                print("✓ Commit inicial criado")
                
                return True
            except subprocess.CalledProcessError as e:
                print(f"✗ Erro ao inicializar Git: {e}")
                return False
    else:
        print("✓ Repositório Git já inicializado")
        return True

def show_next_steps():
    """Mostra os próximos passos"""
    print_header("Próximos Passos")
    
    print("1. 🌐 Crie um repositório no GitHub:")
    print("   https://github.com/new")
    print()
    print("2. 📤 Adicione o remote e faça push:")
    print("   git remote add origin https://github.com/SEU-USUARIO/infrastructure-monitoring.git")
    print("   git branch -M main")
    print("   git push -u origin main")
    print()
    print("3. 📸 Adicione screenshots:")
    print("   - Execute o sistema (start.bat)")
    print("   - Tire prints do Grafana")
    print("   - Salve em docs/images/")
    print()
    print("4. 📝 Revise e atualize:")
    print("   - README.md - Adicione seu usuário do GitHub")
    print("   - SECURITY.md - Adicione seu email")
    print("   - LICENSE - Revise se necessário")
    print()
    print("5. 🎉 Divulgue seu projeto!")
    print()
    print("📚 Documentação detalhada: GITHUB_SETUP.md")

def main():
    """Função principal"""
    print_header("Setup para Publicação no GitHub")
    print("Este script ajudará a preparar o projeto para publicação.")
    
    total_steps = 7
    
    # Passo 1: Verificar Python
    print_step(1, total_steps, "Verificando versão do Python")
    if check_python_version():
        print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detectado")
    else:
        print("✗ Python 3.8+ é necessário")
        return
    
    # Passo 2: Verificar Git
    print_step(2, total_steps, "Verificando Git")
    if check_git():
        print("✓ Git instalado")
    else:
        print("✗ Git não encontrado. Instale em: https://git-scm.com/")
        return
    
    # Passo 3: Verificar Docker
    print_step(3, total_steps, "Verificando Docker")
    if check_docker():
        print("✓ Docker rodando")
    else:
        print("⚠️  Docker não está rodando (necessário para executar o sistema)")
    
    # Passo 4: Verificar .env
    print_step(4, total_steps, "Verificando arquivo .env")
    check_env_file()
    
    # Passo 5: Verificar .gitignore
    print_step(5, total_steps, "Verificando .gitignore")
    check_gitignore()
    
    # Passo 6: Customizar arquivos
    print_step(6, total_steps, "Customizando arquivos")
    customize = input("\nDeseja customizar README e SECURITY agora? (s/N): ").strip().lower()
    if customize == 's':
        customize_readme()
        customize_security()
    
    # Passo 7: Inicializar Git
    print_step(7, total_steps, "Configurando Git")
    init_git_repo()
    
    # Mostrar próximos passos
    show_next_steps()
    
    print("\n✅ Setup concluído!")
    print("\nO projeto está pronto para ser publicado no GitHub.")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelado pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        sys.exit(1)
