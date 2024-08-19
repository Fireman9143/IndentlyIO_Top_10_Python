from morse import morse_code

def convert_to_morse(text:str) -> str:
    """Uses list comprehension to convert each letter to morse code"""
    return ' '.join(morse_code.get(char.upper(), '') for char in text)


def convert_to_text(text:str) -> str:
    """Splits up the morse code into words, words into letters, and compares letters to code dictionary.  Replaces dits/dahs with letters."""
    words:list = []
    for group in text.split("  "):
        words.append(group)
    letters:list = []
    for word in words:
        letters.append(word.split())
    translated:list = []
    for letter in letters:
        for n, i in enumerate(letter):
            for key, value in morse_code.items():
                if i == value:
                    letter.remove(i)
                    letter.insert(n, key)
        translated.append(''.join(letter).title())
    return ' '.join(translated)


def main():
    user_input:str = input('Enter message: ')
    output:str = convert_to_morse(user_input)
    print(output)
    morse_input:str = input("Enter morse code: ")
    words:str = convert_to_text(morse_input)
    print(words)


if __name__ == "__main__":
    main()