import CurrencyEquations
print("Currently supports CAD USD EUR GBP AUD NZD")
CurrencyIn = input("Type the currency code for your local currency (in caps): ")
CurrencyOut = input("Type the currency code for your destinations currency (in caps): ")
if CurrencyIn == "CAD":
    if CurrencyOut == "USD":
        CurrencyEquations.cadusd()
    if CurrencyOut == "EUR":
        CurrencyEquations.cadeur()
    if CurrencyOut == "GBP":
        CurrencyEquations.cadgbp()
    if CurrencyOut == "AUD":
        CurrencyEquations.cadaud()
    if CurrencyOut == "NZD":
        CurrencyEquations.cadnzd()

if CurrencyIn == "USD":
    if CurrencyOut == "CAD":
        CurrencyEquations.usdcad()
    if CurrencyOut == "EUR":
        CurrencyEquations.usdeur()
    if CurrencyOut == "GBP":
        CurrencyEquations.usdgbp()
    if CurrencyOut == "AUD":
        CurrencyEquations.usdaud()
    if CurrencyOut == "NZD":
        CurrencyEquations.usdnzd()

if CurrencyIn == "EUR":
    if CurrencyOut == "USD":
        CurrencyEquations.eurusd()
    if CurrencyOut == "CAD":
        CurrencyEquations.eurcad()
    if CurrencyOut == "GBP":
        CurrencyEquations.eurgbp()
    if CurrencyOut == "AUD":
        CurrencyEquations.euraud()
    if CurrencyOut == "NZD":
        CurrencyEquations.eurnzd()

if CurrencyIn == "GBP":
    if CurrencyOut == "USD":
        CurrencyEquations.gbpusd()
    if CurrencyOut == "EUR":
        CurrencyEquations.gbpeur()
    if CurrencyOut == "CAD":
        CurrencyEquations.gbpcad()
    if CurrencyOut == "AUD":
        CurrencyEquations.gbpaud()
    if CurrencyOut == "NZD":
        CurrencyEquations.gbpnzd()

if CurrencyIn == "AUD":
    if CurrencyOut == "USD":
        CurrencyEquations.audusd()
    if CurrencyOut == "EUR":
        CurrencyEquations.audeur()
    if CurrencyOut == "CAD":
        CurrencyEquations.audcad()
    if CurrencyOut == "GBP":
        CurrencyEquations.audgbp()
    if CurrencyOut == "NZD":
        CurrencyEquations.audnzd()

if CurrencyIn == "NZD":
    if CurrencyOut == "USD":
        CurrencyEquations.nzdusd()
    if CurrencyOut == "EUR":
        CurrencyEquations.nzdeur()
    if CurrencyOut == "CAD":
        CurrencyEquations.nzdcad()
    if CurrencyOut == "AUD":
        CurrencyEquations.nzdaud()
    if CurrencyOut == "GBP":
        CurrencyEquations.nzdgbp()
