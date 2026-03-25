import os
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.tools.load_memory_tool import load_memory_tool

load_dotenv()

# System Instruction
sys_instruction = (
    "Você é um Assistente Pessoal altamente capaz desenvolvido com o Google ADK. "
    "Seu objetivo é ajudar o usuário com base no histórico da conversa atual e, "
    "se necessário, resgatar informações cruciais de sessões antigas usando a ferramenta 'load_memory_tool'. "
    "Sempre seja prestativo, lembre-se do contexto (nome do usuário, detalhes passados) e "
    "seja amigável e conciso."
)

# Cria e exporta o agente nativo do ADK
root_agent = Agent(
    name="Agente_com_Memoria",
    instruction=sys_instruction,
    tools=[load_memory_tool],
    include_contents="default" # Utiliza o buffer de memória padrão da sessão atual
)

if __name__ == "__main__":
    print("Agente de Memória (M05) configurado com sucesso!")
    print("Teste-o passando informações e, na mesma sessão, pergunte sobre elas.")
    print("Para interagir através do painel da web:")
    print("1. adk api_server --allow_origins=http://localhost:4200 --host=0.0.0.0 --agent-path=m05_memory.agent:root_agent")
    print("2. Abra o ADK Web Frontend (http://localhost:4200)")
