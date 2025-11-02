#create a program named numeric_character_analytics.py

#prompt the user to enter a line of text
words = input("Please enter a line of text")
#for each word in the line of text, print the quantity of numeric digits in the word
wrd_list = list(words.split())
l_words = len(words)
print(wrd_list)
numb_digits = 0

if l_words == 0:
    print("0 words were analyzed")
else:
    for word in wrd_list:
        numb_digits = 0
        for val in word:
            if val.isdigit():
                numb_digits += 1
        print(f'"{word}" contains {numb_digits} numeric characters.') 
