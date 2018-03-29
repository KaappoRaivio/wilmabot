import re

string = open('filu.html', 'r').read()

pattern_alku = re.compile('      <script type="text/javascript">')
pattern_loppu = re.compile('[\t ]*</script>')

for i in string.split('\n'):
    a = print(pattern_alku.search(i)) if pattern_alku.search(i) is not None else None
