"""This is the doc string"""
def hello():
    """This is your typical first program.

    It has a minor twist.
    """
    print("hello world " * 3)

hello()
print(hello.__doc__)
