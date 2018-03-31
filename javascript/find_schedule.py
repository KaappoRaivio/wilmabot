import re

# string = open('filu.html', 'r').read()
#
# pattern_alku = re.compile('<script type="text/javascript">')
# pattern_loppu = re.compile('var weekdays')
#
# lista = string.split('\n')
#
# a = 0
#
# for i in lista:
#     if pattern_alku.search(i):
#         lista = lista[a:]
#         break
#     # å = print(pattern_loppu.search(i).group(), a) if pattern_loppu.search(i) is not None else None
#     a += 1
#
# print(lista)
#
# a = 0
#
# for i in lista:
#     if pattern_loppu.search(i):
#         lista = lista[:a]
#         break
#     # å = print(pattern_loppu.search(i).group(), a) if pattern_loppu.search(i) is not None else None
#     a += 1
#
# print('\n'.join(lista))

def find(string):
    pattern_alku = re.compile('        var eventsJSON = ')
    pattern_loppu = re.compile('var weekdays')

    lista = string.split('\n')

    a = 0

    for i in lista:
        if pattern_alku.search(i):
            lista = lista[a:]
            break
        # å = print(pattern_loppu.search(i).group(), a) if pattern_loppu.search(i) is not None else None
        a += 1

    # print(lista)

    a = 0

    for i in lista:
        if pattern_loppu.search(i):
            lista = lista[:a]
            break
        # å = print(pattern_loppu.search(i).group(), a) if pattern_loppu.search(i) is not None else None
        a += 1

    return '\n'.join(lista)

if __name__ == '__main__':
    print(find(open('filu.html', 'r').read()))
