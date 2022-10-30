from compiler import *

file = open("main.mpy", "r")

print(Lexer(file))