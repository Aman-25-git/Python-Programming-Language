#NameValidation.py<---Module Name
from NameExcept import SpaceError,ZeroNameLengthError,InValidNameError
def validate_name(name):
    if (name.isspace()):
        raise SpaceError
    else:
        words = name.split()  # [GUIDO,VAN,ROSUMM]
        if (len(words) == 0):
            raise ZeroNameLengthError
        else:
            res = True
            for word in words:
                if (not word.isalpha()):
                    res = False
                    break
            if (res):
                return " ".join(words)
            else:
                raise InValidNameError