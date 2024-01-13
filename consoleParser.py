def parse(args, arg):
    for a in range(len(args)):
        if not args[a] == f"main.py" and args[a] == arg or str(args[a + 1]).startswith("-"):
            if a + 1 >= len(args):
                return True
            elif not str(args[a + 1]).startswith("-") and not args[a + 1] == None:
                return convertType(args[a + 1])
    return "nothing"


def convertType(s):
    if type(s) == str:
        return str(s)
    elif type(s) == int:
        return int(s)
    elif type(s) == bool:
        return bool(s)
