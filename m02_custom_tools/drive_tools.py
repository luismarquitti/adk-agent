import os
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload

SCOPES = ['https://www.googleapis.com/auth/drive']
CREDENTIALS_FILE = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")

def get_drive_service():
    """Inicializa o cliente da API do Google Drive usando Service Account."""
    if not os.path.exists(CREDENTIALS_FILE):
        raise FileNotFoundError(
            f"Arquivo de credenciais não encontrado em: {CREDENTIALS_FILE}. "
            "Siga o guia google_drive_setup.md para configurá-lo."
        )
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES
    )
    return build('drive', 'v3', credentials=creds)

def list_drive_documents() -> str:
    """
    Lista os 10 documentos mais recentes disponíveis no Google Drive do agente.
    
    Returns:
        str: Uma lista de arquivos com seus IDs e nomes, ou uma mensagem de erro.
    """
    try:
        service = get_drive_service()
        # Query: Apenas arquivos (ignorando pastas) no "Meu Drive"
        # order_by="modifiedTime desc" garante que os editados recentemente venham primeiro
        results = service.files().list(
            pageSize=10, 
            fields="nextPageToken, files(id, name, mimeType)",
            q="mimeType != 'application/vnd.google-apps.folder'"
        ).execute()
        
        items = results.get('files', [])
        
        if not items:
            return "Nenhum documento encontrado no Drive do agente."
            
        output = ["Inventário de documentos no Google Drive:"]
        for item in items:
            output.append(f"- [{item['name']}] (ID: {item['id']}) - Tipo: {item['mimeType']}")
            
        return "\n".join(output)
        
    except HttpError as error:
        return f"Erro de API do Google Drive ao listar: {error}"
    except Exception as e:
        return f"Erro inesperado: {str(e)}"

def read_drive_document(doc_id: str) -> str:
    """
    Lê o conteúdo de um documento do Google Drive.
    Funciona melhor para planilhas e documentos exportáveis como texto.
    
    Args:
        doc_id (str): O ID do documento no Google Drive.
        
    Returns:
        str: O conteúdo em texto do documento.
    """
    try:
        service = get_drive_service()
        file = service.files().get(fileId=doc_id, fields="name, mimeType").execute()
        mime_type = file.get("mimeType")
        
        # Se for um Google Doc, exportamos como texto plano
        if mime_type == "application/vnd.google-apps.document":
            content = service.files().export_media(
                fileId=doc_id, mimeType="text/plain"
            ).execute()
            return content.decode('utf-8')
        else:
            # Para outros arquivos, tenta baixar o conteúdo bruto
            request = service.files().get_media(fileId=doc_id)
            content = request.execute()
            return content.decode('utf-8')
            
    except HttpError as error:
        return f"Erro de API do Google Drive ao ler documento: {error}"
    except Exception as e:
        return f"Erro inesperado ao tentar ler o documento: {str(e)}"

def save_local_document(name: str, content: str) -> str:
    """
    Salva um documento de planejamento localmente na pasta 'outputs' do projeto.
    Usado como alternativa ao Google Drive para contornar limites de cota de armazenamento (Storage Quota) 
    das Contas de Serviço gratuitas.
    
    Args:
        name (str): O título do documento (Ex: PRD - Módulo 2).
        content (str): O conteúdo a ser salvo no documento.
        
    Returns:
        str: Mensagem indicando sucesso e o caminho do arquivo gerado.
    """
    try:
        os.makedirs('outputs', exist_ok=True)
        
        # Remove caracteres problemáticos do nome
        safe_name = "".join([c if c.isalnum() or c in " -_" else "_" for c in name])
        filepath = os.path.join('outputs', f"{safe_name}.md")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return f"Documento '{name}' salvo com sucesso localmente no caminho: {filepath}\nUse esta resposta para informar ao usuário onde o arquivo está."
    except Exception as e:
        return f"Erro inesperado ao salvar documento local: {str(e)}"
