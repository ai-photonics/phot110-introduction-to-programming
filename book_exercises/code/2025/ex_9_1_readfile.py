# Open the file for only reading (file must exist)
f = open("samples/sample_text_poem.txt", "r", encoding="utf-8")
# Read the text-data
my_text = f.read()
# Close the file afterwards, otherwise data might not be saved or corrupt
print(my_text)
f.close()
