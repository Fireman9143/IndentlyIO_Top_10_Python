import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict

def check_status(url:str) -> None:
    """Uses requests library to get information from website"""
    try:
        response:Response = requests.get(url)

        #Information
        status_code:int = response.status_code
        headers:CaseInsensitiveDict[str] = response.headers
        content_type:str = headers.get('Content-Type', 'Unknown')
        server:str = headers.get('Server', 'Unknown')
        response_time:float = response.elapsed.total_seconds()

        print(f'URL: {url}')
        print(f'Status Code: {status_code}')
        print(f'Content Type: {content_type}')
        print(f'Server: {server}')
        print(f'Response Time: {response_time:.2f} seconds')
    except RequestException as e:
        print(f"Error: {e}")


def main():
     """Uses check_status function to get information from list of websites"""
     url_to_check:list = ['https://www.indently.io', 
                          'https://www.apple.com', 
                          'https://www.facebook.com', 
                          'https://www.google.com', 
                          'https://www.python.org',
                          'https://www.google.io']
     for url in url_to_check:
         check_status(url)
         print()

     
if __name__ == "__main__":
    main()