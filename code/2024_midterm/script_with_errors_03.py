# This script contains errors and doesn't run.
#
# The correct script prompts the user to type a sentence.
# It then reverses the order of the words, prints this
# reversed sentence on the console and saves it to a
# text-file.
#
# Correct the errors so that it gives the intended output.

# Prompt the user to input a sentence:
sentence = input("Please enter a sentence: ")

# Split the sentence into words and reverse the order
sentence.split() = word_list
word_list_reversed =
    reversed(word_list)
# Put the sentence back together using the reversed ordered words.
sentence_reversed = ' '.join(word_list_reversed)

# Print the reversed sentence
 print("The reversed version of the sentence is:\n" + reversed)
# Save the sentence to a file
f = open(file="output_text_script_with_errors_03.txt", mode="w+"):
    f.write(sentence_reversed)
f.close()
