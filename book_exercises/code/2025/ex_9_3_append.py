# Open the file for reading and writing
with open("samples/sample_text_file.txt", "r+", encoding="utf-8") as f:
    # Read the text-data
    my_text = f.read()
    # Adapt the text
    my_text = my_text.replace("banana", "orange")
    # Append the adapted text to the old file content
    f.write("This and the next part will be appended to the original:\n")
    f.write(my_text)
