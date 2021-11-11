"""
Controller Server

- receives trade fill at random intervals
- payload from fill server:
    {
        'stock_ticker': '<1 of 10 stocks>',
        'price': '<random positive price>',
        'quantity': '<random quantity>'
    }

- receives random account splits from the aum server at 30 seconds intervals
- payload from the aum server:
    {
        'account1': '<random percentage>',
        'account2': '<random percentage>',
        'account3': '<random percentage>',
    }

- keep track of positions held by each account
- tries to divide stocks so that each account has an overall position that matches the split from AUM server

- send report to the position server at 10 seconds interval


"""
