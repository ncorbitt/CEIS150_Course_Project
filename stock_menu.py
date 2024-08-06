"""
Created on Mon Aug 30 22:57:11 2021

@author: D99003734
"""
from datetime import datetime
import csv
import json
import matplotlib.pyplot as plt

from stock_class import Stock, DailyData
from account_class import Traditional, Robo

#from account_class import  Traditional, Robo
import matplotlib.pyplot as plt


def add_stock(stock_list):
    print('\nAdd Stock ---')
    symbol = input('Enter stock symbol: ').upper()
    name = input('Enter company name: ').upper()
    shares = float(input('Enter number of shares: '))
    new_stock = Stock(symbol, name, shares)
    stock_list.append(new_stock)
    print('Stock added.')
    input('Press enter to continue ***')


# Remove stock and all daily data
def delete_stock(stock_list):
    print('\nDelete stock ---')
    print(f"Stock List: { [stock.symbol for stock in stock_list] }")
    symbol = input('Which stock do you want to delete?: ').upper()
    found = False
    i = 0
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            stock_list.pop(i)
        i += 1
    if found:
        print(f'Stock->{symbol} deleted.')
    else:
        print('Stock not found.')
    input('Press enter to continue *** ')


def buy_stock(stock_list):
    print('\nBuy Shares ---')
    print(f"Stock List: {[stock.symbol for stock in stock_list]}")
    symbol = input('Which stock do you want to buy?: ').upper()
    shares = float(input('How many shares do you want to buy?: '))

    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            stock.buy(shares)
            print('Shares added.')
            break

    if found:
        print(f"Bought/Sold {shares} of {symbol}")
    else:
        print(f"Error: {symbol} not found!")

    input("Press enter to continue *** ")


# Sell stocks
def sell_stock(stock_list):
    list = [stock.symbol for stock in stock_list]
    print('Sell Shares ---')
    print(f"Stock List: {list}")
    symbol = input('Which stock do you want to sell?: ').upper()
    shares = float(input('How many shares do you want to sell?: '))

    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            stock.buy(shares)
            print('Shares added.')
            break
    if found:
        print(f"Bought/Sold {shares} of {symbol}")
    else:
        print(f"Error: {symbol} not found!")

    input("Press enter to continue *** ")


# List stocks being tracked
def list_stocks(stock_list):
    print("\nStock List ---")
    print(f"{'SYMBOL':10} {'NAME':30} {'SHARES':30}")
    print(
        f"{'-'*len('symbol'):10} {'-'*len('name'):30} {'-'*len('shares'):30}")
    for stock in stock_list:
        print(f'{stock.symbol:10} {stock.name:30} {stock.shares:<30}')
    input('\nPress enter to continue')


# Add Daily Stock Data
def add_stock_data(stock_list):
    print("\nAdd Daily Stock Data ----")
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol, " ", end="")
    print("]")
    symbol = input("Which stock do you want to use?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        print("Ready to add data for: ", symbol)
        print("Enter Data Separated by Commas - Do Not use Spaces")
        print("Enter a Blank Line to Quit")
        print("Enter Date,Price,Volume")
        print("Example: 8/28/20,47.85,10550")
        data = input("Enter Date,Price,Volume: ")
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(date, float(price), float(volume))

            current_stock.add_data(daily_data)
            data = input("Enter Date,Price,Volume: ")
        print("Date Entry Complete")
    else:
        print("Symbol Not Found ***")
    _ = input("Press Enter to Continue ***")


def investment_type(stock_list):
    print("\nInvestment Account ---")
    balance = float(input("What is your initial balance: "))
    number = input("What is your account number: ")
    acct = input("Do you want a Traditional (t) or Robo (r) account: ")

    if acct.lower() == "r":
        years = float(input("How many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ", robo_acct.investment_return())
        print("\n\n")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list = []
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [", end="")
            for stock in stock_list:
                print(stock.symbol, " ", end="")
            print("]")
            symbol = input(
                "Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol == "0":
                break
            shares = float(input("How many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
                if stock.symbol == symbol:
                    found = True
                    current_stock = stock
            if found:
                current_stock.shares += shares
                temp_list.append(current_stock)
                print("Bought ", shares, "of", symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)


# Function to create stock chart
def display_stock_chart(stock_list, symbol):
    print("This method is under construction")


# Display Chart
def display_chart(stock_list):
    print("This method is under construction")


# Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    print("This method is under construction")


# Display Report
def display_report(stock_list):
    print('Stock Report --- ')

    for stock in stock_list:
        print(f'Report for {stock.symbol} {stock.name}')
        print(f'Shares: {stock.shares}')
        count = 0
        price_total = 0
        volumn_total = 0
        lowPrice = 999999.99
        highPrice = 0.0
        lowVolumn = 999999999999
        highVolumn = 0.0
        startDate = datetime.strptime("12/31/2099", "%m/%d/%Y")
        endDate = datetime.strptime("1/1/1900", "%m/%d/%Y")
        for daily_data in stock.daily_data:
            count += 1
            price_total += daily_data.price
            volumn_total += daily_data.volume

            if daily_data.date < startDate:
                startDate = daily_data.date
            if daily_data.date > endDate:
                endDate = daily_data.date
            if daily_data.price < lowPrice:
                lowPrice = daily_data.price
            if daily_data.price > highPrice:
                highPrice = daily_data.price
            if daily_data.volume < lowVolumn:
                lowVolumn = daily_data.volume
            if daily_data.volume > highVolumn:
                highVolumn = daily_data.volume


def main_menu(stock_list):
    option = ""
    while True:
        print("Stock Analyzer ---")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List Stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option == "0":
            print("Goodbye")
            break

        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
            add_stock_data(stock_list)
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:

            print("Goodbye")


# Begin program
def main():
    stock_list = []
    main_menu(stock_list)


# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()
