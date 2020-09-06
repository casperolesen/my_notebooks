import argparse
import os
from os.path import join, isfile, isdir, splitext


def files_in_folder(**kwargs):
    """
    Get or save a list of files from a folder

    :keyword path: Full path to the folder
    :keyword output_file: Name of file if you want to save the list (file_name.txt) 
    """

    path = kwargs['path']
    output_file = kwargs['output_file']
    dirs = os.listdir(path)  # all files and dirs in a path
    files = [join(path, file) for file in dirs if isfile(join(path, file))]

    if kwargs['output_file'] == None:
        return files
    else:
        output_path = join(path, r"downloads\{}".format(output_file))
        with open(output_path, 'w') as file_object:
            [file_object.write(file + "\n") for file in files]
        print("Done writing to file!")


def files_in_folder_rec(**kwargs):
    """
    Prints all files in main and subfolders

    :keyword path: Full path to the folder
    """

    path = kwargs['path']
    dirs = os.listdir(path)
    folders = []
    for x in dirs:
        if isdir(join(path, x)):
            if not x.startswith("."):
                folders.append(join(path, x))
            else:
                print("- " + x)  # hidden files
        else:
            print("- " + x)

    for folder in folders:
        print(folder)
        files_in_folder_rec(path=folder)


def first_line_in_files(**kwargs):
    """
    Prints first line of each file from a list of files

    :keyword files: A list of filepaths
    """

    files = kwargs['files']
    for file in files:
        if splitext(file)[1] == '.txt':  # only read .txt files
            with open(file) as file_object:
                print(file_object.readline().replace("\n", ""))


def find_emails_in_files(**kwargs):
    """
    Search a list of files and print all emails from each file

    :keyword files: A list of filepaths
    """

    files = kwargs['files']
    for file in files:
        if splitext(file)[1] == '.txt':  # only read .txt files
            with open(file) as file_object:
                for line in file_object:
                    if '@' in line:
                        print(line.replace("\n", ""))


def find_headlines_in_md_files(**kwargs):
    """
    Search a list of markdown-files and print each headlines

    :keyword files: A list of filepaths to .md files
    """

    files = kwargs['files']

    for file in files:
        if splitext(file)[1] == '.md':  # only read .md files
            with open(file) as file_object:
                for line in file_object:
                    if line.startswith('#'):
                        print(line.replace("\n", ""))


if __name__ == "__main__":
    # top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # files_in_folder parser
    parser_files_in_folder = subparsers.add_parser('files_in_folder')
    parser_files_in_folder.add_argument(
        '-path', default=r"C:\Users\Casper\datamatiker\python_cko\docker_notebooks\notebooks\my_notebooks")
    parser_files_in_folder.add_argument('-output_file', default=None)
    parser_files_in_folder.set_defaults(func=files_in_folder)

    # files_in_folder_rec parser
    parser_files_in_folder_rec = subparsers.add_parser('files_in_folder_rec')
    parser_files_in_folder_rec.add_argument(
        '-path', default=r"C:\Users\Casper\datamatiker\python_cko\docker_notebooks\notebooks\my_notebooks")
    parser_files_in_folder_rec.set_defaults(func=files_in_folder_rec)

    # first_line_in_files parser
    parser_first_line_in_files = subparsers.add_parser('first_line_in_files')
    parser_first_line_in_files.add_argument('-files', default=files_in_folder(
        path=r"C:\Users\Casper\datamatiker\python_cko\docker_notebooks\notebooks\my_notebooks\downloads", output_file=None))
    parser_first_line_in_files.set_defaults(func=first_line_in_files)

    # find_emails_in_files parser
    parser_find_emails_in_files = subparsers.add_parser('find_emails_in_files')
    parser_find_emails_in_files.add_argument('-files', default=files_in_folder(
        path=r"C:\Users\Casper\datamatiker\python_cko\docker_notebooks\notebooks\my_notebooks\downloads", output_file=None))
    parser_find_emails_in_files.set_defaults(func=find_emails_in_files)

    # find_headlines_in_md_files parser
    parser_find_headlines_in_md_files = subparsers.add_parser(
        'find_headlines_in_md_files')
    parser_find_headlines_in_md_files.add_argument('-files', default=files_in_folder(
        path=r"C:\Users\Casper\datamatiker\python_cko\docker_notebooks\notebooks\my_notebooks\downloads", output_file=None))
    parser_find_headlines_in_md_files.set_defaults(
        func=find_headlines_in_md_files)

    # call function in sub-command parser
    args = parser.parse_args()
    args.func(**vars(args))
