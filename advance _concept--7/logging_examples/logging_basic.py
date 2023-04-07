import logging

"""
logging have 5 levels
# debug- 10 -> detail information, traceback,input output, statements that could helps us in debugging the issue

#info - 20-> any information 

#warning - 30-> an indication that something is working now but can break in future.

#error - 40 -> any error which we face

# critical - 50 -> any critical information, system failure, data full, 
"""
# use number or logging.<level name in capital>
# logging default level is warning i.e 30 and if we use level 30 then it is implemented with 40 and 50 but 10, 20 not implemented
# and if we use 20 then 30,40,50 also use but 10 not use i.e uppper level is use

logging.basicConfig(level=logging.DEBUG, filename="basic.log", format="%(asctime)s -> %(levelname)s -> %(message)s -> %(lineno)d -> %(funcName)s" )

class OutputWillBeZero(Exception):
    pass

def addtion(a,b):
    logging.info("Addition called")
    return a+b

def subtraction(a,b):
    logging.info("Subtraction called")
    return a-b

def multiplication(a,b):
    logging.info("Multiplication called")
    if a==0 or b==0:
        logging.debug("one of the input was zero")
        raise OutputWillBeZero("one or both the argument is zero hence result will be zero, which of no use")
    logging.info("Multiplication Success")
    return a*b

def division(a,b):
    logging.info("Division called")
    try:
        return a/b
    except Exception as e:
        logging.error(f"{e}")
        pass

addtion(10,20)
multiplication(2,10)
subtraction(50,43)
division(45,6)
division(56,0)


addtion(10,20)
try:
    multiplication(2,0)
except OutputWillBeZero:
    pass
subtraction(50,43)
division(45,6)
division(56,0)





















# print(f"Add called with input 1 and 2 and result is {addtion(1,2)}")
# print(f"Subtration called with input 1 and 2 and result is {subtraction(1,2)}")
# print(f"Multiplication called with input 1 and 2 and result is {multiplication(1,2)}")
# print(f"Division called with input 1 and 2 and result is {division(1,2)}")
#
#
# logging.warning(f"Add called with input 1 and 2 and result is {addtion(1,2)}")
# logging.warning(f"Subtration called with input 1 and 2 and result is {subtraction(1,2)}")
# logging.warning(f"Multiplication called with input 1 and 2 and result is {multiplication(1,2)}")
# logging.warning(f"Division called with input 1 and 2 and result is {division(1,2)}")