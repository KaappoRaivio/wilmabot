from html.parser import HTMLParser
from html.entities import name2codepoint


class Oppitunti(object):

    id = 0

    def __init__(self):
        self.__id = Oppitunti.id
        Oppitunti.id += 1

    def organizeData(self):
        self.nimi_lyhyt = self.data[0].split(' ')[0]
        self.nimi_pitkä = self.data[0].split(' ')[1]
        self.opettaja = self.data[1]
        self.sijainti = self.data[2]

    def printAttrs(self):
        temp = {}
        for i in dir(self):
            if not i.startswith('__'):
                temp[i] = (str(self.__getattribute__(i)))

        print(temp)
        for key, value in temp.items():
            print('{}: {}'.format(key, value))

testi = Oppitunti()


def getWeekday(tag, attrs):
    print(attrs['data-weekday'])
    testi.viikonpäivä = attrs['data-weekday']


def getData(tag, attrs):
    print("asd" + attrs['title'])
    try:
        testi.data.append(attrs['title'])
    except AttributeError:
        testi.data = [attrs['title']]


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
            getWeekday(tag, attrs)

        #  tunnin nimi

        if tag == 'a' and 'title' in attrs and 'class' in attrs and not 'normal teachers profile-link no-underline-link' in attrs:
            print('asd\n\n')
            getData(tag, attrs)

        print("Start tag:", tag)
        for key in attrs:
            print("\tattr: {}: {}".format(key, attrs[key]))


    def handle_endtag(self, tag):
        print("<{}>".format(tag))


    def handle_data(self, data):
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


parsaaja = MyHTMLParser()

parsaaja.feed(open('kakka.txt', 'r').read())


testi.organizeData()
testi.printAttrs()
