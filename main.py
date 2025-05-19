from fastapi import FastAPI, Query
from random import randint
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/simular")
def simular_roleta(giros: int = Query(default=1000, gt=1)):
    contagem_numeros = {num: 0 for num in range(1, 11)}
    pares = 0

    for _ in range(giros):
        numero = randint(1, 10)
        contagem_numeros[numero] += 1

        if numero % 2 == 0:
            pares += 1

    prob_empirica = pares / giros
    prob_teorica = 0.5

    return {
        "giros": giros,
        "pares": pares,
        "impares": giros - pares,
        "probabilidade_empirica": round(prob_empirica, 4),
        "probabilidade_teorica": prob_teorica,
        "contagem_numeros": contagem_numeros
    }
