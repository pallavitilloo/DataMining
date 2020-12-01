#import re
#import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd
from gsppy.gsp import GSP
import time
#from mlxtend.frequent_patterns import apriori, association_rules

# def hot_encode(x):
#     if x <= 0:
#         return 0
#     if x >= 1:
#         return 1
#
# data = pd.read_csv('UK_DataDesc_Clean.csv', encoding="ISO-8859-1")
# # groupby('CustomerID')["Total cost"].mean('Revenue').
# # Stripping extra spaces in the description
# data['Description'] = data['Description'].str.strip()
#
# # Dropping the rows without any invoice number
# data.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
# data['InvoiceNo'] = data['InvoiceNo'].astype('str')
#
# # Dropping all transactions which were done on credit
# data = data[~data['InvoiceNo'].str.contains('C')]
#
#
# basket_UK = (data[data['Country'] =="United Kingdom"].groupby(['InvoiceNo', 'CustomerID'])['Quantity']
#              .sum().unstack().reset_index().fillna(0).set_index('InvoiceNo'))
#              #.sum().unstack().reset_index().fillna(0).set_index('InvoiceNo'))
#
# basket_encoded = basket_UK.applymap(hot_encode)
# basket_UK = basket_encoded
#
# frq_items = apriori(basket_UK, min_support = 0.1, use_colnames = True)
# rules = association_rules(frq_items, metric ="lift", min_threshold = 1)
# rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])
# print(rules)

# Sequence Mining
#
if __name__ == '__main__':
    start_time = time.time()

    # data = pd.read_csv('UK_DataDesc_Clean.csv', encoding = "ISO-8859-1", nrows=500).groupby(['InvoiceDate'])
    data = pd.read_csv('UK_DataDesc_New.csv', encoding = "ISO-8859-1", nrows=20).groupby(['InvoiceNo'])

    transactions = []
    transaction = []
    counter = 0
    i = 0
    prevItem = ""

    for item in data:
        stock = item[1]['StockCode'].tolist()
        stock = list(dict.fromkeys(stock))
        transactions.append(stock)

    result = GSP(transactions)

    print(result.search(0.05))
    print("--- %s seconds ---" % (time.time() - start_time))

