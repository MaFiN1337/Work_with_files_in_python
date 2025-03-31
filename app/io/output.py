import os
from collections.abc import Iterable

def output_func(output_info):
    """
    Args:
    output_info (Any): output information you want to get in console
    Returns:
        None
    Examples:
        >>> output_func(5)
        Your information was the following:
        5
        >>> output_func(None)
        Your information was the following:
        None
        >>> output_func(["first object", "second object", 3, True])
        Your information was the following:
        first object
        second object
        3
        True
    """
    print("Your information was the following:")
    if isinstance(output_info, Iterable):
        for item in output_info:
            print(item)
    else:
        print(output_info)
    return None

def write_to_file(file_name, info):
    """
    Args:
        file_name (str): output file you want to write in
        info (Any): output information you want to write in file
    Returns:
        None
    Raises:
        FileNotFoundError: if the file doesn't exist or path is invalid
        KeyboardInterrupt: if something like ctrl + c was entered when asking for confirmation
    """
    if os.path.exists(file_name):
        confirmation = input(f"File {file_name} already exists. Do you want to overwrite it? (y/n): ")
        if confirmation.strip().lower() == "n":
            print("Terminating...")
            return None
    with open(file_name, "w") as f:
        if isinstance(info, Iterable):
            for item in info:
                f.write(item+"\n")
        else:
            f.write(info)
    return None

write_to_file("../../interesting_info_to_read", ["This will be my first line", "And this will be second"])