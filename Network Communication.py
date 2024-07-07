# Send logs or status updates to a remote server for monitoring:
import requests

def send_log_to_server(log):
    url = "http://your-server.com/log"
    payload = {"log": log}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        logging.error(f"Error sending log: {e}")

send_log_to_server("Encryption completed")
