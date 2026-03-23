import os
from dotenv import load_dotenv

from google.adk import Agent
from m02_custom_tools.github_tools import (
    create_issue,
    list_open_issues,
    update_issue_comment,
    list_github_files,
    read_github_file
)
from m02_custom_tools.drive_tools import (
    list_drive_documents,
    read_drive_document,
    save_local_document
)

# Carrega as variáveis de ambiente (GEMINI_API_KEY, GITHUB_TOKEN, GITHUB_REPO, GOOGLE_APPLICATION_CREDENTIALS)
load_dotenv()

# Instruções de Sistema para o Agente focado em Gestão de Projetos
sys_instruction = (
    "Você é um Gerente de Projetos de Software Sênior (PM/PO) assistido por IA. "
    "Sua principal responsabilidade é alinhar os documentos de negócio do Google Drive "
    "com a organização do repositório no GitHub (tanto o código em si quanto as Issues). "
    "Sempre que precisar atuar ou planejar atividades, siga esta abordagem: "
    "1. Leia o contexto: Verifique o que está definido no projeto lendo os documentos de requisitos via 'read_drive_document' (ID via 'list_drive_documents'). "
    "2. Analise a realidade técnica: Use as ferramentas 'list_github_files' e 'read_github_file' para espiar o repositório. "
    "3. Sincronize ideias: Verifique as issues atuais ('list_open_issues') e crie tarefas técnicas ('create_issue'). "
    "4. Se você precisar gerar ou salvar um NOVO documento para o projeto, NUNCA crie no drive. Use a ferramenta 'save_local_document' que salvará em formato Markdown no diretório ./outputs local."
    "Sempre documente e informe o usuário o relatório do que você executou."
)

# Cria e exporta o agente nativo do ADK
root_agent = Agent(
    name="Gerente_Projeto",
    instruction=sys_instruction,
    tools=[
        create_issue, 
        list_open_issues, 
        update_issue_comment,
        list_github_files,
        read_github_file,
        list_drive_documents, 
        read_drive_document, 
        save_local_document
    ]
)

if __name__ == "__main__":
    print("PM Agent do Módulo 2 configurado com sucesso!")
    print("Para interagir com este agente através do painel:")
    print("1. Certifique-se de configurar as credenciais (veja os arquivos .md)")
    print("2. Execute o servidor ADK (na raiz do projeto): adk api_server --allow_origins=http://localhost:4200 --host=0.0.0.0")
    print("3. Abra o ADK Web Frontend (http://localhost:4200)")
