# Write a Python program to test whether a passed letter is a vowel or not.

letter = input("Enter a Single Character: ")

if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("The given Letter is Vowel!")
else:
    print("The given Letter is not a Vowel!")