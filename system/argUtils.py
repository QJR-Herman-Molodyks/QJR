
from QJRtools.QJRboolUtils import switch

def detect_2_args_with_scopes(conhost: str):
    for c in conhost:
        if c == " ":
            end_cmd = conhost.index(c)
            break

    rest = conhost[end_cmd:].strip()

    quote_index = []

    for index, char in enumerate(rest):
        if char == '"':
            quote_index.append(index)

    if len(quote_index) == 4:
        arg_1 = rest[quote_index[0]+1:quote_index[1]]
        arg_2 = rest[quote_index[2]+1:quote_index[3]]
    else:
        raise ValueError(f"Wrong usage! We have {len(quote_index)} double quotes instead of 4!!!")

    return [arg_1, arg_2]

def detect_1_arg_with_scopes(conhost: str):
    is_started = False
    arg = []
    for c in conhost:
        if c == '"' and not is_started:
            is_started = True
        elif c == '"' and is_started:
            break
        else:
            if is_started:
                arg.append(c)



    return "".join(arg)


# testing
#
# if __name__ == "__main__":
#     print(detect_2_args_with_scopes('move "something" "something"'))
#     print(detect_1_arg_with_scopes('move "something _" "something"'))