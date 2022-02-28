"""
Using docstring to REF -> Dr. Charles R. Severance P4E Exercises
"""
VAL = 0
emailHistogram = {}
# Default encoding é UTF-8
with open(r'DictPy\mbox-short.txt', 'r', encoding='UTF-8') as handle:
    for lines in handle:
        if lines.startswith('From '):
            words = lines.split()
            email = words[1]
            emailHistogram[email] = emailHistogram.get(email, 0) + 1
            VAL = list(emailHistogram.values())
    # print(emailHistogram)
    a = max(VAL)
    print(list(emailHistogram.keys())[
          list(emailHistogram.values()).index(a)], a)

# Consegui fazer o exercicio pg 130 P4E
