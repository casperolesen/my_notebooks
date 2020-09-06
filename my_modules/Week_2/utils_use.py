import utils

# files_in_folder
utils.files_in_folder(path = r"C:\Users\Casper\datamatiker\python_cko\docker_notebooks\notebooks\my_notebooks", output_file = 'output_file.txt')

# files_in_folder_rec
utils.files_in_folder_rec(path=r"C:\Users\Casper\datamatiker\python_cko\docker_notebooks\notebooks\my_notebooks")

# first_line_in_files
files = utils.files_in_folder(path=r"C:\Users\Casper\datamatiker\python_cko\docker_notebooks\notebooks\my_notebooks\downloads", output_file=None)
utils.first_line_in_files(files=files)

# find_emails_in_files
utils.find_emails_in_files(files=files)

# find_headlines_in_md_files
utils.find_headlines_in_md_files(files=files)