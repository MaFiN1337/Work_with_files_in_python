import pandas as pd

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

def read_with_pandas(file_name):
    """
    Args:
        file_name(str): name of the file to read
    Returns:
        list[str]: list of strings representing the lines of the file
    Raises:
        FileNotFoundError: if the file does not exist or the path is entered incorrectly
        ValueError: if the file format is not .txt
    Examples:
        >>> print(read_with_pandas("csv_file.csv"))
        ValueError
    """
    if file_name.endswith(".txt"):
        df = pd.read_csv(file_name, header=None)
        return df[0].astype(str).tolist()
    raise ValueError("Unsupported file format")
