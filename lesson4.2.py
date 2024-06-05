Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> students = { "Bob":90,
...              "Smith":75,
...              "James":40
...              }
>>> students["Mark"] = 50
>>> print("upadeted  dictionary" students)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> students = { "Bob":90,
...              "Smith":75,
...              "James":40
...              }
>>> students["Mark"] = 50
>>> print(students)
{'Bob': 90, 'Smith': 75, 'James': 40, 'Mark': 50}
>>> students["Bob"] = 100
>>> del students["Smith"]
>>> print(students)
{'Bob': 100, 'James': 40, 'Mark': 50}
