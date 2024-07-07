import logging
logging.basicConfig(
    filename='hidden_log.log',       # Log messages will be written to this file
    level=logging.INFO,              # Set the logging level to INFO
    format='%(asctime)s %(message)s' # Define the log message format to include timestamp and message
)
logging.info('This is a log message.')
with open('hidden_log.log', 'r') as file:
    content = file.read()
    print(content)


import logging
import os

# Determine the appropriate log file path
log_filename = 'hidden_log.log'
log_filepath = os.path.join(os.getcwd(), log_filename)

logging.basicConfig(
    filename=log_filepath, 
    level=logging.INFO, 
    format='%(asctime)s %(message)s'
)

logging.info('This is a log message.')
