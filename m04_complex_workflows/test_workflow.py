import pytest
from m04_complex_workflows.agents import router_agent, ideation_agent, feature_agent, swebok_agent

def test_workflow_agents_initialization():
    """Valida se todos os agentes especialistas em SWEBOK estão devidamente instanciados e configurados sem erros Pydantic."""
    assert router_agent.name == "workflow_router"
    assert "roteador lógico" in router_agent.instruction
    
    assert ideation_agent.name == "ideation_expert"
    assert feature_agent.name == "feature_analyst"
    
    assert swebok_agent.name == "swebok_auditor"
    assert "SWEBOK" in swebok_agent.instruction

def test_workflow_has_callable_entrypoint():
    """Teste estático para garantir que a função assíncrona raiz foi exportada de acordo."""
    from m04_complex_workflows.workflow import run_complex_workflow
    assert callable(run_complex_workflow), "O script workflow.py deve exportar 'run_complex_workflow'."
