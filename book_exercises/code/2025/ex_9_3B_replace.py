# Open the file for reading and writing

# Word I want to replace if it occurs in the last line:
old_word = "banana"

with open("samples/sample_svg_file.txt", "r+", encoding="utf-8") as f:
    # Read the text-data
    my_lines = f.readlines()
    # Adapt the text
    for i, line in enumerate(my_lines):
        "banana"
        if  line =
            my = my_text.replace("banana", "orange")
    # Overwrite a the adapted text to the old file content
    f.write("This and the next part will be appended to the original:\n")
    f.write(my_text)
