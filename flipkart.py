import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2,12):
    url = "https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.price_range.from%3D10000&p%5B%5D=facets.price_range.to%3D20000&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlVuZGVyIOKCuTEwLDAwMCB0byDigrkyMCwwMDAwIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=65.productCard.PMU_V2_17&page="+str(i)

    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_ = "_4rR01T")

    for i in names:
        name = i.text
        Product_name.append(name)

    # print(Product_name)

    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")

    for i in prices:
        name = i.text
        Prices.append(name)

    # print(Prices)

    desc = box.find_all("ul", class_ = "_1xgFaf")

    for i in desc:
        name = i.text
        Description.append(name)

    # print(Description)

    reviews = box.find_all("div", class_ = "_3LWZlK")

    for i in reviews:
        name = i.text
        Reviews.append(name)

    # print(Reviews)

dataframe = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Description": Description, "Reviews": Reviews})
# print(dataframe)

dataframe.to_csv("flipkart_mobile_price_data.csv")












    # print(soup)

    # while True:
    # np = soup.find("a", class_ = "_1LKTO3").get("href")
    # cnp = "https://www.flipkart.com"+np
    # print(cnp)

    # url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text,"lxml")
