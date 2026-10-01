from qjrcc import QJRCC
from qjrcc.runtime import Runtime

with open("examples/main.c") as file:
    code = file.read()

compiler = QJRCC()

ast = compiler.compile(code)

runtime = Runtime()
runtime.execute(ast)

print(ast)