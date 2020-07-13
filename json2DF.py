import json, pandas as pd

demo = pd.read_json('Kindle_Store_5.json')

'''
demo = [{
    'Name' : 'Rahul',
    'Address' : 'Guwahati',
    'Age' : '21'
}]
'''

# x = json.dumps(demo)  # not really neccessary

y = pd.DataFrame(demo)   # converting json -> df

# y.to_excel('Demo.xlsx', index = False, encoding = 'utf-8')  # df -> excel
y.to_csv('Demo.csv', index = False, encoding = 'utf-8')   # df -> csv

# print(y, y.shape)