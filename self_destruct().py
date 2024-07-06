# The script can delete itself after execution:
import os

def self_destruct():
    os.remove(__file__)

