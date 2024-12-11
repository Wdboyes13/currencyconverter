import yfinance
def cadusd():
    ticker = yfinance.Ticker('CAD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to USD: ")
    amountfl = float(amount)
    print(amount, "CAD is equal to about", amountfl*ratefl, "USD")

def cadeur():
    ticker = yfinance.Ticker('EURCAD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to EUR: ")
    amountfl = float(amount)
    print(amount, "CAD is equal to about", amountfl*ratefl, "EUR")

def cadgbp():
    ticker = yfinance.Ticker('GBPCAD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to GBP: ")
    amountfl = float(amount)
    print(amount, "CAD is equal to about", amountfl*ratefl, "GBP")
def cadnzd():
    ticker = yfinance.Ticker('NZDCAD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to NZD: ")
    amountfl = float(amount)
    print(amount, "CAD is equal to about", amountfl*ratefl, "NZD")

def cadaud():
    ticker = yfinance.Ticker('AUDCAD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to AUD: ")
    amountfl = float(amount)
    print(amount, "CAD is equal to about", amountfl*ratefl, "AUD")

def usdcad():
    ticker = yfinance.Ticker('CADUSD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to CAD: ")
    amountfl = float(amount)
    print(amount, "USD is equal to about", amountfl*ratefl, "CAD")

def usdeur():
    ticker = yfinance.Ticker('EURUSD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to EUR: ")
    amountfl = float(amount)
    print(amount, "USD is equal to about", amountfl*ratefl, "EUR")

def usdgbp():
    ticker = yfinance.Ticker('GBPUSD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to GBP: ")
    amountfl = float(amount)
    print(amount, "USD is equal to about", amountfl*ratefl, "GBP")

def usdaud():
    ticker = yfinance.Ticker('AUDUSD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to AUD: ")
    amountfl = float(amount)
    print(amount, "USD is equal to about", amountfl*ratefl, "AUD")

def usdnzd():
    ticker = yfinance.Ticker('NZDUSD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to NZD: ")
    amountfl = float(amount)
    print(amount, "USD is equal to about", amountfl*ratefl, "NZD")

def gbpcad():
    ticker = yfinance.Ticker('CADGBP=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to CAD: ")
    amountfl = float(amount)
    print(amount, "GBP is equal to about", amountfl*ratefl, "CAD")

def gbpeur():
    ticker = yfinance.Ticker('EURGBP=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to EUR: ")
    amountfl = float(amount)
    print(amount, "GBP is equal to about", amountfl*ratefl, "EUR")

def gbpusd():
    ticker = yfinance.Ticker('USDGBP=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to USD: ")
    amountfl = float(amount)
    print(amount, "GBP is equal to about", amountfl*ratefl, "USD")

def gbpaud():
    ticker = yfinance.Ticker('AUDGBP=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to AUD: ")
    amountfl = float(amount)
    print(amount, "GBP is equal to about", amountfl*ratefl, "AUD")

def gbpnzd():
    ticker = yfinance.Ticker('NZDGBP=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to NZD: ")
    amountfl = float(amount)
    print(amount, "GBP is equal to about", amountfl*ratefl, "NZD")

def eurcad():
    ticker = yfinance.Ticker('CADEUR=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to CAD: ")
    amountfl = float(amount)
    print(amount, "EUR is equal to about", amountfl*ratefl, "CAD")

def eurgbp():
    ticker = yfinance.Ticker('GBPEUR=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to GBP: ")
    amountfl = float(amount)
    print(amount, "EUR is equal to about", amountfl*ratefl, "GBP")

def eurusd():
    ticker = yfinance.Ticker('USDEUR=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to USD: ")
    amountfl = float(amount)
    print(amount, "EUR is equal to about", amountfl*ratefl, "USD")

def euraud():
    ticker = yfinance.Ticker('AUDEUR=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to AUD: ")
    amountfl = float(amount)
    print(amount, "EUR is equal to about", amountfl*ratefl, "AUD")

def eurnzd():
    ticker = yfinance.Ticker('NZDEUR=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to NZD: ")
    amountfl = float(amount)
    print(amount, "EUR is equal to about", amountfl*ratefl, "NZD")

def audcad():
    ticker = yfinance.Ticker('CADAUD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to CAD: ")
    amountfl = float(amount)
    print(amount, "AUD is equal to about", amountfl*ratefl, "CAD")

def audgbp():
    ticker = yfinance.Ticker('GBPAUD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to GBP: ")
    amountfl = float(amount)
    print(amount, "AUD is equal to about", amountfl*ratefl, "GBP")

def audusd():
    ticker = yfinance.Ticker('USDAUD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to USD: ")
    amountfl = float(amount)
    print(amount, "AUD is equal to about", amountfl*ratefl, "USD")

def audeur():
    ticker = yfinance.Ticker('EURAUD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to EUR: ")
    amountfl = float(amount)
    print(amount, "AUD is equal to about", amountfl*ratefl, "EUR")

def audnzd():
    ticker = yfinance.Ticker('NZDAUD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to NZD: ")
    amountfl = float(amount)
    print(amount, "AUD is equal to about", amountfl*ratefl, "NZD")

def nzdcad():
    ticker = yfinance.Ticker('CADNZD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to CAD: ")
    amountfl = float(amount)
    print(amount, "NZD is equal to about", amountfl*ratefl, "CAD")

def nzdgbp():
    ticker = yfinance.Ticker('GBPNZD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to GBP: ")
    amountfl = float(amount)
    print(amount, "NZD is equal to about", amountfl*ratefl, "GBP")

def nzdusd():
    ticker = yfinance.Ticker('USDNZD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to USD: ")
    amountfl = float(amount)
    print(amount, "NZD is equal to about", amountfl*ratefl, "USD")

def nzdeur():
    ticker = yfinance.Ticker('EURNZD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to EUR: ")
    amountfl = float(amount)
    print(amount, "NZD is equal to about", amountfl*ratefl, "EUR")

def nzdaud():
    ticker = yfinance.Ticker('AUDNZD=X').info
    conrate = ticker['open']
    ratefl = float(conrate)
    amount = input("Type the amount you want to convert to AUD: ")
    amountfl = float(amount)
    print(amount, "NZD is equal to about", amountfl*ratefl, "AUD")
