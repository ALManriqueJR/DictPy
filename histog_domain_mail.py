"""
Using docstring to REF -> Dr. Charles R. Severance P4E Exercises
"""

emails_domain_sum = {}

try:
    handle = open(r'DictPy/mbox-short.txt', 'r', encoding='UTF-8')
except Exception:
    print('Cannot reach the file')
    exit()

for lines in handle:
    lines = lines.rstrip()
    words = lines.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    email = words[1]
    emailsplit = email.split('@')
    domain = emailsplit[1]
    if domain not in emails_domain_sum:
        emails_domain_sum[domain] = 1
    else:
        emails_domain_sum[domain] += 1

print(emails_domain_sum)
