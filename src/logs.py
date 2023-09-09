import logging


def logs(error=None, info=None):
    """Функция для записи логов в файл logfile.log"""
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('../logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    if info:
        logger.info(f'Information message: {info}')
    elif error:
        logger.error(f'Error message: {error}')
