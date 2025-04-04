from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("../arquivos/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv", sep=";")

@app.get("/buscar")
def buscar_operadora(nome: str = Query(..., description="Nome da operadora")):
    resultado = df[df['Nome_Fantasia'].str.contains(nome, case=False, na=False)]
    return resultado.fillna("").to_dict(orient='records')
