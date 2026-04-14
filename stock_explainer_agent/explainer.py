def explain_stock(data, pros, cons):
    verdict = "Neutral"

    if len(pros) > len(cons):
        verdict = "Good for long-term beginners"
    elif len(cons) > len(pros):
        verdict = "Higher risk stock"

    text = f"""
Stock: {data['name']}
Sector: {data['sector']}
Price: {data['current_price']}

About:
{data['summary']}

Pros:
"""

    for p in pros:
        text += f"- {p}\n"

    text += "\nCons:\n"

    for c in cons:
        text += f"- {c}\n"

    text += f"\nFinal Verdict: {verdict}"

    return text