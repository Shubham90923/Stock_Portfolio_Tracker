# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 125,
    "MSFT": 280
}

# Initialize portfolio
portfolio = {}
total_investment = 0

print("Welcome to the Stock Portfolio Tracker!")
print("Enter your stock holdings. Type 'done' to finish.\n")

# User input loop
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not in price list. Please enter a valid symbol.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number for quantity.")

# Calculate total investment
print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Option to save to file
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ")
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price per Share,Total Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock},{qty},{price},{value}\n")
        file.write(f"\nTotal Investment Value,,,{total_investment}\n")
    print(f"Portfolio saved to {filename}.")