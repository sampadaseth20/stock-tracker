def analyze_stock(data):
    pros = []
    cons = []

    pe = data.get("pe_ratio")
    market_cap = data.get("market_cap")
    sector = data.get("sector")

    # Pros
    if market_cap and market_cap > 100000000000:
        pros.append("Large and established company")

    if pe and pe < 30:
        pros.append("Valuation looks reasonable")

    if sector == "Technology":
        pros.append("Strong growth potential sector")

    # Cons
    if pe and pe > 40:
        cons.append("Stock may be overvalued")

    if not pe:
        cons.append("P/E ratio data unavailable")

    return pros, cons