Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list_count_Consonants = []
>>> list_count_Vowles = []
>>> Vowles = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Y", "y"]
>>> word = input()
Hello
>>> for l in word:
...     if l.isalpha():
...         if l in Vowles:
...             list_count_Vowles.append(l)
...         else:
...             list_count_Consonants.append(l)
... 
...             
>>> count_Vowles = len(set(list_count_Vowles))
>>> count_Consonants = len(set(list_count_Consonants))
>>> print(count_Vowles, count_Consonants)
2 2
