import os
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool

# Carrega a API Key (GEMINI_API_KEY) do .env
load_dotenv()

# System Instruction
sys_instruction = (
    "Você é um Engenheiro de Software Sênior assistido por IA. "
    "Quando o usuário fizer uma pergunta técnica ou pedir ajuda, "
    "você deve obrigatoriamente realizar buscas na web (incluindo documentações e GitHub) "
    "para fundamentar sua resposta. "
    "Sua resposta final DEVE ser formatada como um relatório ou tutorial passo-a-passo detalhado em formato Markdown."
)

# Cria e exporta o agente nativo do ADK
root_agent = Agent(
    name="Especialista_em_Software",
    instruction=sys_instruction,
    tools=[GoogleSearchTool()]
)

if __name__ == "__main__":
    print("Agente ADK configurado com sucesso!")
    print("Para interagir com este agente através do painel:")
    print("1. adk api_server --allow_origins=http://localhost:4200 --host=0.0.0.0")
    print("2. Abra o ADK Web Frontend (http://localhost:4200)")
