from collections import Counter
import re

def main():
    """Executes main program"""
    user_input:str = input('Enter your text: ').strip()

    if user_input.endswith(".txt"): #Checks for file extension
        text = open_file(user_input)
        word_frequencies:list[tuple[str, int]] = get_frequency(text)
    else:
        word_frequencies:list[tuple[str, int]] = get_frequency(user_input)
    
    for word, count in word_frequencies:
       print(f'{word}: {count}')


def get_frequency(text:str) -> list[tuple[str, int]]:
    """Uses regular expressions and Counter module to count words"""
    lowered_text:str = text.lower()
    words:list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common()


def open_file(file) -> str:
    """Opens file and returns contents"""
    with open(file, 'r') as text_file:
        return text_file.read()


if __name__ == "__main__":
    main()