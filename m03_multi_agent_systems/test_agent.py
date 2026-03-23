import pytest
from google.adk import Agent

def test_m03_agent_loads_without_validation_errors():
    """
    Este teste simula a inicialização do módulo agent.py do m03_multi_agent_systems.
    Ele irá falhar se houver algum erro de sintaxe ou erro de Pydantic ValidationError.
    Rode isso antes de npm run dev para garantir a integridade do agente.
    """
    try:
        from m03_multi_agent_systems.agent import root_agent
        
        assert isinstance(root_agent, Agent), "root_agent não é uma instância de google.adk.Agent"
        assert len(root_agent.sub_agents) == 3, "root_agent deve ter 3 sub_agents definidos"
        assert root_agent.sub_agents[0].name == "coder_agent"
        assert root_agent.sub_agents[1].name == "reviewer_agent"
        assert root_agent.sub_agents[2].name == "test_agent"
        
    except ImportError as e:
        pytest.fail(f"Falha ao importar o root_agent: {e}")
    except Exception as e:
        pytest.fail(f"Exceção inesperada na inicialização do agente: {e}")

def test_specialized_agents_loaded_correctly():
    """Valida que os agentes especialistas também carregam suas instruções perfeitamente, sem Extra Inputs."""
    try:
        from m03_multi_agent_systems.specialized_agents import coder_agent, reviewer_agent, test_agent
        
        assert hasattr(coder_agent, "instruction")
        assert "Coder" in coder_agent.instruction
        
    except Exception as e:
        pytest.fail(f"Falha na validação dos agentes subordinados: {e}")
