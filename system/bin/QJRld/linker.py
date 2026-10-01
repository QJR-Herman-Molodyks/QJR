
def QJRld_link(file1, file2, linked_filename):
    linked_content = ""

    with open(file1, "r") as f:
        linked_content = f.read()

    with open(file2, "r") as f:
        linked_content += f.read()

    if file1.endswith(".qjro") and file2.endswith(".qjro"):
        with open(f"{linked_filename}", "w") as f:
            f.write(f"{linked_content}\nFF")

    else:
        with open(f"{linked_filename}", "w") as f:
            f.write(linked_content)

if __name__ == "__main__":
    QJRld_link("test.qjro", "test1.qjro", "test2.qjrexc")