import pandas as pd
'''
df = pd.read_csv("https://raw.githubusercontent.com/lauradiosan/AI-2019-2020/master/exam/1/homeData.csv")


max_zipcode= df.loc[df.price == df.price.max(),"zipcode"].values[0]
print(df.loc[df.zipcode==max_zipcode,"zipcode"].median())
'''
'''
df = pd.read_csv("https://raw.githubusercontent.com/lauradiosan/AI-2019-2020/master/exam/2/homeData.csv")


medium_room= df.loc[:,"bedrooms"].median()
print(medium_room)
print(df.loc[df.bedrooms>medium_room,"sqft_living"].max())
'''
'''
df = pd.read_csv("https://raw.githubusercontent.com/lauradiosan/AI-2019-2020/master/exam/3/persons.csv")

gr_femei=df.loc[df.sex=='female',"weight"].median()
gr_barbati= df.loc[df.sex=='male',"weight"].median()
print(gr_barbati)
print(gr_femei)
if(gr_femei>gr_barbati):
    print("femei")
else:
    print("barbati")

    femaleTshirts, maleTshirts
'''
'''
df = pd.read_csv("https://raw.githubusercontent.com/lauradiosan/AI-2019-2020/master/exam/4/tshirts.csv")

gr_femei = df.loc[:, "femaleTshirts"].sum()
gr_barbati = df.loc[:,"maleTshirts"].sum()
print(gr_barbati)
print(gr_femei)
if (gr_femei > gr_barbati):
    print("femei")
else:
    print("barbati")
    
    '''

df = pd.read_csv("https://raw.githubusercontent.com/lauradiosan/AI-2019-2020/master/exam/5/wine.csv")

dens_medium = df.loc[df.alcohol>df.alcohol.median(), "density"].median()
print(dens_medium)

from cmath import sqrt

import numpy

realOutputs = [(1, 2, 3, 4), (11, 4, 7, 9), (5, 21, 3, 7), (89, 74, 23, 1), (6, 2, 4, 3)]
computedOutputs = [(1.4, 3, 2, 7), (10, 4.33, 2, 8.5), (4.8, 21.2, 2.9, 7.1), (90, 73, 22.9, -3), (5.56, -0.5, 3, 2.1)]


def myPredictioError():
    L1 = sum(abs(distance(ro, co)) for ro, co in zip(realOutputs, computedOutputs)) / len(realOutputs)
    L2 = sqrt(sum(distance(ro, co) ** 2 for ro, co in zip(realOutputs, computedOutputs)) / len(realOutputs))

    print("MyPredictionError: ")
    print("\tMean Absolute Error L1 = " + str(L1))
    print("\tRoot Mean Square Error L2 = " + str(L2))


def distance(a, b):
    summ = 0
    for i in range(len(a)):
        summ += (a[i] - b[i]) ** 2
    return sqrt(summ)


myPredictioError()