# To be used for educational materials,
# There is a mess, yet

# SCRIPTS FOR 
# pandas, numpy
# - datacleaning
# - preprocessing
# - data exploration
# - basic feature engeneering
# 
# Also to be reviewed:
# https://pandas.pydata.org/pandas-docs/stable/text.html
# http://pandas.pydata.org/pandas-docs/stable/groupby.html
# https://pandas.pydata.org/pandas-docs/stable/text.html
# https://www.programcreek.com/python/example/101351/pandas.read_html
# https://cloudxlab.com/blog/numpy-pandas-introduction/
# https://blog.thedataincubator.com/2018/02/numpy-and-pandas/
# https://realpython.com/python-data-cleaning-numpy-pandas/
# https://jakevdp.github.io/PythonDataScienceHandbook/03.03-operations-in-pandas.html
# https://www.analyticsvidhya.com/blog/2016/01/12-pandas-techniques-python-data-manipulation/
# https://www.dataquest.io/blog/programming-best-practices-for-data-science/
# https://towardsdatascience.com/how-to-shrink-numpy-scipy-pandas-and-matplotlib-for-your-data-product-4ec8d7e86ee4
# https://dataconomy.com/2015/03/14-best-python-pandas-features/
# https://sigdelta.com/blog/text-analysis-in-pandas/    
# https://www.dataquest.io/blog/programming-best-practices-for-data-science/
# https://stackoverflow.com/questions/50662176/best-practices-for-indexing-with-pandas
# https://www.datadan.io/python-pandas-pitfalls-hard-lessons-learned-over-time/
# https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-39e811c81a0c
  

import pandas as pd

time_sentences = ["Monday: The doctor's appointment is at 2:45pm.", 
                  "Tuesday: The dentist's appointment is at 11:30 am.",
                  "Wednesday: At 7:00pm, there is a basketball game!",
                  "Thursday: Be back home by 11:15 pm at the latest.",
                  "Friday: Take the train at 08:10 am, arrive at 09:00am."]

df = pd.DataFrame(time_sentences, columns=['text'])
df


# find the number of characters for each string in df['text']
df['text'].str.len()


# find the number of tokens for each string in df['text']
df['text'].str.split().str.len()


# find which entries contain the word 'appointment'
df['text'].str.contains('appointment')


# find which entries contain the word 'appointment'
df['text'].str.contains('appointment')

# find how many times a digit occurs in each string
df['text'].str.count(r'\d')

# find all occurances of the digits
df['text'].str.findall(r'\d')

# group and find the hours and minutes
df['text'].str.findall(r'(\d?\d):(\d\d)')

# replace weekdays with '???'
df['text'].str.replace(r'\w+day\b', '???')

# replace weekdays with 3 letter abbrevations
df['text'].str.replace(r'(\w+day\b)', lambda x: x.groups()[0][:3])

# create new columns from first match of extracted groups
df['text'].str.extract(r'(\d?\d):(\d\d)')

# extract the entire time, the hours, the minutes, and the period
df['text'].str.extractall(r'((\d?\d):(\d\d) ?([ap]m))')

# extract the entire time, the hours, the minutes, and the period with group names
df['text'].str.extractall(r'(?P<time>(?P<hour>\d?\d):(?P<minute>\d\d) ?(?P<period>[ap]m))')


#############
# to be used for edu materials:

# select
df.loc[df['column_name'] == some_value]
To select rows whose column value is in an iterable, some_values, use isin:

df.loc[df['column_name'].isin(some_values)]
Combine multiple conditions with &:

df.loc[(df['column_name'] == some_value) & df['other_column'].isin(some_values)]
To select rows whose column value does not equal some_value, use !=:

df.loc[df['column_name'] != some_value]
isin returns a boolean Series, so to select rows whose value is not in some_values, negate the boolean Series using ~:

df.loc[~df['column_name'].isin(some_values)]

If you have multiple values you want to include, put them in a list (or more generally, any iterable) and use isin:

print(df.loc[df['B'].isin(['one','three'])])


# Row side
df[3:6]
df['Aaron':'Christina']
# Col side

df[['food']]
df[['col_name1', 'col_name2']]

# Row side
df.loc['row1':'row2']
df.loc[row_selection, column_selection]
df.loc[['Dean', 'Cornelia'], ['age', 'state', 'score']]
df.loc[['Penelope','Cornelia'], :]


# Index
df2_idx = df2.set_index('Names')


# Bool indexing
so[so['answercount'] == 5]
so[so['quest_name'] == so['ans_name']]
so[so['ans_name'].isnull() & (so['score'] > 100)]
quest_higher_rep = so[so['quest_rep'] > so['ans_rep']]
so[so['answercount'].between(5, 10) & (so['viewcount'] < 1000)].head()

# Criteria 
criteria = (so['answercount'].between(5, 10) & (so['viewcount'] < 1000))
ex7 = so[~criteria]

deps = ['Parks & Recreation', 'Solid Waste Management', 'Fleet Management Department', 'Library']
c1 = employee['DEPARTMENT'].isin(deps)
c3 = employee['BASE_SALARY'] > 60000
employee[c1 & c3]

criteria = (employee['GENDER'] == 'Male') & (employee['BASE_SALARY'] > 100000)
employee.loc[criteria, ['RACE', 'GENDER', 'BASE_SALARY']].head()

criteria = so['ans_name'].isin(['Scott Boston', 'Ted Petrou', 'MaxU', 'unutbu'])
so.loc[criteria].head()

# Change type
df['BONUS'] = df['BONUS'].astype(int)
total_rows['ColumnID'] = total_rows['ColumnID'].astype(str)

# Assignment
df.loc[df['age'] > 10, 'score'] = 99

### IDIOMATIC

# is in
states = ['AL', 'LA', 'TX', 'FL', 'GA']
college[college['STABBR'].isin(states)].shape

# INDEXERS: [], .iloc, .loc, .ix, .at, .iat, that each do something different
#.ix has recently been deprecated in favor of .loc and .iloc

df.loc[['Aaron', 'Dean'], 'color'] = 'PURPLE'
df.loc[df['age'] < 30, 'score'] = 100








