import argparse
import yfinance

def main():
    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description="Currency Converter using Current Stocks")

    # Add arguments for local currency, destination currency, and amount
    parser.add_argument('local_currency', type=str, help="The code for your local currency (e.g., USD)")
    parser.add_argument('destination_currency', type=str, help="The code for your destination currency (e.g., EUR)")
    parser.add_argument('amount', type=float, help="The amount you want to convert")

    # Parse the arguments
    args = parser.parse_args()

    # Convert currency codes to uppercase for consistency
    local_currency = args.local_currency.strip().upper()
    destination_currency = args.destination_currency.strip().upper()
    amount = args.amount

    try:
        # Fetch the exchange rate using yfinance
        ticker = yfinance.Ticker(f"{local_currency}{destination_currency}=X").info
        
        # Extract the rate from the 'open' field in ticker info
        ratefl = float(ticker['open'])

        # Perform the conversion
        converted_amount = amount * ratefl

        # Output the conversion result
        print(f"{amount} {local_currency} is equal to about {converted_amount:.2f} {destination_currency}")

    except KeyError:
        print("Error: Could not retrieve exchange rate for the given currencies.")
    except ValueError:
        print("Error: Please enter valid numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
