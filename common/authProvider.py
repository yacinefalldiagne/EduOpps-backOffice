from dotenv import load_dotenv
import os

load_dotenv()


endpoint = os.getenv('endpoint')



def add_token_to_request(request):
    global token
    if token:
        request.headers['Authorization'] = f'Bearer {token}'
    return request
