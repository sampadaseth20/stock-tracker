import streamlit as st
import yfinance as yf
from stock_fetcher import get_stock_info
from pros_cons import analyze_stock
from explainer import explain_stock

st.title("Stock Explainer Agent")

ticker1 = st.text_input("Enter first stock ticker", "AAPL")
ticker2 = st.text_input("Enter second stock ticker", "GOOGL")

if st.button("Compare Stocks"):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Analysis: {ticker1}")

        data1 = get_stock_info(ticker1)
        pros1, cons1 = analyze_stock(data1)
        result1 = explain_stock(data1, pros1, cons1)

        st.markdown(result1)

        stock1 = yf.Ticker(ticker1)
        hist1 = stock1.history(period="6mo")
        st.line_chart(hist1["Close"])

    with col2:
        st.subheader(f"Analysis: {ticker2}")

        data2 = get_stock_info(ticker2)
        pros2, cons2 = analyze_stock(data2)
        result2 = explain_stock(data2, pros2, cons2)

        st.markdown(result2)

        stock2 = yf.Ticker(ticker2)
        hist2 = stock2.history(period="6mo")
        st.line_chart(hist2["Close"])