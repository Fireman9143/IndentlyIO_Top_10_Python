import json
import requests

response = requests.get(' http://www.floatrates.com/daily/usd.json')#based on USD, free and no subscription
current_rates = response.json()


"""def load_rates(json_file:str) -> dict[str, dict[str, str | float]]:
    with open(json_file, 'r') as file:
        return json.load(file)"""#Not needed for URL requests, only for loading local JSON
    
def convert(amount:float, base:str, to:str, rates: dict[str, dict]) -> float:
    """Compares user inputs and performs currency conversion"""
    base:str = base.lower()
    to:str = to.lower()

    if base != "usd":
        from_rates:dict|None = rates.get(base)
    else:
        from_rates = 1
    if to != "usd":
        to_rates:dict|None = rates.get(to)
    else:
        to_rates = 1

    if base != 'usd' and to != 'usd' and from_rates is not None and to_rates is not None:
        return amount * (to_rates['rate'] / from_rates['rate'])
    elif base == "usd":
        return amount * (to_rates['rate'] / from_rates)
    elif to == "usd":
        return amount * (to_rates / from_rates['rate'])
    else:
        print('Rates are not available')
        return None

def main():
    """Gets values from user and runs conversion.  Displays results."""
    rates:dict[str,dict] = current_rates
    try:
        base:str = input('Enter code for "from" base currency: ')
        to:str = input('Enter code for "to" currency: ')
        amount:int = int(input('Enter the number of base currency to convert: '))
        result:float = convert(amount, base, to, rates=rates)
        if result is not None:
            print(f'{base} to {to} is {result}')
        else:
            raise ValueError
    except ValueError:
        print(f'Invalid input, {base}, {to}')
        print('Valid currency codes: ')
        for i in rates: 
            print(f"{rates[i].get('name')} : {i}")
    

if __name__ == "__main__":
    main()