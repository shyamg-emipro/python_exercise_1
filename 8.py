# Write a Python program to test whether a passed letter is a vowel or not.

letter = input("Enter a Single Character: ")
print("The given Letter is Vowel!" if letter.lower() in ('a', 'e', 'i', 'o', 'u') else "The given Letter is not a Vowel!")