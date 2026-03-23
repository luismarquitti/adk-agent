# Module 1: Build Your First AI Agent

## Overview
Neste módulo, você irá criar seu primeiro agente: um Especialista em Desenvolvimento de Software Assistido por IA. Usaremos a biblioteca `google-genai` e, por baixo dos panos, o agente terá acesso à pesquisa do Google em tempo real. O agente tem um comportamento programado para formatar as respostas na forma de tutoriais e relatórios técnicos.

## Pré-requisitos: Setup no Google Cloud Console

Para conseguirmos as credenciais com as opções de segurança e cota de um projeto Enterprise:

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/).
2. **Criar Projeto:** Clique no menu de projetos no topo (ao lado do logo) e clique em "New Project". Dê um nome (ex: `adk-agent-course`) e conclua a criação.
3. **Faturamento (Billing):** No menu lateral esquerdo, vá em **Billing** (Faturamento) e vincule uma conta de faturamento ativa a este novo projeto. Diversas APIs do ecossistema de GenAI exigem faturamento validado para escalar ou liberar ferramentas nativas.
4. **Habilitar API:** Vá em **APIs & Services > Library**. Pesquise por `Generative Language API` e clique em **Enable** (Ativar).
   *Nota: Caso o Google AI Studio redirecione sua API para projetos Cloud, certifique-se de vincular a API Key a este projeto.*
5. **Gerar Credenciais:**
   - Acesse **APIs & Services > Credentials**.
   - Clique em **Create Credentials > API Key**.
   - Copie a chave gerada e cole no seu arquivo `.env` (na raiz do repositório) no campo `GEMINI_API_KEY`.

## Executando o Agente

1. Certifique-se de que o ambiente virtual está ativado na raiz (`.\.venv\Scripts\Activate.ps1`) e as dependências instaladas (`pip install -r requirements.txt`).
2. Acesse esta pasta ou chame o script a partir da raiz.
3. Forneça a sua pergunta técnica como argumento.

Exemplo de uso:
```pwsh
python 01_first_agent/agent.py "Como as goroutines em Go lidam com acesso a variáveis globais? Mande referências da documentação e tutoriais."
```

O agente irá buscar a informação e compilar um relatório denso para você.
