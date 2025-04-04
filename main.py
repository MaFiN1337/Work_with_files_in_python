from app.io.input import *
from app.io.output import *

def main():
    user_data = input_func()
    output_func(user_data)
    write_to_file("data/interesting_info_to_write.txt", user_data)
    file_data = read_with_pandas("data/interesting_info_to_read.txt")
    output_func(file_data)
    write_to_file("data/interesting_info_to_write_2.txt", file_data)


if __name__ == '__main__':
    main()