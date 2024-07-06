# The script can delete itself after execution:
import os

def self_destruct():
    os.remove(__file__)

import os

def self_destruct():
    try:
        os.remove(__file__)
        print("File successfully deleted.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    self_destruct()
