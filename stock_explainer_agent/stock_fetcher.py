import yfinance as yf

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "market_cap": info.get("marketCap"),
        "current_price": info.get("currentPrice"),
        "pe_ratio": info.get("trailingPE"),
        "summary": info.get("longBusinessSummary")
    }
