#!/usr/bin/python3

import requests
import time
import yfinance as yf


def calculateStock(stocks, rate):

    # print('enter...')

    total = 0

    for stock in stocks:

        index = stock.find(":")
        stockSymbal = stock[:index]
        stockAmount = stock[index+1:]

        ticker = yf.Ticker(stockSymbal)

        currency = ticker.info["currency"]

        if currency == 'USD':
            total = total + \
                (float(ticker.info["regularMarketPrice"])
                 * int(stockAmount)) / float(rate)
        else:
            total = total + \
                (float(ticker.info["regularMarketPrice"]) * int(stockAmount))

    return total


def getUSDRate():

    url = "https://ca.finance.yahoo.com/quote/CADUSD=X?p=CADUSD=X"

    page = requests.get(url)
    pageContent = page.text

    index = pageContent.find("root.App.main =")
    endIndex = pageContent.find("(this));")

    x = pageContent[index + 6:endIndex]

    # print(x)
    s1 = "regularMarketPrice"
    index = x.find(s1)

    y = x[index:index + 150]
    anotherIndex = y.find("\"raw\"")
    pindex = y.find(",")

    # print(y)
    # print(y[anotherIndex + 6:pindex])

    rate = y[anotherIndex + 6:pindex]

    return rate


terryTF = ['TCEHY:10', 'AAPL:30', 'AMZN:3', 'MSFT:100', 'V:100', 'COST:45']
cathyTF = ['AMZN:1', 'COST:30', 'MSFT:40']
terrymarginstocks = ['WMT:40']


marginCashCAD = 306.7
marginCashUSD = 437.67

terryTFCashCAD = 839.62
terryTFCashUSD = 2711.25

cathyTFCashCAD = 262.61
cathyTFCashUDS = 27861.27

rate = getUSDRate()
print(rate)

print("margin-------------------")
marginTotal = calculateStock(terrymarginstocks, rate) + \
    marginCashCAD + marginCashUSD / float(rate)
# marginTotal = calculateStock(terrymarginstocks, 0.76) + marginCashCAD + marginCashUSD / 0.76

print(marginTotal)


print("TERRT -----------------")
terryTFTotal = calculateStock(terryTF, rate) + \
    terryTFCashCAD + terryTFCashUSD / float(rate)
print(terryTFTotal)
print("cathy TFSA-----------------")
cathyTFTotal = calculateStock(cathyTF, rate) + \
    cathyTFCashCAD + cathyTFCashUDS / float(rate)
print(cathyTFTotal)


terryRRSP = ['COST:5', 'GOOG:8', 'MA:13', 'TCEHY:11']
terryRRSPCashCAD = 1970.83
terryRRSPCashUSD = 19.23

terryRRSPTotal = calculateStock(
    terryRRSP, rate) + terryRRSPCashCAD + terryRRSPCashUSD / float(rate)
print("terryRRSP -------------")
print(terryRRSPTotal)

terryRESP = ['AMZN:7', 'GOOG:1', 'HD:4', 'MA:3', 'TCEHY:37', 'MSFT:9']
terryRESPCashCAD = 2177.77
terryRESPCashUSD = 0

terryRESPTotal = calculateStock(
    terryRESP, rate) + terryRESPCashCAD + terryRESPCashUSD / float(rate)
print("terryRESP ------------------")
print(terryRESPTotal)

cathyRRSP = ['BABA:4', 'COST:2', 'MSFT:8']
cathyRRSPCashCAD = 2830.23
cathyRRSPCashUSD = 1.29

cathyRRSPTotal = calculateStock(
    cathyRRSP, rate) + cathyRRSPCashCAD + cathyRRSPCashUSD / float(rate)
print("cathyRRSPTotal----------")
print(cathyRRSPTotal)


cathySRRSP = ['AMZN:2', 'BABA:8', 'COST:50',
              'GOOG:2', 'MSFT:41', 'SHOP:2', 'V:45']
cathySRRSPCashCAD = 2147.22
cathySRRSPCashUSD = 0

cathySRRSPTotal = calculateStock(
    cathySRRSP, rate) + cathySRRSPCashCAD + cathySRRSPCashUSD / float(rate)
print("cathySRRSPTotal----------")
print(cathySRRSPTotal)


print('---------------------------------------------------')
subTotal = marginTotal + terryTFTotal + cathyTFTotal

print(subTotal)
print('---------------------------------------------------')
print(terryRRSPTotal +
      terryRESPTotal + cathyRRSPTotal + cathySRRSPTotal)

print('---------------------------------------------------')
print(marginTotal + terryTFTotal + cathyTFTotal + terryRRSPTotal +
      terryRESPTotal + cathyRRSPTotal + cathySRRSPTotal)


print('---------------------------------------------------')
