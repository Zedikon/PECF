__author__ = "Zedikon"
__copyright__ = "Copyright zedikon 2022, all rights reserved."
__version__ = "1.03.22"
__emal__ = "mrzedikon@gmail.com"


stack = []

tokens = {
    "meaning": ":"
}

def decode(x, name):
    stack.append(x)
    strstack = ','.join(stack)
    try:
        result = strstack.split(name + tokens["meaning"])
        return result[1]
    except Exception:
        return "PECF: Sorry, but i can't find this variable."