
import pandas as pd
import json

# with open('C:/Users/chand/PycharmProjects/JSONtoExcel/data/Aug.json') as json_file:
   # data = json.load(json_file)
   # df = pd.DataFrame(data)
    #df.to_excel('C:/Users/chand/PycharmProjects/JSONtoExcel/Excel data/Aug.xlsx')


df = pd.read_json('C:/Users/chand/PycharmProjects/JSONtoExcel/data/Aug.json')
df.to_excel('C:/Users/chand/PycharmProjects/JSONtoExcel/Excel data/Aug.xlsx')
