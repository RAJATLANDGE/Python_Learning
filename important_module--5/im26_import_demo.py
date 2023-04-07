# type 1 --- direct file import
import json
#
# # import json
# # import os
import sys
# import datetime
#
# # type 2
#
# from datatypes--1 import string_introduction
#
#
# # type 3 --- import as key name
# import datetime as dt          # later datetime use as dt  this will creat shortcut for long name
# from datetime import datetime as dte

# in api communication is in json data
# --in jason values only dictionary, list,array, number,null, string and boolean are callebale, tuple and set give error

data = {"name": "first"}
print(json.dumps(data))                  # conversion of dictionary to jason

data_2 = '{"data": "test"}'         #in json single inverted comma is not use
print(json.loads(data_2))           # conversion of sting to dictionary type data

print(sys.path)