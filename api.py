import requests

class Wilma:
    def __init__(self, credentials='credentials.txt'):
        self.__password = eval(open('credentials.txt', 'r').read())['Password']
        self.__username = eval(open('credentials.txt', 'r').read())['Login']

    @property
    def credentials(self):
        return {'Login': self.__username, 'Password': self.__password}

    def handleLogin(self):
        def _getSessionId(html):
            for i in html.split('\n'):
                if i.startswith('            <input type="hidden" name="SESSIONID" value='):
                    return i.split(' ')[len(i.split(' ')) - 1][7:19]
            else:
                return 0

        with requests.Session() as s:
            payload = eval(open('credentials.txt', 'r').read())

            response = s.get('https://wilma.espoo.fi/login')

            session_id = _getSessionId(response.text)

            s.post('https://wilma.espoo.fi/login', data={'SESSIONID': session_id, **payload}).text, 'temp'
            s.get('https://wilma.espoo.fi/groups/1101955').text, 'temp1'

            self.session = s
