import find_schedule
import json
from without_quotes import *

string_dict = find_schedule.find(open('filu.html', 'r').read())

string_dict = string_dict[25:]

print(string_dict)

# dictionary = dict(string_dict)

json = json.loads(string_dict)
