"""
    Fill Server

    - sends trade fills at random intervals
    - uses only 10 stocks that are available
    - payload for the trade fill:
        {
            "stock_ticker": <random stock>,
            "price": <random positive price>,
            "quantity": <random quantity>
        }
"""
