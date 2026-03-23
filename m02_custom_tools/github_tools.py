import os
import base64
from github import Github
from github.GithubException import GithubException

def get_github_client() -> Github:
    """Helper function to initialize the GitHub client."""
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("A variável de ambiente GITHUB_TOKEN não está configurada.")
    return Github(token)

def get_repo_name() -> str:
    """Helper function to get the target repository name."""
    repo = os.environ.get("GITHUB_REPO")
    if not repo:
        raise ValueError("A variável de ambiente GITHUB_REPO não está configurada. Ex: usuario/repo")
    return repo

def create_issue(title: str, body: str, labels: list = None) -> str:
    """
    Cria uma nova issue no repositório GitHub configurado.
    
    Args:
        title (str): O título da issue.
        body (str): A descrição detalhada da issue.
        labels (list[str], optional): Lista de labels para a issue (ex: ['bug', 'enhancement']). Defaults to None.
        
    Returns:
        str: Uma mensagem de sucesso com a URL da issue criada ou mensagem de erro.
    """
    try:
        g = get_github_client()
        repo_name = get_repo_name()
        repo = g.get_repo(repo_name)
        
        issue = repo.create_issue(
            title=title,
            body=body,
            labels=labels or []
        )
        return f"Issue criada com sucesso! URL: {issue.html_url}"
    except GithubException as e:
        return f"Erro na API do GitHub ao criar issue: {e.data.get('message', str(e))}"
    except Exception as e:
        return f"Erro inesperado ao criar issue: {str(e)}"

def list_open_issues() -> str:
    """
    Lista todas as issues abertas no repositório configurado.
    
    Returns:
        str: Um texto formatado contendo o número, título e URL das issues em aberto.
    """
    try:
        g = get_github_client()
        repo_name = get_repo_name()
        repo = g.get_repo(repo_name)
        
        open_issues = repo.get_issues(state='open')
        result_lines = [f"Issues abertas em {repo_name}:"]
        
        for issue in open_issues:
            # get_issues also returns pull requests by default in PyGithub if not filtered
            if not issue.pull_request:
                result_lines.append(f"#{issue.number} - {issue.title} ({issue.html_url})")
                
        if len(result_lines) == 1:
            return "Nenhuma issue aberta encontrada."
            
        return "\n".join(result_lines)
    except GithubException as e:
        return f"Erro na API do GitHub ao listar issues: {e.data.get('message', str(e))}"
    except Exception as e:
        return f"Erro inesperado ao listar issues: {str(e)}"

def update_issue_comment(issue_number: int, comment: str) -> str:
    """
    Adiciona um comentário em uma issue existente.
    
    Args:
        issue_number (int): O número da issue (ex: 1, 2, 3).
        comment (str): O comentário a ser adicionado.
        
    Returns:
        str: Mensagem de sucesso ou erro.
    """
    try:
        g = get_github_client()
        repo_name = get_repo_name()
        repo = g.get_repo(repo_name)
        
        issue = repo.get_issue(number=issue_number)
        issue.create_comment(comment)
        return f"Comentário adicionado com sucesso na issue #{issue_number}."
    except GithubException as e:
        return f"Erro na API do GitHub ao comentar na issue: {e.data.get('message', str(e))}"
    except Exception as e:
        return f"Erro inesperado: {str(e)}"

def list_github_files(directory_path: str = "") -> str:
    """
    Lista os arquivos e pastas em um diretório específico do repositório GitHub.
    
    Args:
        directory_path (str, optional): O caminho do diretório (ex: 'src' ou vazio para a raiz). Defaults to "".
        
    Returns:
        str: Uma lista formatada de arquivos e subdiretórios encontrados.
    """
    try:
        repo = get_github_client().get_repo(get_repo_name())
        contents = repo.get_contents(directory_path)
        
        # Se for apenas um arquivo retornado, converte para lista
        if not isinstance(contents, list):
            contents = [contents]
            
        result = [f"Conteúdo do diretório '/{directory_path or 'raiz'}':"]
        for item in contents:
            type_icon = "📁" if item.type == 'dir' else "📄"
            result.append(f"{type_icon} {item.path}")
            
        return "\n".join(result)
    except GithubException as e:
        return f"Erro na API do GitHub ao listar arquivos: {e.data.get('message', str(e))}"
    except Exception as e:
        return f"Erro inesperado ao listar arquivos no GitHub: {str(e)}"

def read_github_file(file_path: str) -> str:
    """
    Lê o conteúdo em texto de um arquivo específico do repositório GitHub.
    
    Args:
        file_path (str): O caminho completo do arquivo (ex: 'src/main.py' ou 'README.md').
        
    Returns:
        str: O conteúdo do arquivo ou mensagem de erro.
    """
    try:
        repo = get_github_client().get_repo(get_repo_name())
        file_item = repo.get_contents(file_path)
        
        if isinstance(file_item, list):
            return "O caminho informado é um diretório, não um arquivo. Use a ferramenta 'list_github_files'."
            
        content = base64.b64decode(file_item.content).decode('utf-8')
        return f"Conteúdo de '{file_path}':\n\n{content}"
    except GithubException as e:
        return f"Erro na API do GitHub ao tentar ler o arquivo: {e.data.get('message', str(e))}"
    except Exception as e:
        return f"Erro inesperado ao ler arquivo no GitHub: {str(e)}"
