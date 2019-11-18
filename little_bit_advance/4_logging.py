import logging
logging.basicConfig(filename='example.log',level=logging.INFO)


logging.warning("This is warning.")
logging.debug("This is debug message.")
logging.info("This is info message.")
logging.error("This is error message.")
log = logging.getLogger("ModuleName")


log.info("log with error.")
log.critical("Critical message.")