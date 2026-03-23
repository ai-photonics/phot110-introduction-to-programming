# Import os for testing
import os


def convert_text(file_path, file_path_new):
    """
    Adapts a text in a file to be conform (with certain format).

    Opens a text file, adapts the text to be
    upper-case and removes `!` symbols.

    :param file_path: file path of original text
    :param file_path_new: file path of adapted text
    :returns: None
    """
    with open(file_path) as f:
        text = f.read()

    text = text.upper()
    text = text.replace("!", "")

    with open(file_path_new, "w+") as f:
        f.write(text)


def text_to_html_page(file_path, title):
    """ Makes a valid html page from text in a file """
    with open(file_path, "r") as f:
        text = f.read()
        html_text = """<!doctype html>
<html lang=en>
    <head>
        <meta charset=utf-8>
        <title>""" + title + """</title>
    </head>
    <body>
        <p>""" + text + """</p>
    </body>
</html>
    """
    return html_text


# Performing tests on the module functions within separate test functions
def test_convert_text():
    folder_name = "."
    file_name = "sample.txt"
    file_name_new = "sample_new.txt"
    file_path = os.path.join(folder_name, file_name)
    file_path_new = os.path.join(folder_name, file_name_new)
    convert_text(file_path, file_path_new)


def test_text_to_html():
    folder_name = "."
    file_name = "sample.txt"
    file_name_html = "sample.html"
    file_path = os.path.join(folder_name, file_name)
    file_path_html = os.path.join(folder_name, file_name_html)
    html = text_to_html_page(file_path, file_name)
    with open(file_path_html, "w") as f:
        f.write(html)


# Perform the tests
if __name__ == "__main__":
    test_convert_text()
    test_text_to_html()
