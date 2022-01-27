# def replace_ending(sentence, old, new):
#     # Check if the old string is at the end of the sentence
#     if sentence.endswith(old):
#         # Using i as the slicing index, combine the part
#         # of the sentence up to the matched string at the 
#         # end with the new string
#         i = len(old)
#         new_sentence = sentence[:-i]+new
#         return new_sentence
#     # Return the original sentence if there is no match
#     return sentence


# ending = replace_ending("file.csv", "csv", "xlsx")
# print(ending)


# def is_palindrome(input_string):
#     # We'll create two strings, to compare them
#     new_string = ""
#     reverse_string = ""
#     # Traverse through each letter of the input string
#     for letter in input_string.strip():
#         # Add any non-blank letters to the 
#         # end of one string, and to the front
#         # of the other string. 
#         new_string = new_string+letter.replace(" ","")
#         reverse_string = letter.replace(" ","")+reverse_string
#     # Compare the strings
#     if new_string.lower() == reverse_string.lower():
#         return True
#     return False
    
# print(is_palindrome("level"))