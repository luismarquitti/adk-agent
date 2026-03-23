# Configuração do GitHub Personal Access Token (PAT)

Para que o nosso agente do Módulo 2 consiga manipular issues no repositório, precisamos fornecer uma credencial segura: um **Personal Access Token**.

## Passo a passo para criar o Token:

1. Acesse o [GitHub](https://github.com/) e faça login em sua conta.
2. No canto superior direito, clique na sua foto de perfil e vá em **Settings** (Configurações).
3. No menu lateral esquerdo, role até o final e clique em **Developer Settings**.
4. No painel esquerdo, expanda **Personal access tokens** e selecione **Tokens (classic)** (recomendado por simplicidade, embora o *Fine-grained* também funcione).
5. Clique no botão **Generate new token** -> **Generate new token (classic)**.
6. Dê um nome para o token, por exemplo: `ADK-Course-Module-2-Agent`.
7. Configure a expiração (`Expiration`) conforme desejar (recomendado 30 dias para evitar problemas de segurança).
8. Na lista de permissões (Scopes), marque a caixa principal **`repo`**. Isso garante que o agente consiga ler os repositórios, criar e modificar issues.
9. Desça até o fim da tela e clique em **Generate token**.

> [!WARNING]
> **Atenção!** O GitHub mostrará o seu token apenas UMA vez após gerar. Copie a string e salve em um local seguro.

## Configurando o projeto

Crie um arquivo `.env` na raiz do seu projeto caso ainda não exista, e adicione o seu token e o nome do repositório de teste:


GITHUB_TOKEN=ghp_seu_token_aqui_xxxxxx
GITHUB_REPO=seu_usuario/nome_do_repositorio_de_teste


Pronto! Agora o nosso módulo de integração com GitHub (`PyGithub`) conseguirá ler essas credenciais.
