import requests
import webbrowser
import os



def avaaSelaimessa(filu):
    f = open('temp.html', 'w')

    message = filu

    f.write(message)
    f.close()

    filename = '/home/kaappo/git/wilmabot/temp.html'
    webbrowser.open(filename)
    # os.remove(filename)


class Wilma:
    id = 0
    def __init__(self, credentials='credentials.txt'):
        self.__password = eval(open('credentials.txt', 'r').read())['Password']
        self.__username = eval(open('credentials.txt', 'r').read())['Login']
        self.session = requests.Session()
        self.__id = Wilma.id
        Wilma.id += 1

    def __del__(self):
        print('Poistetaan {}'.format(self.__id))
        self.session.close()

    @property
    def credentials(self):
        return {'Login': self.__username, 'Password': self.__password}

    @staticmethod
    def getSessionId(html):
        for i in html.split('\n'):
            if i.startswith('            <input type="hidden" name="SESSIONID" value='):
                return i.split(' ')[len(i.split(' ')) - 1][7:19]
        else:
            return 0


    def handleLogin(self):

        payload = self.credentials

        response = self.session.get('https://wilma.espoo.fi/login')

        self.session_id = Wilma.getSessionId(response.text)

        self.payload = {'SESSIONID': self.session_id, **payload}

        response = self.session.post('https://wilma.espoo.fi/login', self.payload)

        return response.status_code

    def getPage(self, url):
        return self.session.get(url, data=self.payload)


botti = Wilma()
print(botti.handleLogin())

# avaaSelaimessa(botti.getPage('https://wilma.espoo.fi/schedule').text)

print(botti.getPage('https://wilma.espoo.fi/schedule').text)

del botti
