import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)

handler = TimedRotatingFileHandler("app_rotating.log", when="midnight", interval=1, backupCount=7)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("Mensagem de DEBUG")
logger.info("Mensagem de INFO")
logger.warning("Mensagem de WARNING")
logger.error("Mensagem de ERROR")
