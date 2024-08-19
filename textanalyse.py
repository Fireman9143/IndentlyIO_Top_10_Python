import re
from collections import Counter

def open_file(path:str) -> str:
    with open(path, 'r') as file:
        text:str = file.read()
        return text
    

def analyse(text:str) -> dict[str, int]:
    #print(f'Text: "{text}"')
    result:dict[str, int] = {
        'total_chars_incl_space': len(text),
        'total_chars_excl_space': len(text.replace(' ', '')),
        'total_spaces': text.count(' '),
        'total_words': len(text.split())
    }
    return result


def get_frequency(text:str) -> list[tuple[str, int]]:#Taken from the frequency.py practice problem
    """Uses regular expressions and Counter module to count words"""
    lowered_text:str = text.lower()
    words:list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common()


def main():
    text:str = open_file('finances.py')
    analysis:dict[str,int] = analyse(text)
    word_frequencies:list[tuple[str, int]] = get_frequency(text)
    top_five = 0
    for word, count in word_frequencies:
        if top_five == 5:
            break
        else:
            top_five += 1
            print(f'{word}: {count}')
    for k, v in analysis.items():
        match k:
            case 'total_chars_incl_space': print(f'Total characters including space: {v}')
            case 'total_chars_excl_space': print(f'Total characters excluding space: {v}')
            case 'total_spaces': print(f'Total number of space: {v}')
            case 'total_words': print(f'Total words space: {v}')

        
if __name__ == "__main__":
    main()