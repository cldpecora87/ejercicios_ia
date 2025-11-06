
import os
from typing import Dict, List
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class ChatBot:
    def __init__(self, temperature:float, memory:bool, max_token:int=8192):
        self._client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))
        self._model = api_key= os.getenv("MODELO")
        self._messages: List[Dict[str, str]] = []
        self._temperature = temperature
        self._memory = memory
        self._max_token = max_token


    def talk(self, user_message:str)->str:
        if not self._memory:
            self._messages = []
            
        self._messages.append({"role": "user", "content":user_message})

        response = self._client.chat.completions.create(
            model= self._model,
            messages= self._messages,
            temperature = self._temperature,
            max_tokens= self._max_token
        )

        respuesta = response.choices[0].message.content
        self._messages.append({"role": "assistant", "content":respuesta})

        return respuesta

    