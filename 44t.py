import pandas as pd
import random

lst = ['robot'] * 10

lst += ['human'] * 10

random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})

data_one_hot = pd.DataFrame({'robot': [x == 'robot' for x in data['whoAmI']],
                             'human': [x == 'human' for x in data['whoAmI']]})

print(data_one_hot[['human', 'robot']].head())
