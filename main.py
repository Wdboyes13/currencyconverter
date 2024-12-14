import yfinance
print("Enter currency codes in all caps")
inp = input("Enter the code for your local currency: ")
out = input("Enter the code for your destination currency: ")

def main(inp, out):
    ticker = yfinance.Ticker(out + inp + "=X").info
    ratefl = float(ticker['open'])
    amountfl = float(input("Type the amount you want to convert: " ))
    print(amountfl, inp, "is equal to about", amountfl*ratefl, out) 

main(inp, out)
