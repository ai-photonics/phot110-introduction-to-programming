# Open the file for reading and writing
with open("samples/sample_text_newfile.txt", "w+", encoding="utf-8") as f:
    # Create a file and add text to the file content
    f.write("This is my new file with some text:\n")
    f.writelines(["1 ..", "2 ..", "3 .."])
    f.write("Go! Notice that there is not enter or space before go")
