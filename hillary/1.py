
import pandas as pd
import networkx as nx
import numpy as np
from collections import Counter, defaultdict
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import operator

# read the main data source
emails = pd.read_csv("../../Documents/data_hillary/Emails.csv")

l = []
#emails['MetadataSubject']

print(emails['ExtractedBodyText'])
for e in emails['ExtractedBodyText'][:100]:
    if not isinstance(e, str):
        continue
    l.append(e.split())

d = {}
ll = [item for sublist in l for item in sublist]
for w in set(ll):
    d[w] = ll.count(w)
d.keys = d.keys.upper()
basic = ['OF', 'AT', 'A', 'AS', 'FOR', 'TO', 'ON', 'THE', 'THAT', 'THIS', 'WITH', 'FROM', 'IN', 
            'AND', 'BY', 'NO',  'NOT', 'BUT', 'IF',   'UP', #basic 
            'IS', 'S', 'BE', 'AM', 'ARE', 'DID', 'HAVE', 'DO', 'I', 'HE', 'SHE',  'WE', 'U',  'YOU', 'YOU.', 'YOUR',
              'THEY', 'ME',  'WILL', 'US', 'HAS',  'OUR', 'CAN', # pronums and have/be verbs
             'HILLARY', 'H:',  'FW:',  'SID', 'RE', 'RE:',  'FYI:', 'FYI', 'FYI,', '-',  '&', '@', '2', '�2M-A-YEAR', '--', # symbols and Hillary
             'THANKS',  'OR', 'MEMO', 'QUESTION', 'REMARKS', 'STATEMENT', 'AUTOREPLY:', 
            'MY', 'SO', 'ABOUT',  'ANY', 'WHEN',  'SAYS',   'MORE','ALL', 'OVER', 'OUT',
            'FAX', 'LIST', 'MAY', 'IT',  'GET', 'GOOD', 'ANOTHER',  'EMAIL', 'TWO', 'LATEST', 'TALK', 'TALK?',
            'TEXT', 'JUST', 'ASKING', 'BACK', 'TALKS', 'CALLED', 'CALL', 'CALLS', 'CALL?', 'ARTICLE', 'REPORT',
            'MEETING', 'DRAFT', 'NEWS', 'FOLLOW', 'CONFERENCE', ''
            'SHEET', 'UPDATE', 'LETTER', 'FOLLOWUP', 'NOTE', 'NEED',  'SCHEDULE', 'NEW',
            "SECRETARY'S", "SECRETARY", 'TODAY', 'TOMORROW', 'TRIP',
            'THANK', 'CONFIRMED', 'OFFICE', 'MESSAGE', 'LAST', 'START'] # verbs & nums

for b in basic:
    if b in d:
        d.pop(b.upper())

print(d.values())
print(d.keys())

#print([val for val, key in d.items() if key>30])
words_30 = {key: val for key, val in sorted(d.items()) if val>30}
#ax = sns.barplot(x=np.arange(0,len(words_30)), y=words_30, palette="RdBu")
#words_30_sort = sorted(words_30.items(), key=operator.itemgetter(1))
#print(words_30_sort)
print(words_30)
print()
vals = sorted(words_30.values())
keys = sorted(words_30, key=words_30.get)
print(vals)
print(keys)
fig = plt.figure(figsize=(4, 8))
x = range(0, 4*len(words_30), 4)
plt.barh(x, vals, align='center')
x_ticks = np.linspace(0, max(vals), 10, 'i4')
plt.xticks(x_ticks)
plt.yticks(x,keys)
plt.ylim((x[0]-1, x[-1]+1))
plt.xlim((0, max(vals)))


plt.show()
