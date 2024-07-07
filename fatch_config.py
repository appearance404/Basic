import requests

def fetch_config():
    url = "http://your-server.com/config"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        logging.error(f"Error fetching config: {e}")
        return None

config = fetch_config()
if config:
    key = config.get('encryption_key', b'default_key_123456')
else:
    key = b'default_key_123456'
