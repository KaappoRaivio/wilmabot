# from HTMLParser import HTMLParser
import requests
import webbrowser
# import re


def getSessionId(html):
    for i in html.split('\n'):
        if i.startswith('            <input type="hidden" name="SESSIONID" value='):
            a = i.split(' ')
            return a[len(a) - 1][7:19]
    return 0


def getSessionKey(html):
    for i in html.split('\n'):
        if i.startswith('                <input type="hidden" name="formkey" value="'):
            a = i.split(' ')
            return a[len(a) - 1][7:len(a[len(a) - 1]) - 3]
    return 0


def avaaSelaimessa(filu):
    f = open('helloworld.html', 'w')

    message = filu

    f.write(message)
    f.close()

    filename = '/home/kaappo/git/wilmabot/' + 'helloworld.html'
    webbrowser.open(filename)


with requests.Session() as s:
    response = s.get('https://wilma.espoo.fi/login')

    SESSIONID = getSessionId(response.text)

    payload = {
        'Login': 'kaappo.raivio',
        'Password': 'A2606gnu',
        'SESSIONID': SESSIONID
    }

    p = s.post('https://wilma.espoo.fi/login', data=payload)

    SESSIONID = getSessionId(p.text)
    SESSIONKEY = getSessionKey(p.text)

    payload = {
        'Login': 'kaappo.raivio',
        'Password': 'A2606gnu',
        'SESSIONID': SESSIONID,
        'formkey': SESSIONKEY
    }

    r = s.post('https://wilma.espoo.fi/groups/1101786', data=payload)

    # print(p.headers)
    print(p.text)
    print(getSessionKey(p.text))
    avaaSelaimessa(r.text)
