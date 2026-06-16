import json 
import os 
from dados_iniciais import clientes_iniciais, pedidos_iniciais

ARQ_CLIENTES = "dados/clientes.json"
ARQ_PEDIDOS = "dados/pedidos.json"

def carregar_clientes():
    try:
        if os.path.exists(ARQ_CLIENTES):
            with open(ARQ_CLIENTES, "r", encoding="utf-8") as f:
                return json.load(f) 
    except (json.JSONDecodeError, IOError):        
        print("Erro ao carregar clientes. Carregando dados iniciais.")
    return clientes_iniciais.copy()

def carregar_pedidos():
    try:
        if os.path.exists(ARQ_PEDIDOS):
            with open(ARQ_PEDIDOS, "r", encoding="utf-8") as arq:
                return json.load(arq)
    except (json.JSONDecodeError, OSError):
        print("Erro ao carregar pedidos.")

    return list(pedidos_iniciais)


def salvar_clientes(clientes):
    os.makedirs("dados", exist_ok=True)

    with open(ARQ_CLIENTES, "w", encoding="utf-8") as arq:
        json.dump(clientes, arq, ensure_ascii=False, indent=4)


def salvar_pedidos(pedidos):
    os.makedirs("dados", exist_ok=True)

    with open(ARQ_PEDIDOS, "w", encoding="utf-8") as arq:
        json.dump(pedidos, arq, ensure_ascii=False, indent=4)