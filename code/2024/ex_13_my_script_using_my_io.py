# This script shows functionality of the lecture_13_ex_my_io module.
#
# The lecture_13_ex_my_io module contains functions to manipulate
# text-files. The name of the module is a bit complex, "my_io" would
# be a more logical choice, but for our course we add the lecture info.

# Import our module
import lecture_13_ex_my_io as my_io
# Import os for the file path name
import os

folder_name = "."
file_name = "sample.txt"
file_name_new = "sample_new.txt"
file_name_html = "sample_new.html"
file_path = os.path.join(folder_name, file_name)
file_path_new = os.path.join(folder_name, file_name_new)
file_path_html = os.path.join(folder_name, file_name_html)

# First make the file contain all upper-case text without "!" symbols
my_io.convert_text(file_path, file_path_new)
# Then load the new file and convert the text to an html page
html_text = my_io.text_to_html_page(file_path_new, file_name_html)
# Save the html page
with open(file_path_html, "w+") as f:
    f.write(html_text)

