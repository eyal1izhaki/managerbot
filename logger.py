import logging

# Setting logger up
logger = logging.getLogger("botmanager")
logger.setLevel(logging.INFO)
logging_handler = logging.StreamHandler()
logging_handler.setLevel(logging.INFO)    
formatter = logging.Formatter("[%(name)s] [%(levelname)s] [%(asctime)s] - %(message)s")
logging_handler.setFormatter(formatter)
logger.addHandler(logging_handler)