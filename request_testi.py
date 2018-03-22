# from HTMLParser import HTMLParser
import requests
import webbrowser
# import re


def getSessionId(html):
    for i in html.split('\n'):
        if i.startswith('            <input type="hidden" name="SESSIONID" value='):
            return i.split(' ')[len(i.split(' ')) - 1][7:19]
    else:
        return 0


def getSessionKey(html):
    for i in html.split('\n'):
        if i.startswith('                <input type="hidden" name="formkey" value="'):
            a = i.split(' ')
            return a[len(a) - 1][7:len(a[len(a) - 1]) - 3]
    else:
        return 0


def avaaSelaimessa(filu, filename2):
    f = open(filename2, 'w')

    message = filu

    f.write(message)
    f.close()

    filename = '/home/kaappo/git/wilmabot/' + filename2
    webbrowser.open(filename)


with requests.Session() as s:
    payload = eval(open('credentials.txt', 'r').read())

    response = s.get('https://wilma.espoo.fi/login')

    session_id = getSessionId(response.text)

    avaaSelaimessa(s.post('https://wilma.espoo.fi/login', data={'SESSIONID': session_id, **payload}).text, 'temp')
    avaaSelaimessa(s.get('https://wilma.espoo.fi/groups/1101955').text, 'temp1')

    print(s.cookies)
