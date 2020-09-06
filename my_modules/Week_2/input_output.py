import argparse
import os
import csv
from pathlib import Path

def print_file_content(**kwargs):
    localfile = kwargs['file']

    with open(localfile) as file_object:
        contents = file_object.read()
        print(contents)

def write_list_to_file(**kwargs):
    output_file = kwargs['output_file']
    lst = kwargs['lst']

    #file_check = os.getcwd()
    #print(file_check)

    #newfile = Path(Path.cwd() / 'docker_notebooks' / 'notebooks' / 'my_notebooks' / 'downloads' / output_file)
    #file_check = Path(Path.cwd() / 'docker_notebooks' / 'notebooks' / 'my_notebooks' / 'downloads' / lst)
    content = None
    
    if isinstance(lst, list):
        content = lst
    else:
        with open(lst) as file_object:
            content = file_object.readlines()

    with open(output_file, 'w') as file_object:
        [file_object.write(((item.replace("\n", "")).replace(" ", "")) + "\n") for item in content if item.strip()]
    
    print("File saved!")

def read_file(**kwargs):
    csv_list = []
    input_file = kwargs['input_file']
    #filename = './downloads/' + input_file
    with open(input_file) as f:
        reader = csv.reader(f)
        #header_row = next(reader)

        for row in reader:
            csv_list.append(row)
    
    print(csv_list)

if __name__ == "__main__":
    # top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # print_file_content parser
    parser_print_file_content = subparsers.add_parser('print_file_content')
    parser_print_file_content.add_argument(
        '-file', default=r"C:\Users\Casper\datamatiker\python_cko\docker_notebooks\notebooks\my_notebooks\downloads\pi_30_digits.txt")
    parser_print_file_content.set_defaults(func=print_file_content)

    # write_list_to_file parser
    parser_write_list_to_file = subparsers.add_parser('write_list_to_file')
    parser_write_list_to_file.add_argument(
        '-output_file', default=r"C:\Users\Casper\datamatiker\python_cko\docker_notebooks\notebooks\my_notebooks\downloads\list_to_file.txt")
    parser_write_list_to_file.add_argument('-lst', default=['a','b','c','d','e'])
    parser_write_list_to_file.set_defaults(func=write_list_to_file)

    # read_file parser
    parser_read_file = subparsers.add_parser('read_file')
    parser_read_file.add_argument('-input_file', default=r"C:\Users\Casper\datamatiker\python_cko\docker_notebooks\notebooks\my_notebooks\downloads\100 Sales Records.csv")
    parser_read_file.set_defaults(func=read_file)

    # call function in sub-command parser
    args = parser.parse_args()
    args.func(**vars(args))