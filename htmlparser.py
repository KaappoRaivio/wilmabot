# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class Oppitunti(object):
    def __init__(self):
        pass

testi = Oppitunti()


def getWeekday(tag, attrs):
    print attrs['data-weekday']
    testi.viikonpaiva = attrs['data-weekday']

def getTitle(tag, attrs):
    print "asd" + attrs['title']
    testi.nimi = attrs['title']

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        temp = {}
        # print(attrs)
        for i in range(len(attrs)):
            temp[attrs[i][0]] = attrs[i][1]
        # print(temp)
        attrs = temp


        # viikonpaiva
        if tag == 'div' and 'data-weekday' in attrs:
            getWeekday(tag, attrs)

        #tunnin nimi
        if tag == 'a' and 'title' in attrs and 'class' in attrs and not 'normal teachers profile-link no-underline-link' in attrs:
            print 'asd\n\n'
            getTitle(tag, attrs)

        print "Start tag:", tag
        for key in attrs:
            print "\tattr: {}: {}".format(key, attrs[key])

    def handle_endtag(self, tag):
        print("<{}>".format(tag))

    def handle_data(self, data):
        print "\tData: {}".format(data)

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


print testi.nimi, testi.viikonpaiva
