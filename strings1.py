#Python string patterns
import re
from collections import Counter

alist=['ROKU price target raised to 17 from 13', 'AAPL price target raised to 17 from 13', 
'TSLA price target raised to 17 from 13', 'ROKU price target raised to 16 from 15', 
'ROKU price target raised to 17 from 13', 'TSLA price target raised to 13 from 18']
alist_changed = []

pattern = r' price target raised to .*'

for x in alist:
    y = re.sub(pattern, '', x, 1)
    alist_changed.append(y)

print(alist_changed)
print(Counter(alist_changed))
