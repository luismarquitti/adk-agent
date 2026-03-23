# M04: Complex Workflows (Routing & Chaining)

Neste módulo avançamos da delegação estática de Agentes (`Agent-as-a-Tool` no M03) para **Routing Condicional**, permitindo a orquestração dinâmica da chamada dos LLMs baseada no roteiro das intenções do usuário.

## Estrutura do Workflow SWEBOK

O cenário é a construção e o controle de evolução de software rigoroso pela conformidade do SWEBOK (Software Engineering Body of Knowledge V4).

### Como o Workflow Funciona (Pipeline em `workflow.py`):
1. **O Gatilho (User Request):** Alguém pede para fazer um software do zero ou adicionar uma feature nova em algo que já existe.
2. **Router Agent (`router_agent`):** O primeiro LLM restrito via *Structured Output*, configurado com temperature=0.0. Ele devolve EXCLUSIVAMENTE um JSON `{"route": "NEW_PROJECT" | "NEW_FEATURE"}`.
3. **Chaveamento e Execução Especialista (Branching):**
   - Se foi `NEW_PROJECT`, chamamos o **Ideation Expert**, que levanta requisitos embrionários.
   - Se foi `NEW_FEATURE`, chamamos o **Feature Analyst**, focado em análise de impacto.
4. **SWEBOK Compliance Convergence (Chaining):** Qualquer que tenha sido a rota tomada no passo 3, o resultado cru é passado para o validador definitivo: O **SWEBOK Auditor**. Ele enriquece, audita e formata os achados gerando conformidade automática com as áreas de conhecimento de *Software Requirements* e *Software Design*.

## Testando

### 1. Testes Estáticos (Pytest)
```bash
python -m pytest m04_complex_workflows/test_workflow.py -v
```

### 2. Testes de Fluxo
Execute o workflow diretamente na raiz com a ativação prévia do backend de Python assíncrono:
```bash
python m04_complex_workflows/workflow.py
```
*(Cuidado: Exige ambiente com sua `.env` injetando GEMINI_API_KEY corretamente e acessibilidade de Event Loops na sua máquina)*
