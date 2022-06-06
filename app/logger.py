import logging
logging.basicConfig(filename='logs/api.log', filemode='w', level=logging.DEBUG)

def create_logger():
    logger = logging.getLogger('basic')
    logger.setLevel('DEBUG')
    
    file_handler = logging.FileHandler('logs/api.log')
    logger.addHandler(file_handler)
    
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(mesage)s')
    file_handler.setFormatter(formatter)
    
    return logger