import pandas as pd
import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar")
soup=BeautifulSoup(response.content,"html.parser")
#fetching data from website
names=soup.find_all("span",class_="a-size-base-plus a-color-base a-text-normal")
prices=soup.find_all("span",class_="a-price-whole")
ratings=soup.find_all("span",class_="a-icon-alt")
seller_info=soup.find("span",class_="a-size-small tabular-buybox-text-message")
links=soup.find_all("a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")#links and iamges are additional informnation
images=soup.find_all("img",class_="s-image")
#craete a empty list for appending all values
productname=[]
productprice=[]
productratings=[]
sellerinformation=[]
productlink=[]
productimage=[]
for i in names:#Here we can use slicing like[0:10] if we want only some particular data
    d=i.get_text()
    productname.append(d)
print(productname) 
for i in prices:
    d=i.get_text()
    productprice.append(d)
print(productprice)
for i in ratings[0:24]:
    d=i.get_text()
    productratings.append(d)
print(productratings) 
for i in links:
    d="https://www.amazon.in/"+i["href"]
    productlink.append(d)
print(productlink) 
for i in images:
    d=i["src"]
    productimage.append(d)
print(productimage) 
df=pd.DataFrame()#row columns
df["productname"]=productname
df["productprice"]=productprice
df["productrating"]=productratings
df["productlink"]=productlink
df["productimages"]=productimage





df.to_csv("amazon.csv")