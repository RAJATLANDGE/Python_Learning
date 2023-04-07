"""
1)module level information\ documentation
"""

# 2)function--3 madhe docstring
def function():
    """
    what does the function--3 do
    :return: explain what function--3 can return
    """

def function2(n1, n2):
    """
    this function--3 took two parameter as input and process it.
    :param n1:first input for processing
    :param n2:second input for processing
    :return: processing results
    """

print(function2.__doc__)


# 3) docstring in class
class Test:
    """

    """
    def method1(self):
        """

        :return:
        """