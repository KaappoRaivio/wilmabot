text = open('kakka.txt', 'r').read()

lista = text.split('\n')

for i in range(len(lista)):
    if lista[i].startswith('          <h2 class="sr-only">'):
        lista = lista[i:]
        break

else:
    print('ei toimi')

for i in range(len(lista)):
    if lista[i].startswith('      <script type="text/javascript">'):
        lista = lista[:i]
        break
else:
    print('eitoimi')

schedule_part = '\n'.join(lista)

schedule_part
