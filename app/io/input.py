def input_func():
    """
    Returns:
        list[Any]: list of any values our user had input
    Raises:
        KeyboardInterrupt: something like ctrl + c can raise KeyboardInterrupt
    """
    user = []
    repeat = True
    while repeat:
        user_input = input("Enter something: ")
        user.append(user_input)
        want_to_repeat = input("Do you want to repeat? (y/n): ")
        repeat = False if want_to_repeat.strip().lower() == "n" else True
    return user

def read_from_file(file_name):
    """
    Args:
        file_name(str): name of the file to read
    Returns:
        list[str]: list of strings representing the lines of the file
    Raises:
        FileNotFoundError: if the file does not exist or the path is entered incorrectly
    """

    with open(file_name, "r") as f:
        result = f.readlines()
    return result

def read_with_pandas():
    pass

print(read_from_file("../../interesting_info_to_read"))