def Divide_Lines(filename):
    file = open(filename, "r")
    lines = file.readlines()

    read_lines = []

    for i in lines:
        cur_div = ""

        for e in i:
            if e != ";":
                cur_div += e
            else:
                read_lines.append(cur_div)
                cur_div = ""

            

class Lexer:
    def __init__(self):
        pass