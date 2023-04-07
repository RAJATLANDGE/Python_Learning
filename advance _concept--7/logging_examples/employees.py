import logging
from loggers import function_logger
from laptop import Laptop

# logging.basicConfig(level=logging.DEBUG, filename="emplo.log", format="%(asctime)s -> %(levelname)s -> %(message)s -> %(lineno)d -> %(funcName)s" )
emp_logger = function_logger(__name__,"employee.log", "%(asctime)s -> %(levelname)s -> %(message)s -> %(lineno)d -> %(funcName)s", 10)

class Employee:

    def __init__(self,id, name, city):
        self.id = id
        self.name = name
        self.city = city
        emp_logger.info(f"Employee created with id: {id}, name: {name}")


e1 = Employee(1, "Saurabh", "Nagpur")
l2 = Laptop(2,"Sony","1024")















