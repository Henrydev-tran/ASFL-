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

    file.close()

    return read_lines

def Run_Test():
    sample1_test = Divide_Lines("./versions/1.0.0/tests/samples/sample1.mpy")
    if sample1_test == ['var:int m0001 = 0', 'var:bool m0002 = false', ' var:float m0003 = 0f', ' var:string m0004 = "Hello, World!"']:
        print("Sample 1 test success")
    else:
        print("Sample 1 test failure")


Run_Test()