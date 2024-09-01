"""
Created on Mon Aug 30 22:57:11 2021

@author: D99003734
"""
from datetime import datetime
import csv
import json
import numpy
import matplotlib.pyplot as plt

from stock_class import Stock, DailyData
from account_class import Traditional, Robo

#from account_class import  Traditional, Robo


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
    print('\nDelete Stock ---')
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

    print(f'*** current_stock:\n{current_stock} ')

    if found:
        print("Ready to add data for: ", symbol)
        print("Enter Data Separated by Commas - Do Not use Spaces")
        print("Enter a Blank Line to Quit")
        print("Enter Date,Price,Volume")
        print("Example: 8/28/20,47.85,10550")

        data = input("\nEnter Date,Price,Volume: ")

        while data != "":
            date, price, volume = data.split(",")
            print()
            print(date, price, volume)
            print()
            daily_data = DailyData(date, float(price), float(volume))
            current_stock.add_data(daily_data)
            data = input("Enter Date,Price,Volume: ")
        print("\nDate Entry Complete")
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


# Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    list = [stock.symbol for stock in stock_list]
    print('\nAdd historical data to a stock in the stock list ---')
    print(f"Stock List: {list}\n")
    symbol = input('Enter stock symbol: ').upper()
    filename = input('Enter the fillname: ')
    print()

    for stock in stock_list:
        if stock.symbol == symbol:
            with open(filename, newline='') as stockdata:
                datareader = csv.reader(stockdata)
                next(datareader)
                for row in datareader:
                    daily_data = DailyData(str(row[0]), float(row[4]), float(row[6]))
                    # print(f'daily_data: {daily_data}')
                    stock.add_data(daily_data)
        display_report(stock_list)

    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        display_stock_chart(stock_list, current_stock.symbol)
    else:
        print("Symbol not found")
        _ = input("Press enter ro continue")
    

# Display Report
def display_report(stock_list):
    print('\nStock Report --- ')

    for stock in stock_list:
        print(f'Report for {stock.symbol} {stock.name}')
        print(f'Shares: {stock.shares}')
        count = 0
        price_total = 0
        volumn_total = 0
        lowPrice = 999999.99
        highPrice = 0.0
        lowVolume = 999999999999
        highVolume = 0

        for daily_data in stock.DataList:

            count += 1
            price_total += daily_data.close
            volumn_total += daily_data.volume

            if daily_data.close  < lowPrice:   lowPrice   = daily_data.close
            if daily_data.close  > highPrice:  highPrice  = daily_data.close
            if daily_data.volume < lowVolume:  lowVolume  = daily_data.volume
            if daily_data.volume > highVolume: highVolume = daily_data.volume
            
            priceChange = highPrice - lowPrice
            print(daily_data.date, daily_data.close, daily_data.volume)
        
        if count > 0:
            print("\nSummary ---")
            print(f"Low Price: ${lowPrice:,.2f}")
            print(f"High Price: ${highPrice:,.2f}")
            print(f"Average Price: ${price_total/count:,.2f}")
            print(f"Low Volume: ${lowVolume}")
            print(f"High Volumn: ${highVolume}")
            print(f"Average Volumn: ${volumn_total/count}")
            print(f"Change in price: ${priceChange}")
            print(f"Profit/Loss: ${priceChange*stock.shares}")
        else:
            print('**** No daily history')
        print('\n\n\n')
    print('--- report complete ---')
    _ = input('Press enter to continue')

def display_stock_chart(stock_list, symbol):
    date = []
    price = []
    volume = []
    company = ''

    for stock in stock_list:
        if stock.symbol == symbol:
            company = stock.name
            for dailyData in stock.DataList:
                date.append(dailyData.date)
                price.append(dailyData.close)
                volume.append(dailyData.volume)

    print(f'''
    date = {date}
    price = {price}
    volume = {volume}
    ''')

    plt.plot(date, price)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(company)
    plt.show()


def display_chart(stock_list):
    print('\nStock Chart ---')
    print(f"Stock List: { [stock.symbol for stock in stock_list] }")
    symbol = input('Pick stock for a chart: ').upper()
    found = False

    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found:
        display_stock_chart(stock_list, current_stock.symbol)
    else:
        print(f"Error: {symbol} not found!")
        _ = input('Press enter to continue ***')


def main_menu(stock_list):
    option = ""
    while True:
        print("\nStock Analyzer ---\n")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List Stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program\n")
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
