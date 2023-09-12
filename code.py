import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filepath=("C:\\Users\\lanaa\\Downloads\\unique_devices_per_domain_daily-2018-09-21\\unique_devices_per_domain_daily-2018-09-21.txt")
data=pd.read_csv(filepath,sep="\t")
data.columns=["Wikimedia_Projects","The_Unique_Underestimate","The_Estimate","The_Offset"]
count=data.Wikimedia_Projects.str.split(".",expand=True)[0]
counts=data.Wikimedia_Projects.str.split(".",expand=True)[1]
data.loc[:,"ex"]=counts
data.loc[:,"Language"]=count
grouped=data.groupby(["Language"])
estimate=(grouped.The_Estimate)
lang_s=[]
est_s=[]
for i in data.Language:
    if str(i).startswith ("s"):
        lang_s.append(i)
df=pd.Series(lang_s).unique().tolist()
for i in df:
    s=grouped.get_group(i).The_Estimate.sum()
    est_s.append(s)
y=est_s
x=df
fig, ax = plt.subplots()
ax.stackplot(x,y,color=['yellow'])
plt.title("The Estimate Of Project That Language Starts with 's'")
plt.xlabel("Language")
plt.ylabel("The Estimate")
plt.show()


filepath=("C:\\Users\\lanaa\\Downloads\\unique_devices_per_project_family_daily-2021-05-14\\unique_devices_per_project_family_daily-2021-05-14.txt")
data1=pd.read_csv(filepath,sep="\t",header=None)
data1.columns=["Wikimedia_Projects","The_Unique_Underestimate","The_Estimate","The_Offset"]
grouped=data1.groupby(["Wikimedia_Projects"])
g=grouped.The_Estimate.sum()
filepath=("C:\\Users\\lanaa\\Downloads\\unique_devices_per_project_family_daily-2019-05-14\\unique_devices_per_project_family_daily-2019-05-14.txt")
data2=pd.read_csv(filepath,sep="\t",header=None)
data2.columns=["Wikimedia_Projects","The_Unique_Underestimate","The_Estimate","The_Offset"]
grouped1=data2.groupby(["Wikimedia_Projects"])
g1=grouped1.The_Estimate.sum()

filepath=("C:\\Users\\lanaa\\Downloads\\unique_devices_per_project_family_daily-2020-05-14\\unique_devices_per_project_family_daily-2020-05-14.txt")
data3=pd.read_csv(filepath,sep="\t",header=None)
data3.columns=["Wikimedia_Projects","The_Unique_Underestimate","The_Estimate","The_Offset"]
grouped2=data3.groupby(["Wikimedia_Projects"])
g2=grouped2.The_Estimate.sum()
list=g+g1+g2
projects=["mediawiki","wikibooks","wikidata","wikimediafoundation","wikinews","wikipedia","wikiquote","wikisource","wikiversity","wikivoyage","wiktionary"]
estimate=list.tolist()
width = 0.20
fig, ax = plt.subplots()
ax.bar(projects, estimate, width,color=["purple","black","red","green","cyan","gray","pink","gold","silver","blue","orange"])
plt.title("The Estimate Of The Projects In '15 May' Of Different Years")
plt.ylabel("Estimate")
plt.xlabel("Projects")
plt.show()
