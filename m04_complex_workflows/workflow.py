import asyncio
import json
import uuid
from google.adk.runners import InMemoryRunner
from google.genai import types

# Se quisermos testar localmente as integrações diretamente via Runner
from m04_complex_workflows.agents import router_agent, ideation_agent, feature_agent, swebok_agent


async def get_agent_response(agent, request_text: str) -> str:
    """Helper function to run an agent via InMemoryRunner and extract the final text."""
    runner = InMemoryRunner(app_name="m04_complex_workflows", agent=agent)
    
    # Create the session first with a random ID
    session_id = str(uuid.uuid4())
    user_id = "default_user"
    await runner.session_service.create_session(
        app_name="m04_complex_workflows", 
        user_id=user_id, 
        session_id=session_id
    )
    
    msg = types.Content(role="user", parts=[types.Part.from_text(text=request_text)])
    
    final_output = ""
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=msg):
        if event.is_final_response() and event.content and event.content.parts:
            # Pegamos o texto final gerado pelo modelo
            final_output = event.content.parts[0].text
            
    return final_output


async def run_complex_workflow(user_request: str) -> dict:
    """
    Orquestra o Complex Workflow:
    1. Passa no Router Agent
    2. Direciona ao Ideation ou Feature Agent
    3. Passa o resultado para o Swebok Agent (Chain)
    """
    print(f"\n[Workflow] Iniciando Orquestração para a requisição: '{user_request}'")
    
    # 1. Router Step
    print("[Router] Consultando Router Agent...")
    response_text = await get_agent_response(router_agent, user_request)
    
    route_data = {"route": "UNKNOWN"}
    
    # Tratando markdown code blocks se o modelo ainda retorná-lo
    if "```json" in response_text:
        response_text = response_text.split("```json")[-1].split("```")[0].strip()
        
    try:
        route_data = json.loads(response_text)
    except json.JSONDecodeError:
        print(f"[Router Warning] Erro de parse no JSON. Fallback para detecção por regex. Resposta crua: {response_text}")
        if "NEW_FEATURE" in response_text:
            route_data["route"] = "NEW_FEATURE"
        elif "NEW_PROJECT" in response_text:
            route_data["route"] = "NEW_PROJECT"
            
    chosen_route = route_data.get("route", "NEW_PROJECT") # Fallback padrão
    print(f"[Router] Rota selecionada: {chosen_route}")
    
    # 2. Execution Step (Ideation ou Feature)
    analysis_text = ""
    if chosen_route == "NEW_FEATURE":
        print("[Execution] Acionando Feature Analyst Agent...")
        analysis_text = await get_agent_response(feature_agent, user_request)
    else:
        print("[Execution] Acionando Ideation Expert Agent...")
        analysis_text = await get_agent_response(ideation_agent, user_request)
            
    print("[Execution] Análise concluída pelos especialistas. Passando para SWEBOK Auditor...")
    
    # 3. Chain Convergence (SWEBOK)
    swebok_prompt = f"""
    Aqui está a análise detalhada pelo especialista sobre a requisição original do usuário ({user_request}):
    {analysis_text}
    
    Transforme essa análise no documento de conformidade SWEBOK oficial com suas descrições de KA.
    """
    print("[SWEBOK] Acionando SWEBOK Auditor Agent...")
    final_output = await get_agent_response(swebok_agent, swebok_prompt)
    if not final_output:
        final_output = "Erro na formatação."
    
    return {
        "route": chosen_route,
        "specialist_analysis": analysis_text,
        "swebok_document": final_output
    }

if __name__ == "__main__":
    # Teste rápido
    try:
        result = asyncio.run(run_complex_workflow("Gostaria de refatorar o login para aceitar Auth do Google num app existente."))
        print("\n================ FINAL DOCUMENT ================\n", result["swebok_document"])
    except RuntimeError as e:
        if "This event loop is already running" in str(e):
             # Em jupyter/alguns kernels isso ocorre
             import nest_asyncio
             nest_asyncio.apply()
             result = asyncio.run(run_complex_workflow("Gostaria de criar o proximo Instagram descentralizado do zero."))
             print("\n================ FINAL DOCUMENT ================\n", result["swebok_document"])
