# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import csv
import datetime
#import pyodbc

def dataframe_difference(df1, df2):
    
    primary_key_list = ['ID','FIRST_NAME'] #Defining Primary keys
    comparison_df = df1.merge(df2, on=primary_key_list,
                              indicator=True,
                              how='outer')
    print(comparison_df)
    diff_left = comparison_df[comparison_df['_merge'] == 'left_only']
    diff_right = comparison_df[comparison_df['_merge'] == 'right_only']
    diff_both = comparison_df[comparison_df['_merge'] == 'both']
    # Delete Rows Section
    cno = [] #Empty list to collect index values
    for idx in range(len(diff_left.columns)):
        if diff_left.columns[idx].endswith('_y'):
            cno.append(idx)
    cno.reverse() #Reversed the list 
    if len(cno) > 0:
        for n in range(len(cno)):
            diff_left = diff_left.drop(diff_left.columns[cno[n]], axis=1) #axis 0 is row axis 1 is col
    for idx in range(len(diff_left.columns)):
        if diff_left.columns[idx].endswith('_x'):
            orig_col_name = diff_left.columns[idx]
            new_col_name = orig_col_name.replace('_x','')
            diff_left = diff_left.rename(columns={orig_col_name: new_col_name})
    diff_left = diff_left.drop('_merge', axis=1)
    with open('deletedrows.csv', "w") as fptr:
        diff_left.to_csv(fptr, header=True, index=False, sep=',', quoting = csv.QUOTE_ALL, quotechar = '"')
    r,c = diff_left.shape #get Row and Col on the dataframe
    print(f"{datetime.datetime.now()} : Deleted Rows: {r}") #f denotes formatted string

    cno = []
    for idx in range(len(diff_right.columns)):
        if diff_right.columns[idx].endswith('_x'):
            cno.append(idx)
    cno.reverse()
    if len(cno) > 0:
        for n in range(len(cno)):
            diff_right = diff_right.drop(diff_right.columns[cno[n]], axis=1)
    for idx in range(len(diff_right.columns)):
        if diff_right.columns[idx].endswith('_y'):
            orig_col_name = diff_right.columns[idx]
            new_col_name = orig_col_name.replace('_y','')
            diff_right = diff_right.rename(columns={orig_col_name: new_col_name})
    diff_right = diff_right.drop('_merge', axis=1)
    with open('newrows.csv', "w") as f:
        diff_right.to_csv(f, header=True, index=False, sep=',', quoting = csv.QUOTE_ALL, quotechar = '"')
    r,c = diff_right.shape
    print(f"{datetime.datetime.now()} : New Rows: {r}")

    x_col_list = ['ID','FIRST_NAME']
    y_col_list = ['ID','FIRST_NAME']
    for idx in range(len(diff_both.columns)):
        if diff_both.columns[idx].endswith('_x'):
            x_col_list.append(diff_both.columns[idx])
        if diff_both.columns[idx].endswith('_y'):
            y_col_list.append(diff_both.columns[idx])
    df1 = diff_both[x_col_list]
    df2 = diff_both[y_col_list]
    
    xdf = df1.copy()
    ydf = df2.copy()

    for idx in range(len(xdf.columns)):
        if xdf.columns[idx].endswith('_x'):
            orig_col_name = xdf.columns[idx]
            new_col_name = orig_col_name.replace('_x','')
            xdf = xdf.rename(columns={orig_col_name: new_col_name})

    for idx in range(len(ydf.columns)):
        if ydf.columns[idx].endswith('_y'):
            orig_col_name = ydf.columns[idx]
            new_col_name = orig_col_name.replace('_y','')
            ydf = ydf.rename(columns={orig_col_name: new_col_name})
    
    df_diff = pd.concat([xdf,ydf]).drop_duplicates(keep=False)
    #df_diff.to_csv('modifiedrows.csv', index=False)
    with open('modifiedrows.csv', "w") as f:
        df_diff.to_csv(f, header=True, index=False, sep=',', quoting = csv.QUOTE_ALL, quotechar = '"')
    r,c = df_diff.shape
    print(f"{datetime.datetime.now()} : Modified Rows: {r}")

def main():
    print(f"{datetime.datetime.now()} : Process started")
    print(f"{datetime.datetime.now()} : Reading employees1.csv")
    mdf1 = pd.read_csv('employees1.csv')
    print(f"{datetime.datetime.now()} : Reading employees1.csv done")
    print(f"{datetime.datetime.now()} : Reading employees2.csv")
    mdf2 = pd.read_csv('employees2.csv')
    print(f"{datetime.datetime.now()} : Reading employees2.csv done")
    print(f"{datetime.datetime.now()} : Analyze start")
    dataframe_difference(mdf1, mdf2)
    print(f"{datetime.datetime.now()} : Analyze end")
    print(f"{datetime.datetime.now()} : Process ended")

if __name__ == '__main__':
    main()
