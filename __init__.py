__author__ = "Zedikon"
__copyright__ = "Copyright zedikon 2022, all rights reserved."
__version__ = "1.0.23"
__emal__ = "mrzedikon@gmail.com"


stack = []

tokens = {
    "meaning": ":",
    "string": "str:",
    "integer": "int:",
    "eval": "do:",
    "next": ";"
}

def load(variable):
    try:
        stack.append(variable)
        strstack = tokens["next"].join(stack)
        global result
        result = strstack.split()
    except Exception:
        return f"PECF: Sorry, but i can't find {variable} variable"

def decode(name):
    try:
        positions = result.index(name + ":")
    except Exception:
        return f"PECF: Sorry, but i can't find {name} variable"
    try:
        if result[positions + 1] == tokens["string"]:
            res = str(result[positions + 2])
            return res
        if result[positions + 1] == tokens["integer"]:
            res = int(result[positions + 2])
            return res
        if result[positions + 1] == tokens["eval"]:
            res = eval(result[positions + 2])
            return res
        else:
            return result[positions + 1]
    except Exception:
        return result[positions + 2]