# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 12:20:39 2019

@author: puthran1
"""

import pandas as pd
import csv
import time


#data1 = {'ID':[424, 989, 318, 996, 516, 743, 207, 764, 950, 434, 863, 250],
#        'FIRST_NAME':["Regine", "Jessa", "Marci", "Olympe", "Baxy", "Melba", "Willie", "Noby", "Avery", "Richart", "Kalindi", "Marley"],
#        'LAST_NAME':["Aberkirder" , "Acome" , "Acres" , "Acutt" , "Adamides" , "Addey" , "Addionisio" , "Agutter" , "Ahlin" , "Akid" , "Alebrooke" , "Alen"],
#        'EMAIL':["raberkirderbr@shop-pro.jp" , "jacomerg@ustream.tv" , "macres8t@paypal.com" , "oacuttrn@flickr.com" , "badamideseb@google.pl" , "maddeykm@vimeo.com" , "waddionisio5q@hhs.gov" , "nagutterl7@ow.ly" , "aahlinqd@ihg.com" , "rakidc1@ow.ly" , "kalebrookeny@biglobe.ne.jp" , "malen6x@fema.gov"],
#        'GENDER':["Female" , "Female" , "Female" , "Female" , "Male" , "Female" , "Male" , "Male" , "Male" , "Male" , "Female" , "Female"],
#        'DEPARTMENT':["Marketing" , "Business Development" , "Marketing" , "Support" , "Research and Development" , "Accounting" , "Human Resources" , "Accounting" , "Research and Development" , "Engineering" , "Product Management" , "Legal"]
#       }
#
#data2 = {'ID':[424, 989, 318, 996, 516, 743, 207, 764, 950, 434, 863, 1],
#        'FIRST_NAME':["Regine", "Jessa", "Marci", "Olympe", "Baxy", "Melba", "Willie", "Noby", "Avery", "Richart", "Kalindi", "Nitin"],
#        'LAST_NAME':["Aberkirder" , "Acome" , "Acres" , "Acutt" , "Adamides" , "Addey" , "Addionisio" , "Agutter" , "Ahlin" , "Akid" , "Alebrooke" , "Puthran"],
#        'EMAIL':["raberkirderbr@shop-pro.jp" , "jacomerg@ustream.tv" , "macres8t@paypal.com" , "oacuttrn@flickr.com" , "badamideseb@google.pl" , "maddeykm@vimeo.com" , "waddionisio5q@hhs.gov" , "nagutterl7@ow.ly" , "aahlinqd@ihg.com" , "rakidc1@ow.ly" , "kalebrookeny@biglobe.ne.jp" , "nitin@gmail.com"],
#        'GENDER':["Female" , "Female" , "Female" , "Female" , "Male" , "Female" , "Male" , "Male" , "Male" , "Male" , "Female" , "Male"],
#        'DEPARTMENT':["Marketing" , "Business Development" , "Marketing" , "Support" , "Research and Development" , "Accounting" , "Human Resources" , "Accounting" , "Research and Development" , "Engineering" , "GTIR" , "IT"]
#       }
#
#df1 = pd.DataFrame(data1, columns=data1.keys())
#df2 = pd.DataFrame(data2, columns=data1.keys())
#
#with open('employees1.csv', "w") as f:
#    df1.to_csv(f, header=True, index=False, sep=',', quoting = csv.QUOTE_ALL, quotechar = '"')
#
#with open('employees2.csv', "w") as f:
#    df2.to_csv(f, header=True, index=False, sep=',', quoting = csv.QUOTE_ALL, quotechar = '"')
numOfRows = 2000000
startTime = time.perf_counter()
row_list = []
for i in range( 1,numOfRows+1):
    dict1 = dict(ID = i,
                 FIRST_NAME = f"fn{i}",
                 LAST_NAME = f"ln{i}",
                 EMAIL = f"email{i}.com",
                 GENDER = f"gender{i}",
                 DEPARTMENT = f"department{i}")
    row_list.append(dict1)
print('Elapsed time: {:6.3f} seconds for {:d} rows'.format(time.perf_counter() - startTime, numOfRows))

startTime = time.perf_counter()
df = pd.DataFrame(row_list, columns=["ID", "FIRST_NAME", "LAST_NAME", "EMAIL", "GENDER", "DEPARTMENT"])
with open('employees2.csv', "w") as f:
    df.to_csv(f, header=True, index=False, sep=',', quoting = csv.QUOTE_ALL, quotechar = '"')
print('Elapsed time: {:6.3f} seconds for {:d} rows'.format(time.perf_counter() - startTime, numOfRows))
print(df.shape)
