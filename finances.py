def main() -> None:
    """Main program execution"""
    while True:
        try:
            monthly_income: float = float(input('Enter your monthly salary: '))
            tax_rate: float = float(input('Enter your tax rate: '))
            currency: str = input('Enter the currency type: ')
            expenses = get_expenses()
            break
        except ValueError:
            print('Please enter digits')
            continue
    try:
        calculate_finances(monthly_income, tax_rate, currency, expenses)
    except UnboundLocalError:
        print('Unable to calculate')


def calculate_finances(monthly_income: float, tax_rate: float, currency: str, expenses:dict) -> None:
    """Takes in values and performs math functions, returning amounts"""
    yearly_salary: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_net_income: float = yearly_salary - yearly_tax
    total_expenses = []
    total_expense = 0
    for expense in expenses:
        total_expenses.append(expenses[expense])
    for i in total_expenses:
        total_expense += i
    remaining_income = monthly_net_income - total_expense
    print('----------------')
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Monthly expenses: {currency}{total_expense:,.2f}')
    print(f'Remaining income: {currency}{remaining_income}')
    print(f'Yearly salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly Tax: {currency}{yearly_tax:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
    print('----------------')


def get_expenses() -> dict[str, float]:
    """Allows user to enter expense type and amount"""
    expenses = {}
    while True:
        expense_type:str = input('Enter expense (q to quit): ').lower()
        if expense_type == 'q':
            break
        try:
            expense_amount:float = float(input('Enter expense amount (q to quit): '))
        except ValueError or TypeError:
            break
        expenses[expense_type] = expense_amount
    return expenses


if __name__ == "__main__":
    main()