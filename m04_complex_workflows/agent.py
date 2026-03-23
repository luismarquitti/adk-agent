
from google.adk import Agent
from .workflow import run_complex_workflow

async def execute_swebok_workflow(user_request: str) -> str:
    """
    Ferramenta obrigatória para ser chamada SEMPRE que o usuário fizer um pedido.
    Ela executa a orquestração complexa (Router -> Especialista -> SWEBOK) e retorna a markdown gerada.
    """
    result = await run_complex_workflow(user_request)
    return result["swebok_document"]

root_agent = Agent(
    name="workflow_facade_agent",
    instruction="""
    Você é a interface principal do Módulo 04 (Complex Workflows).
    Sua única missão é pegar o input do usuário e passá-lo para a ferramenta 'execute_swebok_workflow'.
    O retorno dessa ferramenta será um documento Markdown massivo e detalhado, estruturado em SWEBOK V4.
    Devolva rigorosamente o conteúdo integral que a ferramenta te retornar, sem resumir.
    """,
    tools=[execute_swebok_workflow]
)
