
from asm_interpreter import QJRassembly

QJRassembly = QJRassembly()
count = 0
print("Welcome to QJRas!")
while True:
    count = count + 1
    command = input(" >>> ")
    if command == "exit":
        break
    else:
        QJRassembly.exec_assembly(command, count)
