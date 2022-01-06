# Write a Python program to count the number of strings in a list where the string length is 2 or more and the first and last character are the same from a given list of strings.

strlist = ['abca', 'aeioua', 'aiwa', 'song', 'computer', 'a']


def filterstr(str1):
    if len(str1) >= 2:
        if str1[0] == str1[len(str1) - 1]:
            return True
    else:
        return False


filteredlist = filter(filterstr, strlist)
print(list(filteredlist))
