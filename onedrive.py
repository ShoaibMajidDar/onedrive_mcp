import httpx
import io
import PyPDF2

MS_GRAPH_BASE_URL = 'https://graph.microsoft.com/v1.0'

class OneDriveClient:
    def __init__(self, access_token):
        self.base_url = 'https://graph.microsoft.com/v1.0'
        self.headers = {'Authorization': 'Bearer ' + access_token}
                
    def get_file(self, file_id) -> str:
        url = f'{MS_GRAPH_BASE_URL}/me/drive/items/{file_id}/content'
        response = httpx.get(url, headers=self.headers)

        if response.status_code == 302:
            location = response.headers['location']
            file_data = httpx.get(location)
            
            # Check if the content type is PDF
            content_type = file_data.headers.get('content-type', '')
            if 'application/pdf' not in content_type.lower():
                raise ValueError('File is not a PDF document')

            pdf_file = io.BytesIO(file_data.content)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            return text
        else:
            raise Exception(f'SomeThing went wrong. {response.status_code=}')
