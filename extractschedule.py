import re
from html.parser import HTMLParser
from html.entities import name2codepoint
import sys

def extract(html):
    text = html

    lista = text.split('\n')


    pattern = re.compile(r'<h2 class="sr-only">')

    for i in range(len(lista)):
        match = pattern.search(lista[i])
        if match:
            lista = lista[i:]
            break

    else:
        print('ei toimi')

    pattern = re.compile('[\t]*<script type="text/javascript">')

    for i in range(len(lista)):
        match = pattern.search(lista[i])
        if match:
            lista = lista[:i]
            break
    else:
        print('eitoimi')

    schedule_part = '\n'.join(lista)

    #-------------------------------------------------------------------------------

    pattern = re.compile(r'<div tabindex="0" class="block" data-weekday[\w <>"=\-./:%;\(\)\,]+?</div>')


    string = schedule_part
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



    #-------------------------------------------------------------------------------



    class Oppitunti(object):

        id = 0

        def __init__(self):
            self.__id = Oppitunti.id
            self.data = []
            Oppitunti.id += 1

        def organizeData(self):
            # print(self)
            # print(self.data)
            # self.nimi_lyhyt = self.data[0].split(' ')[0]
            # self.nimi_pitkä = self.data[0].split(' ')[1]
            self.opettaja = self.data[len(self.data) - 2]
            self.sijainti = self.data[len(self.data) - 1]
            # del self.data

        def printAttrs(self):

            for key, value in self.__dict__.items():
                print('{}: {}'.format(key, value))

        def getData(self, tag, attrs):
            self.data.append(attrs['title'])

        def getWeekday(self, tag, attrs):
            self.viikonpäivä = attrs['data-weekday']

        def ajat(self, data):
            lista = data.split(': ')
            self.alkamisaika = lista[1][11:16]
            self.päättymisaika = lista[1][29:34]
            self.nimi_lyhyt = lista[2]


    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            temp = {}
            # print(attrs)
            for i in range(len(attrs)):
                temp[attrs[i][0]] = attrs[i][1]
            # print(temp)
            attrs = temp


            # viikonpäivä
            if tag == 'div' and 'data-weekday' in attrs:
                self.instance.getWeekday(tag, attrs)

            #  tunnin nimi

            if tag == 'a' and 'title' in attrs and 'class' in attrs and 'normal teachers profile-link no-underline-link' not in attrs:
                # print('asd\n\n')
                self.instance.getData(tag, attrs)

        def handle_data(self, data):
            lista = data.split(': ')

            if lista[0].lower() in ['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai']:
                self.instance.ajat(data)




    strings = entries

    objektit = [Oppitunti() for i in range(len(strings))]

    for i in range(len(strings)):
        testi = Oppitunti()
        parsaaja = MyHTMLParser()

        parsaaja.instance = objektit[i]

        parsaaja.feed(strings[i])

        objektit[i].organizeData()

    return objektit


if __name__ == '__main__':
    print('ehi')
    extract(open('kakka.txt', 'r').read())
