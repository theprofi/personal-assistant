from ..model_api import ModelApi
from api_token.token_getter import TokenGetter
import openai

   
class ChatGpt(ModelApi):
    def __init__(self):
        openai.api_key = TokenGetter().get_token()

    def get_answer(self, question):
        def get_api_response(question):
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=question,
                best_of=3,
                max_tokens=2000,
                # def is 0.5, 0.7 make it more creative
                temperature=0.7,
                # top_p=1.0,
                # frequency_penalty=0.2,
                # presence_penalty=0.0,
            )
            return response["choices"][0]["text"]
        while True:
            try:
                return get_api_response(question)
            except Exception as e:
                return get_api_response(question)