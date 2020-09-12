import pandas as pd
from scipy.stats import pearsonr
df = pd.read_csv("fifa.csv")
loc = input("Enter the location : ")
Locations = []
l = list(set(df['Place']))
twe = list(df['Tweet'])
ss=list(df['Senti'])
for i in l:
    Locations.append(i.lower())
if loc.lower() not in Locations:
    print("Location not found . Please select location only from ",Locations)
else:
    ll = []
    lo = list(df['Place'])
    for i in lo:
        ll.append(i.lower())
    count = 0
    start = ll.index(loc.lower())
    for i in ll:
        if i.lower() ==loc.lower():
            count+=1
    end = count+start
    ll = ll[start:end]
    twe = twe[start:end]
    ss = ss[start:end]
    print(ss)
    li = [ ]
    for i in range(len(ll)):
        li.append(twe[i]+','+ll[i]+','+ss[i]+'\n')
    file = open("fifafile1.csv",'w')
    file.write("Tweet,Place,Senti\n")
    for i in li:
        file.write(i)
    apple = []
    banana = []
    file = open('fifafile1.csv',encoding='utf8')
    df = pd.read_csv(file)
    list1 = df['Tweet'].astype('category').cat.codes
    list2 = df['Senti'].astype('category').cat.codes
    corr, _ = pearsonr(list1, list2)

    print('prarsons correlation: %.3f' % corr)
