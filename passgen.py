import secrets
import string

class Password:
    def __init__(self, length:int = 12, uppercase:bool = True, symbols:bool = True) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        #Get characters from string module
        self.base_characters:str = string.ascii_lowercase + string.digits
       
        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation


    def generate(self) -> str:
        password:list[str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))

        return "".join(password)
    

    def strength_check(self, password) -> str:
        """Checks for uppercase and punctuation in password"""
        if self.contains_upper(password) and self.contains_punctuation(password) and len(password) >= 16:
            return "Strong password"
        elif self.contains_upper(password) or self.contains_punctuation(password) or len(password) >= 16:
            return "Medium password"
        else:
            return "Weak password"
        
    def contains_upper(self, password) -> bool:
        """Function to search password for uppercase"""
        uppercase:list[str] = []
        for i in password:
            if i in string.ascii_uppercase:
                uppercase.append(i)
        if len(uppercase) >= 1:
            return True
        else:
            return False
        

    def contains_punctuation(self, password) -> bool:
        """Function to search password for punctuation"""
        punctuation:list[str] = []
        for i in password:
            if i in string.punctuation:
                punctuation.append(i)
        if len(punctuation) >= 1:
            return True
        else:
            return False

def main():
    """Get input from user and generate password"""
    length:int = 10
    uppercase:str = True
    symbols:str = True

    while True:
        try:
            length:int = int(input("Length of password?: "))
            break
        except ValueError:
            print("Please enter a number. e.g 1, 10, 12")
    try:
        upper:str = input("Use upper case?: ").lower()
        symbol:str = input("Use symbols?: ").lower()
    except ValueError:
        print("Please answer yes or no.")
    
    if upper[0] == "n":
        uppercase = False
    if symbol[0] == "n":
        symbols== False

    password:Password = Password(length= length, uppercase = uppercase, symbols = symbols)
    generated = password.generate()
    strength = password.strength_check(generated)
    print(f'Password: {generated}   Strength: {strength}')


if __name__ == "__main__":
    main()