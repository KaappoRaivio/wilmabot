import re

pattern = re.compile(r'<div tabindex="0" class="block" data-weekday[\w <>"=\-./:%;\(\)\,]+?</div>')
# pattern = re.compile(r'[\w <>"=\-./:%;\(\)\,]+')

# string = open('kakka3.txt', 'r').read()
string = input()

match = True

entries = []

while match is not None:
    match = pattern.search(string)
    try:
        # print(match.group() + '\n')
        entries.append(match.group())
        string = string[match.span()[1]:]
    except AttributeError:
        break
print(len(entries))
print('\n'.join(entries))
