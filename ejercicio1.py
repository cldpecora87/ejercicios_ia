"""
EJERCICIO 1: Sistema de IA con Agentic - 3 Llamadas Secuenciales

ENUNCIADO:
----------
1. Primero, pide al LLM que elija un área de negocio que valga la pena explorar 
   para una oportunidad de IA con Agentic.

2. Después, pide al LLM que presente un problema en esa industria, algo desafiante 
   que pueda ser propicio para una solución con Agentic.

3. Finalmente, pide a la tercera convocatoria del LLM que proponga la solución 
   de IA con Agentic.

OBJETIVO:
---------
Implementar un sistema que realice 3 llamadas secuenciales al LLM, donde cada 
llamada utiliza el contexto de las anteriores para mantener coherencia en la 
conversación.

"""
from chatbot import ChatBot
    

bot = ChatBot(temperature=0.3, memory= True)

# ========================================================================
# PASO 1: Elegir un área de negocio
# ========================================================================
print("\n[PASO 1] Pidiendo al LLM que elija un área de negocio...\n")

prompt_1 = """Quiero que propongas un área de negocio donde la inteligencia artificial agentic (IA con capacidad de acción autónoma y toma de decisiones) tenga un alto potencial de impacto en los próximos 3 años.
            Tu respuesta debe incluir:
            - Área de negocio específica (no genérica).
            - Breve justificación (por qué es prometedora para IA agentic, considerando automatización, eficiencia, escalabilidad o reducción de costos).
            - Ejemplo concreto de aplicación práctica de IA agentic en ese contexto.

                Formato de respuesta:
                Área:
                Justificación:
                Ejemplo:
            """

respuesta = bot.talk(prompt_1)
print(f"Respuesta: {respuesta}")


# ========================================================================
# PASO 2: Presentar un problema en esa industria
# ========================================================================

print("\n" + "-" * 80)
print("[PASO 2] Pidiendo al LLM que presente un problema en esa industria...\n")

prompt_2 = """
    En el área de negocio seleccionada, describí un problema específico que sea desafiante, 
    y que pueda beneficiarse del uso de inteligencia artificial agentic (IA con capacidad de actuar y tomar decisiones autónomas). 
    Incluí en tu respuesta:
    - Problema: descripción breve y clara.
    - Por qué es desafiante: razones técnicas, operativas o de escala.
    - Cómo puede ayudar la IA agentic: explicación breve del impacto positivo.
"""

respuesta = bot.talk(prompt_2)
print(f"Respuesta: {respuesta}")



# ========================================================================
# PASO 3: Proponer la solución de IA con Agentic
# ========================================================================
print("\n" + "-" * 80)
print("[PASO 3] Pidiendo al LLM que proponga una solución de IA con Agentic...\n")


prompt_3 = """
    Diseña una solución basada en inteligencia artificial agentic para abordar el problema identificado en el área de negocio elegida.
    Tu propuesta debe detallar:
        - La arquitectura general del sistema agentic (cómo fluye la información y cómo se toman decisiones).
        - Los agentes necesarios (por ejemplo: agente de análisis, agente de ejecución, agente supervisor, etc.).
        - Cómo cada agente actúa de forma autónoma y se coordina con los demás.
        - Qué tecnologías o componentes podría usar (si aplica).
        - Los beneficios concretos de esta solución en términos de eficiencia, precisión o impacto de negocio.

    Formato:
        Solución agentic:
        Funcionamiento del sistema:
        Agentes involucrados:
        Coordinación y autonomía:
        Beneficios esperados:
"""

respuesta = bot.talk(prompt_3)
print(f"Respuesta: {respuesta}")

    # Resumen final
print("\n" + "=" * 80)
print("RESUMEN DEL EJERCICIO COMPLETADO")
print("=" * 80)
print(f"\n✓ Área de negocio identificada")
print(f"✓ Problema específico descrito")
print(f"✓ Solución de IA con Agentic propuesta")
print("\nEjercicio completado exitosamente!")