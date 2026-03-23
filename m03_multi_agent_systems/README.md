# Módulo 3: Multi-Agent Systems (Agent-as-a-Tool)

Aprenda a construir sistemas multi-agentes robustos utilizando o padrão **Agent-as-a-Tool**.

## O Padrão: Agent-as-a-Tool 🛠️

Em arquiteturas avançadas, agentes de Inteligência Artificial podem colaborar para resolver problemas complexos. Em vez de termos um único "Agente Faz Tudo", é muito mais eficiente e seguro delegar funções a especialistas focados.

No Google ADK, esse padrão é atingido de forma nativa e elegante passando instâncias de `Agent` diretamente na **lista de `tools`** de outro Agente. O agente superior trata o agente subordinado como uma ferramenta que ele pode "chamar" para obter um resultado.

Isso cria uma hierarquia clara:
`Orquestrador -> Delega para Ferramenta A (Agente Especialista)`

## O Nosso Cenário: Squad de Engenharia de Software 🧑‍💻

Neste módulo, simulamos um Squad de Engenharia de Software ágil. Quando o usuário pede a implementação de uma funcionalidade, quem recebe o pedido é o Tech Lead, que por sua vez coordena a equipe:

1.  **Tech Lead Agent (`agent.py`)**: O orquestrador. Recebe as especificações e não escreve código diretamente. Ele invoca as seguintes ferramentas sequencialmente:
    *   **Coder Agent (`specialized_agents.py`)**: O desenvolvedor. Recebe a especificação e escreve o código Python base.
    *   **Reviewer Agent (`specialized_agents.py`)**: O revisor sênior. Recebe o código do Coder, analisa falhas de segurança/performance e dá o aval.
    *   **Tester Agent (`specialized_agents.py`)**: O engenheiro de QA. Escreve a suíte de testes unitários baseada no código aprovado.

O usuário que chama a interface da ADK só vê o Tech Lead e seu report final, contendo o resultado consolidado do trabalho dos agentes subordinados.

## Como Executar e Testar 🚀

Para ver a mágica do trabalho em equipe acontecer na prática:

1. Inicie a stack do projeto (Backend e Web UI). Do diretório raiz (`adk-agent`), rode o comando:
   ```bash
   npm run dev
   ```
*(Caso esteja reiniciando para carregar este módulo, lembre-se de parar o seu backend de módulos anteriores. Mas se a interface estiver rodando, use a UI via localhost).*

2. Acesse o **ADK Web UI** (geralmente em `http://localhost:4200`).

3. No painel lateral ou seletor de caminho, certifique-se de direcionar os requests do backend para rodar dentro deste diretório (`m03_multi_agent_systems/`).

4. Faça um pedido complexo ao Agente, por exemplo:
   > *"Preciso de uma função Python que calcule os juros compostos considerando aportes mensais, retorne o montante final e a evolução mês a mês."*

5. Acompanhe a interação. O Tech Lead acionará sequencialmente seus agentes, trazendo código, avaliação e testes para você.
