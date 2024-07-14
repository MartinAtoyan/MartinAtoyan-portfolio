Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n1 = int(input())
6
>>> n2 = int(input())
4
>>> sym = input()
/
>>> if sym == "+":
...     print(n1 + n2)
... elif sym == "-":
...     print(n1-n2)
... elif sym == "*":
...     print(n1*n2)
... elif (sym == "/") and (n2 != 0):
...     res = float(n1/n2)
...     print(res)
... else:
...     print("An incorrect action was selected")
... 
...     
1.5
