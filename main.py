from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
import uvicorn
from starlette.middleware.cors import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


servicos = {
    1: {"nome": "Lanches", "status": "cliente"},
    2: {"nome": "Vestuários", "status": "cliente"},
    3: {"nome": "Beleza", "status": "cliente"},
    4: {"nome": "Saúde", "status": "cliente"},
    5: {"nome": "Anunciar Produtos", "status": "empresa"},
    6: {"nome": "IA MAX", "status": "empresa"}
}




servicos_lanches = {
    1: {"nome": "Hamburguer", "preco": 10.00, "empresa": "Bem-viver", "local": "freguesiadoo", "avaliacao": 5},
    2: {"nome": "MilkShake", "preco": 20.00, "empresa": "Takamassa no muro", "local": "freguesiadoo", "avaliacao": 4},
    3: {"nome": "Rolinho Primavera", "preco": 15.00, "empresa": "Bem-viver", "local": "freguesiadoo", "avaliacao": 5},
    4: {"nome": "Pipoca Salgada", "preco": 22.00, "empresa": "Empresa Insana", "local": "freguesiadoo", "avaliacao": 5},
    5: {"nome": "Pastel de Atum", "preco": 33.00, "empresa": "Salgado Ruim", "local": "freguesiadoo", "avaliacao": 5},
    6: {"nome": "Pipoca Doce", "preco": 44.00, "empresa": "Tio Jones", "local": "freguesiadoo", "avaliacao": 5},
    7: {"nome": "Barca de Sushi", "preco": 52.00, "empresa": "Takamassa no muro", "local": "freguesiadoo", "avaliacao": 5},
}


@app.get("/servicos/{status}")
def listar_servicos(status):
    return [servico for servico in servicos.values() if servico["status"] == status]

@app.get("/servicos/cliente/{local}/{avaliacao}")
def listar_servico(local: str, avaliacao: float = Path(..., title="Avaliação do serviço")):
    return [servico for servico in servicos_lanches.values() if servico["local"] == local and servico["avaliacao"] >= avaliacao]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)