import numpy as np
import pandas as pd
import sys


sys.stdout = open("D:\\Businesses\\Automation Nation\\extractor\\codeForFilteredData\\halfCleanNames.csv", "w", encoding='utf-8')

with open("D:\\Businesses\\Automation Nation\\extractor\\codeForFilteredData\\alldata.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()  # read all lines into a list

    for index, line in enumerate(lines):  # enumerate the list and loop through it
        if "Requested" in line:  # check if the current line has your substring
            #  print (line.strip ())  # print the current line (stripped off whitespace)
            print("".join(lines[max(0, index - 1):index]))  # print three lines preceding it
        #    outSheet.write ("A1", "lines")

sys.stdout.close()

df2 = pd.read_csv("D:\\Businesses\\Automation Nation\\extractor\\codeForFilteredData\\halfCleanNames.csv", header=None, names=["Names"])

sortedNames = df2.dropna(how="all")

sortedNames.to_csv("D:\\Businesses\\Automation Nation\\extractor\\codeForFilteredData\\sortedNames.csv", index=False, columns=["Names"])

sys.stdout = open("D:\\Businesses\\Automation Nation\\extractor\\codeForFilteredData\\halfCleanEmails.csv", "w", encoding='utf-8')

with open("D:\\Businesses\\Automation Nation\\extractor\\codeForFilteredData\\alldata.txt", "r", encoding='utf-8') as f:

    counter=0

    for line in f:
        if "Email" in line or "email" in line or "E-mail" in line or "e-mail" in line:
            print(next(f, ''))
            counter=0
        elif "Requested" in line:
            if counter > 0:
                print("no Email")
            counter += 1

sys.stdout.close()

df = pd.read_csv("D:\\Businesses\\Automation Nation\\extractor\\codeForFilteredData\\halfCleanEmails.csv", header=None, names=["Emails"])

sortedEmails = df.dropna(how="all")

sortedEmails.to_csv("D:\\Businesses\\Automation Nation\\extractor\\codeForFilteredData\\sortedEmails.csv", index=False, columns=["Emails"])

csv1 = 'D:\\Businesses\\Automation Nation\\extractor\\codeForFilteredData\\sortedNames.csv'
csv2 = 'D:\\Businesses\\Automation Nation\\extractor\\codeForFilteredData\\sortedEmails.csv'

df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)

values1 = df1[['Names']]
values2 = df2[['Emails']]

join = pd.concat([values1, values2], axis=1)

join.to_csv('D:\\Businesses\\Automation Nation\\extractor\\codeForFilteredData\\output.csv')


filtered_df = join[join['Emails'].str.contains('@', na=False)]

filtered_df.reset_index(drop=True, inplace=True)

filtered_df.to_csv('D:\\Businesses\\Automation Nation\\extractor\\codeForFilteredData\\resultt.csv')
