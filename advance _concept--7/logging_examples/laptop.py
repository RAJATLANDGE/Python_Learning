import logging
from loggers import function_logger

# logging.basicConfig(level=logging.INFO, filename="lap.log", format="%(levelname)s -> %(message)s -> %(lineno)d" )

lap_logger = function_logger(__name__, "lap.log","%(asctime)s ->%(levelname)s -> %(message)s -> %(lineno)d",10)

class Laptop:

    def __init__(self,id,brand,ram):
        self.id = id
        self.brand = brand
        self.ram = ram
        lap_logger.info(f"laptop crated with id: {id}, brand: {brand}")

l1 = Laptop(1,"Dell", 512)













