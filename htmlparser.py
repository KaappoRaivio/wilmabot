from html.parser import HTMLParser
from html.entities import name2codepoint
import sys


class Oppitunti(object):

    id = 0

    def __init__(self):
        self.__id = Oppitunti.id
        self.data = []
        Oppitunti.id += 1

    def organizeData(self):
        print(self.data)
        self.nimi_lyhyt = self.data[0].split(' ')[0]
        self.nimi_pitkä = self.data[0].split(' ')[1]
        self.opettaja = self.data[1]
        self.sijainti = self.data[2]

    def printAttrs(self):
        temp = {}
        for i in self.__dict__:
            if not i.startswith('__'):
                temp[i] = (str(self.__getattribute__(i)))

        # print(temp)
        for key, value in temp.items():
            print('{}: {}'.format(key, value))

    def getData(self, tag, attrs):

        print("asd" + attrs['title'])


        self.data.append(attrs['title'])

        print(str(testi.data) + '\n\n\n\n\n\n\n\n\n\n')


    def getWeekday(self, tag, attrs):
        print(attrs['data-weekday'])
        self.viikonpäivä = attrs['data-weekday']

    def viikonpäivä(self, data):
        lista = data.split(' ')
        self.alkamisaika = lista[1][11:16]
        self.päättymisaika = lista[1][29:34]


testi = Oppitunti()



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
            testi.getWeekday(tag, attrs)

        #  tunnin nimi

        if tag == 'a' and 'title' in attrs and 'class' in attrs and 'normal teachers profile-link no-underline-link' not in attrs:
            print('asd\n\n')
            testi.getData(tag, attrs)

        # print("Start tag:", tag)
        # for key in attrs:
        #     print("\tattr: {}: {}".format(key, attrs[key]))


    def handle_endtag(self, tag):
        # print("<{}>".format(tag))
        pass

    def handle_data(self, data):
        lista = data.split(': ')

        if lista[0].lower() in ['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai']:
            testi.viikonpäivä(data)
        print("\tData: {}".format(data))


    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

    # def handle_comment(self, data):
    #     print("Comment  :", data)
    #
    # def handle_entityref(self, name):
    #     c = chr(name2codepoint[name])
    #     print("Named ent:", c)
    #
    # def handle_charref(self, name):
    #     if name.startswith('x'):
    #         c = chr(int(name[1:], 16))
    #     else:
    #         c = chr(int(name))
    #     print("Num ent  :", c)
    #
    # def handle_decl(self, data):
    #     print("Decl     :", data)


def call(string=open(sys.argv[1]).read()):
    print(string)
    testi = Oppitunti()
    parsaaja = MyHTMLParser()
    parsaaja.feed(string)

    testi.organizeData()
    return testi

if __name__ == '__main__':
    call()
