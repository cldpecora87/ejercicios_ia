"""
EJERCICIO 2: Agente de Información de Países con API Pública

ENUNCIADO:
----------
Crear un agente inteligente que:

1. Reciba consultas en lenguaje natural sobre países del mundo
   Ejemplo: "¿Cuál es la capital de Francia?"
   Ejemplo: "Dime la población y moneda de Argentina"

2. Use el LLM de OpenAI para:
   - Extraer el nombre del país de la consulta del usuario
   - Interpretar qué información específica se está solicitando

3. Consulte la API REST Countries (https://restcountries.com/v3.1/name/{pais})
   para obtener datos reales del país

4. Use nuevamente el LLM para:
   - Formatear la respuesta de la API en lenguaje natural
   - Presentar la información de forma conversacional al usuario

OBJETIVO:
---------
Implementar un agente que integre:
- LLM para procesamiento de lenguaje natural
- API externa para obtener datos reales
- Flujo de trabajo agéntico (percepción → acción → respuesta)

API A UTILIZAR:
---------------
REST Countries API v3.1
- URL base: https://restcountries.com/v3.1
- Endpoint: /name/{nombre_pais}
- No requiere API key
- Documentación: https://restcountries.com

DATOS DISPONIBLES:
------------------
- Capital, población, área
- Idiomas oficiales, monedas
- Región, subregión
- Países fronterizos
- Bandera (emoji y URL)
- Zona horaria, código de llamada
"""

from chatbot import ChatBot
import requests    

bot = ChatBot(temperature=0.1, memory= True)
_pais:str|None = None

def extraer_pais(consulta_usuario)->str:
   """
   Usa el LLM para extraer el nombre del país de la consulta del usuario.

   Args:
      consulta_usuario: La pregunta del usuario en lenguaje natural

   Returns:
      El nombre del país en inglés (para la API)
   """

   system_prompt:str = f"""
      - Busca en el siguiente texto "{consulta_usuario}" el nombre de un pais
      - Traducelo al ingles
      - Devuelve solo el nombre del pais sin ningun otro comentario adicional
      - Si no podes indentificar el pais responde con "Pais no identificado"
   """
   
   retorno = bot.talk(system_prompt)
   return retorno

    

def consultar_api_paises(nombre_pais):
    """
    Consulta la API de REST Countries para obtener información del país.
    
    Args:
        nombre_pais: Nombre del país en inglés
    
    Returns:
        Diccionario con los datos del país o None si hay error
    """
    # TODO: Construir la URL de la API
    # URL base: https://restcountries.com/v3.1/name/
    # Agregar el nombre del país al final
    url = f"https://restcountries.com/v3.1/name/{nombre_pais}"
    
    try:
         # TODO: Hacer la petición GET a la API
         response = requests.get(url)
        
         if response.status_code != 200:
            return
        
         data = response.json()
         return data[0]
        
        
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar la API: {e}")
        return None


def formatear_respuesta(consulta_usuario, datos_pais):
   """
   Usa el LLM para formatear los datos del país en una respuesta natural.

   Args:
      consulta_usuario: La pregunta original del usuario
      datos_pais: Diccionario con los datos del país de la API

   Returns:
      Respuesta formateada en lenguaje natural
   """

   info = f"""
      idioma:{", ".join(datos_pais['languages'].values())},
      nombre:{datos_pais['name']['common']},
      capital: {datos_pais['capital']},
      monedas: {datos_pais['currencies'][next(iter(datos_pais['currencies']))]['name']},
      region: {datos_pais['region']},
      subregion:{ datos_pais['subregion']},
      area: {datos_pais["area"]} km²,
      poblacion:{datos_pais["population"]} habitantes,
      zona_horaria: {", ".join(datos_pais['timezones'])},
      bandera: {datos_pais["flags"]['png']}
      bandera_desc: {datos_pais["flags"]['alt']}
      escudo: {datos_pais["coatOfArms"]['png']}
   """
   
   prompt = f"""
     Responde en formato amigable a esta consulta {consulta_usuario} con la siguiente informacion {info} 
   - Si no te suministre la informacion para responder la consulta responde con "Lo siento, no cuento con esa informacion"
   - Solo responde la pregunta sin agregar mas detalles que lo solicitado

   """
   return bot.talk(prompt)


def agente_paises(consulta_usuario):
   """
   Función principal del agente que orquesta todo el flujo.
   
   Args:
      consulta_usuario: La pregunta del usuario
   
   Returns:
      Respuesta final del agente
   """
   global _pais
    
   print(f"\n🤖 Agente: Procesando tu consulta...\n")
   
   # PASO 1: Extraer el país de la consulta
   print("📍 Paso 1: Identificando el país...")
   
   if _pais is None:
      pais = extraer_pais(consulta_usuario)
   else:
      pais = _pais
    
   if not pais or pais == "Pais no identificado":
      return "❌ No pude identificar el país en tu consulta. ¿Podrías reformularla?"

   _pais = pais
   print(f"   ✓ País identificado: {pais}")
   
   # PASO 2: Consultar la API
   print("🌍 Paso 2: Consultando información del país...")

   datos = consultar_api_paises(pais)
    
   if not datos:
      return f"❌ No encontré información sobre '{pais}'. Verifica el nombre del país."
   
   print(f"   ✓ Datos obtenidos de la API")
   
   # PASO 3: Formatear la respuesta
   print("💬 Paso 3: Generando respuesta natural...\n")
   # TODO: Llamar a la función formatear_respuesta()
   respuesta = formatear_respuesta(consulta_usuario, datos)
   
   return respuesta



def main():
   _nueva_consulta:bool = False
   global _pais
    
   print("=" * 80)
   print("🌎 AGENTE DE INFORMACIÓN DE PAÍSES")
   print("=" * 80)
   print("\nEste agente puede responder preguntas sobre países del mundo.")
   print("Ejemplos:")
   print("  - ¿Cuál es la capital de Francia?")
   print("  - Dime la población de Japón")
   print("  - ¿Qué moneda usa Argentina?")
   print("  - Información sobre Italia")
   while True:

      print("\nEscribe 'N' para hacer una nueva consulta o 'salir' para terminar.")
      print("=" * 80)
   
      # TODO: Solicitar la consulta del usuario
      consulta = input("\n👤 Tu consulta: ").strip()
      
      # TODO: Verificar si el usuario quiere salir
      if consulta.lower() in ['salir', 'exit', 'quit']:
         print("\n👋 ¡Hasta luego!")
         break
         
         
      if consulta.lower() == 'n':
         _nueva_consulta = True
         

      # TODO: Verificar que la consulta no esté vacía
      if not consulta or consulta.lower() == 'n':
         print("⚠️  Por favor, escribe una consulta.")
         _pais = None

      else:
         # TODO: Llamar al agente con la consulta
         respuesta = agente_paises(consulta)
         _nueva_consulta = False
         
         
         # TODO: Mostrar la respuesta
         print(f"\n🤖 Agente: {respuesta}")
         print("\n" + "-" * 80)


if __name__ == "__main__":
    main()


