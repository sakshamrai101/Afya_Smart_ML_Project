def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def add_content(file_path, additional_content):
    with open(file_path, "a") as file:
        file.write("\n" + additional_content)

def write_file(file_path, file_content):
    with open(file_path, "w") as file:
        file.write(file_content)
    