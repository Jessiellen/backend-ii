import logging

logging.basicConfig(
    level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s', 
    filename='app.log',  
    filemode='w'  
)
logging.debug("Mensagem de DEBUG")
logging.info("Mensagem de INFO")
logging.warning("Mensagem de WARNING")
logging.error("Mensagem de ERROR")

