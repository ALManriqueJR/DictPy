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
    lst_min_max = []
    for key, val in emailHistogram.items():
        lst_min_max.append((val, key))
        if val == max(VAL):
            print('Max.sender:', key, 'Qt.:', val)
        elif val == min(VAL):
            print('Min.sender:', key, 'Qt.:', val)
    # Individual request
    # print(list(emailHistogram.keys())[
    #       list(emailHistogram.values()).index(a)], a)

# Exerc. pg. 130 P4E
