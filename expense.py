def main():
    """Executes main program"""
    while True:
        try:
            currency:str = input('Enter currency?: ')
            total_amount:float = float(input('Enter total amount of expense: '))
            number_of_people:int = int(input('Enter the total amount of people: '))
            if number_of_people < 1:
                raise ValueError('Number of people must be greater than one.')
            split_even:str = input('Is the bill split evenly?: ').lower()
            if split_even == 'y' or split_even == 'yes':
                calculate_even_split(total_amount, number_of_people, currency)
                break
            elif split_even == 'n' or split_even == 'no':
                percents = []
                for i in range(0, number_of_people):
                    percent:float = float(input(f'Enter percent for {i+1}: '))
                    percents.append(percent)
                calculate_uneven_split(total_amount, number_of_people, currency, percents)
                break
        except ValueError as e:
            print(f'Error: {e}')


def calculate_even_split(total_amount: float, number_of_people:int, currency:str) -> None:
    """Calculates even shares based on number of people"""
    share_per_person: float = total_amount / number_of_people
    print(f' Total expense: {currency}{total_amount:,.2f}')
    print(f'Number of people: {number_of_people}')
    print(f'Each person should pay: {currency}{share_per_person:,.2f}')


def calculate_uneven_split(total_amount: float, number_of_people:int, currency:str, percents:list) -> None:
    """Calculates amount per person based on individual precent values"""
    share_per_person:list = []
    for percent in percents:
        amount = total_amount * (percent/100)
        amount = str(f'{currency}{amount}')
        percent = str(f'{percent}%')
        share_per_person.append((percent, amount))
    print(f' Total expense: {currency}{total_amount:,.2f}')
    print(f'Number of people: {number_of_people}')
    print(f'Each person should pay: ')
    for percent, amount in share_per_person: print(f'{percent} = {amount}')


if __name__ == "__main__":
    main()