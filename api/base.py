import requests
import urllib3

def get_request(url, timeout=1000):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        response = requests.get(url, timeout=timeout, verify=False) 
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return ""