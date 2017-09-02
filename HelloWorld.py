"""This is the doc string"""
def hello():
    """This is your typical first program.

    It has a minor twist.
    """
    print("hello world " * 3)

def fib(limit):
    """Return a list containing the Fibonacci series up to limit."""
    result = []
    var_a, var_b = 0, 1
    while var_a < limit:
        result.append(var_a)
        var_a, var_b = var_b, var_a+var_b
    return result

hello()
print(hello.__doc__)

FIBRES = fib(100)   # call fib
print(FIBRES)
