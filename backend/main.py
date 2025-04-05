from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from unidecode import unidecode

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("../arquivos/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv", sep=";")

df['Nome_Fantasia'] = df['Nome_Fantasia'].astype(str).str.strip()
df['Nome_Fantasia_Sem_Acento'] = df['Nome_Fantasia'].apply(lambda x: unidecode(x.lower()) if isinstance(x, str) else x)

@app.get("/buscar")
def buscar_operadora(nome: str = Query(..., description="Nome da operadora")):
    nome_sem_acento = unidecode(nome.strip().lower())
    resultado = df[df['Nome_Fantasia_Sem_Acento'].str.contains(nome_sem_acento, na=False)]
    return resultado.drop(columns=['Nome_Fantasia_Sem_Acento']).fillna("").to_dict(orient='records')
