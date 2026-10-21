import sys

from . import compile
from . import error
from . import interpreter

def QJRcc_compile(filename, compilation_flag, compiled_filename):
    QJRCCompiler = compile.QJRCCompiler()

    if compilation_flag == "-o":
        QJRCCompiler.compile_file(filename, compiled_filename)
    else:
        QJRcc_error(f"Unknown compilation flag -> {compilation_flag}")


def QJRcc_interpreter(filename):
    interpreter.QJRInterpreter().run_file(filename)

def QJRcc_error(message):
    error.QJRCCError(message)

# Testing
# if __name__ == "__init__":
#     QJRcc_error("QJRcc COMPILATION ERROR (test)")