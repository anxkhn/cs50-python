from cs50 import get_string

text = get_string("Text: ")
words = text.count(" ") + 1
sentences = text.count(".") + text.count("!") + text.count("?")

letters = 0
for i in text:
    if i.isalpha():
        letters += 1
# calculation variables
L = letters / words * 100
S = sentences / words * 100
# calculation of index number
index = int(round(0.0588 * L - 0.296 * S - 15.8))
# printing different cases
if index <= 1:
    print("Before Grade 1")
elif index > 1 and index < 16:
    print(f"Grade {index}")
else:
    print("Grade 16+")
