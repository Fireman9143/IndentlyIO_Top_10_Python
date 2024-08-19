from difflib import SequenceMatcher
from datetime import datetime
import sys, python_weather, asyncio, os

class ChatBot:
    def __init__(self, name:str, responses:dict[str,str]) -> None:
        self.name = name
        self.responses = responses

    @staticmethod
    def calculate_similarity(input_sentence:str, response_sentence:str) -> float:
        sequence:SequenceMatcher = SequenceMatcher(a=input_sentence, b=response_sentence)
        return sequence.ratio()
    
    def get_best_response(self, user_input:str) -> tuple[str, float]:
        highest_similarity:float = 0.0
        best_match:str = 'Sorry, I don\'t understand.'

        for response in self.responses:
            similarity:float = self.calculate_similarity(user_input, response)
            if similarity < 0.5:
                return best_match, similarity
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match:str = self.responses[response]
                return best_match, highest_similarity
    
    @staticmethod
    async def getweather():
        async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
            weather = await client.get('Springfield')
            
            return (f'The temp is: {weather.temperature} degrees\n'
                    f'The humidity is: {weather.humidity} percent\n'
                    f'It feels like: {weather.feels_like} degrees')
    
        
    def run(self) -> None:
        print(f'Hello! My name is {self.name}, how can I help you?')

        while True:
            user_input:str = input('You: ')
            response, similarity = self.get_best_response(user_input)

            if response == "GET_TIME":
                response = f'The time is: {datetime.now():%H:%M}'
            if response == "GET_WEATHER":
                response =  asyncio.run(self.getweather())
            if user_input.lower() == 'bye' or user_input.lower() == 'quit':
                sys.exit(f'{self.name}: Goodbye!')
            
            print(f'{self.name}: {response} (Similarity: {similarity:.2%})')


def main():
    responses:dict[str, str] = {
        'hello': 'Hello! How are you today?',
        'how are you?': 'Great thanks, how about you?',
        'what time is it?': 'GET_TIME',
        'what is the weather like?': 'GET_WEATHER'
    }

    chatbot:ChatBot = ChatBot(name='Bob', responses=responses)
    chatbot.run()
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


if __name__ == "__main__":
    main()

"""
Add more responses?
more cool features??
"""