# Write a Python program to clone or copy a list.

strlist = ['abca', 'aeioua', 'aiwa', 'song', 'computer', 'a']
strlist2 = list(strlist)
strlist3 = strlist2.copy()

print(strlist2)
print(strlist3)
strlist3.remove('a')
print(strlist)
print(strlist3)