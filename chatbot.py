
import os
from typing import Dict, List
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class ChatBot:
    def __init__(self, temperature:float, memory:bool, max_token:int=8192):
        """
        Args:
            temperature: Define que tan creativo puede ser el LLM en sus respuestas 0 = nada creativo, 1 = totalmente creativo
            memory: Determina si se guarda el historial de conversacion
            max_token: define la cantidad maxima de tokens, por defecto 8192
        """
        self._client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))
        self._model = os.getenv("MODELO")
        self._messages: List[Dict[str, str]] = []
        self._temperature = temperature
        self._memory = memory
        self._max_token = max_token




    def talk(self, user_message:str)->str:
        """          
        Args:
            user_message: La pregunta del usuario en lenguaje natural
        Returns:
            Respuesta generada por el LLM
        """
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

    