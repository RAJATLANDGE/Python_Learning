import logging

def function_logger(log_name, filename, format, level):


    logger = logging.getLogger(log_name)
    logger.setLevel(level)                                                              # logging.IMFO
    formatter = logging.Formatter(format)
    filehandler = logging.FileHandler(filename)
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    return logger



