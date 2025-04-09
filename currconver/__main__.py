import argparse
import requests
import os
def main():

    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description="Currency Converter using Open Exchange Rates")

    # Add arguments for local currency, destination currency, and amount
    parser.add_argument('opp', type=str, choices=['AUTH', 'CONV'], help="Choose AUTH to get an API key or CONV to convert currencies.")

    # Add arguments for local currency, destination currency, and amount, but make them optional
    parser.add_argument('local_currency', type=str, nargs='?', help="The code for your local currency (e.g., USD)")
    parser.add_argument('destination_currency', type=str, nargs='?', help="The code for your destination currency (e.g., EUR)")
    parser.add_argument('amount', type=float, nargs='?', help="The amount you want to convert")

    # Parse the arguments
    args = parser.parse_args()
    opp = args.opp
    if opp=="AUTH":
        with open('key.txt', 'w') as file:
            print("Please get an API key from Open Exchange Rates")
            print("https://openexchangerates.org/signup/free")
            key = input("Enter API Key: ")
            file.write(key)
    if opp=="CONV":
        if not args.local_currency or not args.destination_currency or not args.amount:
            print("Error: Missing required arguments for conversion.")
            print("Usage: python3 -m currconver CONV <local_currency> <destination_currency> <amount>")
            return
        # Convert currency codes to uppercase for consistency
        if os.path.exists('key.txt'):
            with open('key.txt') as file:
                API_KEY=file.read().strip()
        else:
            print("No API Key Found")
            print("Please Authorize with python3 -m currconver AUTH")
        local_currency = args.local_currency.strip().upper()
        destination_currency = args.destination_currency.strip().upper()
        amount = args.amount

        # Build the URL for the Open Exchange Rates API
        url = f'https://openexchangerates.org/api/latest.json?app_id={API_KEY}&symbols={local_currency},{destination_currency}'

        try:
            # Fetch the exchange rates
            response = requests.get(url)
            data = response.json()

            # Check if the response contains exchange rates for the requested currencies
            if 'rates' in data and local_currency in data['rates'] and destination_currency in data['rates']:
                local_rate = data['rates'][local_currency]
                destination_rate = data['rates'][destination_currency]

                # Convert the local currency to USD (since Open Exchange Rates provides rates with USD as base)
                amount_in_usd = amount / local_rate
                converted_amount = amount_in_usd * destination_rate

                # Output the conversion result
                print(f"{amount} {local_currency} is equal to about {converted_amount:.2f} {destination_currency}")
            else:
                print("Error: Could not retrieve exchange rate for the given currencies.")

        except requests.exceptions.RequestException as e:
            print(f"Error: There was a problem with the network request - {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()