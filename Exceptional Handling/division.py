#division <---Module name
from Divexcept import AmanZeroError
def division(a,b):
    if (b == 0):
        raise AmanZeroError
    else:
        return a/b