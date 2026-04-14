from stock_fetcher import get_stock_info
from pros_cons import analyze_stock
from explainer import explain_stock

ticker = input("Enter stock ticker: ")

data = get_stock_info(ticker)
pros, cons = analyze_stock(data)

result = explain_stock(data, pros, cons)

print(result)