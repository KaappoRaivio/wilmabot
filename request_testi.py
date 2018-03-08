from HTMLParser import HTMLParser
import requests
import webbrowser
import re
#
#

def getSessionId(html):
    for i in html.split('\n'):
        if i.startswith('            <input type="hidden" name="SESSIONID" value='):
            a = i.split(' ')
            return a[len(a) - 1][7:19]

def avaaSelaimessa(filu):
    f = open('helloworld.html', 'w')

    message = filu

    f.write(message)
    f.close()

    filename = 'file:///home/kaappo/git/Random Paska/' + 'helloworld.html'
    webbrowser.open(filename)
#
#
#     # webbrowser.get(chrome_path).open(url)
#     return None
#
# # Fill in your details here to be posted to the login form.

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    response = s.get('https://wilma.espoo.fi/login')

    SESSIONID = getSessionId(response.text)
    payload = {

    'Login': 'kaappo.raivio',
    'Password': 'A2606gnu',
    'SESSIONID': SESSIONID

    }

    p = s.post('https://wilma.espoo.fi/login', data=payload)

    r = s.post('https://wilma.espoo.fi/groups/1101955', data=payload)

    # print(p.headers)
    avaaSelaimessa(p.text)

    # create a subclass and override the handler methods
    # class MyHTMLParser(HTMLParser):
    #     def handle_starttag(self, tag, attrs):
    #         pass
    #         # print("Encountered a start tag:", tag)
    #     def handle_endtag(self, tag):
    #         # print("Encountered an end tag :", tag)
    #         pass
    #     def handle_data(self, data):
    #         if 'Kotitehtävät 6.3.: Lue s. 182-183 tee tehtävät s. 184 2 ja 4 a ja b' is data:
    #             print("Encountered some data  :", data)
    #
    # # instantiate the parser and fed it some HTML
    # parser = MyHTMLParser()
    # parser.feed(open('/home>/kaappo/git/Random Paska/' + 'helloworld.html', 'r').read())

# with requests.Session() as s:
#     b = s.get('https://wilma.espoo.fi/login')
#     a = open('/home/kaappo/git/Random Paska/' + 'helloworld.html', 'w')
#     a.write(b.text)
#     a.close()
#
# for i in open('/home/kaappo/git/Random Paska/' + 'helloworld.html', 'r').read().split('\n'):
#     # print(i)
#     if i.startswith('            <input type="hidden" name="SESSIONID" value='):
#         a = i.split(' ')
#         print(a[len(a) - 1][6:20])
#
