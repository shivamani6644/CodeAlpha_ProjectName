# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 170
}

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

total_investment = 0

n = int(input("\nHow many different stocks do you own? "))

for i in range(n):
    print(f"\nStock {i + 1}")

    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Price per share: ${stock_prices[stock_name]}")
        print(f"Investment Value: ${investment}")

    else:
        print("Stock not found!")

print("\n===================================")
print(f"Total Investment Value = ${total_investment}")
print("===================================")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total_investment}")

print("\nResult saved to portfolio.txt")