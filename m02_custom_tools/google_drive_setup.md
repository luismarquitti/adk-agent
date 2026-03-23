# Configuração do Google Drive API

Para que o nosso agente do Módulo 2 consiga ler e escrever documentos no Google Drive (como PRDs, atas de reunião, Roadmap), precisamos autenticar o acesso usando um **Service Account** (Conta de Serviço) do Google Cloud.

## Passo 1: Criar um Projeto no Google Cloud Console

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/).
2. Clique no seletor de projetos no menu superior e depois em **Novo Projeto** (New Project).
3. Dê um nome ao seu projeto (ex: `Agent-Development-Kit`) e clique em **Criar**.
4. Selecione o projeto recém-criado.

## Passo 2: Habilitar a Google Drive API

1. No menu lateral esquerdo (hambúrguer), vá em **APIs e Serviços** > **Biblioteca**.
2. Na barra de pesquisa, digite `Google Drive API` e selecione-a.
3. Clique no botão **Ativar** (Enable).

## Passo 3: Criar Credenciais (Service Account)

Essa será a "identidade" do nosso bot:

1. No menu lateral, acesse **APIs e Serviços** > **Credenciais**.
2. Clique em **+ CRIAR CREDENCIAIS** (Create Credentials) no topo e selecione **Conta de serviço** (Service account).
3. Insira um nome da conta de serviço (ex: `pm-agent`) e uma descrição. Clique em **Criar e Continuar**.
4. Na etapa de Papéis (Roles), não é estritamente necessário dar papéis gerais no projeto para acessar o Drive, pois o acesso é por documento, mas você pode deixar em branco e clicar em **Concluir** (Done).
5. De volta à tela de Credenciais, localize a conta de serviço que você acabou de criar lá embaixo e clique nela.
6. Vá na aba **Chaves** (Keys).
7. Clique em **Adicionar chave** (Add Key) > **Criar nova chave** (Create new key).
8. Selecione o formato **JSON** e clique em **Criar**.
9. Um arquivo `.json` será baixado para o seu computador. 

## Passo 4: Configurar no Projeto

1. Renomeie o arquivo JSON baixado para `credentials.json`.
2. Mova o arquivo para a raiz do seu projeto `adk-agent` (ou para uma pasta segura que não seja versionada pelo Git).
3. No arquivo `.env` da raiz do projeto, garanta que existe o caminho para a sua credencial:

```env
GOOGLE_APPLICATION_CREDENTIALS=credentials.json
```

## Passo 5: Como compartilhar pastas com o Agente

A Conta de Serviço é como um "novo usuário" sem e-mail do Gmail, que tem o seu próprio Drive isolado (neste caso, o email da service account parece com `pm-agent@project-id.iam.gserviceaccount.com`). 
Para que o agente consiga visualizar os PRDs do seu curso, você deve:

1. Abrir a pasta ou arquivo no seu Google Drive pessoal.
2. Clicar em **Compartilhar**.
3. Inserir o **e-mail da conta de serviço** (`pm-agent@...`) e garantir o nível de permissão necessário (Leitor ou Editor).

Pronto! Agora o nosso módulo (`google-api-python-client`) saberá como autenticar automaticamente sem intervenção humana.
