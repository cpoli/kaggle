# The data comes both as CSV files and a SQLite database

import pandas as pd
import sqlite3
import seaborn as sns
import numpy as np
import  matplotlib.pyplot as plt

# You can read in the SQLite datbase like this
import sqlite3
sql_conn = sqlite3.connect('../../Documents/data_hillary/database.sqlite')
df = pd.read_sql_query("""SELECT MetadataDateSent, SenderPersonId FROM emails""", sql_conn)
ID = pd.read_sql_query('SELECT Id, Name FROM persons', sql_conn, index_col='Id')


pseudo = ["sbwhoeop","pir","millscd@state.gov","abedinh@state.gov",
              "cheryl.mills","mills, cheryl","jake.sullivan","sullivan, jake", 
              "mills, chery","sullivanjj@state.gov","jilotylc@state.gov","pverveer",
              "pverveer","valmorolj@state.gov","preines","hanleymr@state.gov",
              "slaughtera@state.gov","vermarr@state.gov","russorv@state.gov","balderstonkm@state.gov",
              "muscatinel@state.gov","reinesp@state.gov","crowleypj@state.gov","stalbott",
              "mchaleja@state.gov","campbellkm@state.gov","verveerms@state.gov","steinbergjb@state.gov",
              "lewjj@state.gov"]
              
real_names = ["Blumenthal, Sidney","Reines, Philippe I","Mills, Cheryl D","Abedin, Huma",
         "Mills, Cheryl D","Mills, Cheryl D","Sullivan, Jacob J","Sullivan, Jacob J",
         "Mills, Cheryl D","Sullivan, Jacob J","Jiloty, Lauren C","Verveer, Melanne S",
         "Verveer, Melanne S","Valmoro, Lona J","Reines, Philippe I","Hanley, Monica R",
         "Slaughter, Anne-Marie","Verma, Richard R","Russo, Robert V","Balderston, Kris M",
         "Muscatine, Lissa","Reines, Philippe I","Crowley, Philip J","Talbott, Strobe",
         "McHale, Judith A","Campbell, Kurt M","Verveer, Melanne S","Steinberg, James B",
         "Lew, Jacob J"]

ID['Name'] = ID['Name'].str.lower()
df = df.dropna(how='all').copy()

# select HRC from the sender list
person_of_interest = 'hillary'
person_id = ID[ID.Name.str.contains(person_of_interest)].index.values
df = df[(df['SenderPersonId']==person_id[0])]

# create datetime objects
df['MetadataDateSent'] = pd.to_datetime(df['MetadataDateSent'])
df = df.set_index('MetadataDateSent')

# 0 for Monday, 6 for Sunday
df['dayofweek'] = df.index.dayofweek

sns.set_style('white')
t_labels = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
ax = sns.barplot(x=np.arange(0,7), y=df.groupby('dayofweek').SenderPersonId.count(),\
    label=t_labels, palette="RdBu")
sns.despine(offset=10)
ax.set_xticklabels(t_labels)
ax.set_ylabel('Message Count')
ax.set_title('HRC\'s Sent Emails')
#plt.savefig('seventhday.png', bbox='tight')
plt.show()