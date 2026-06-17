from datetime import datetime
import os

def gerar_relatorio_geral(clientes, pedidos):
    os.makedirs("relatorios", exist_ok=True)

    caminho = "relatorios/relatorio_geral.txt"

    with open(caminho, "w",encoding="utf-8") as arquivo:
        arquivo.write("=" * 40 + "\n")
        arquivo.write("RELATÓRIO GERAL\n")
        arquivo.write(
            f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
        )
        arquivo.write("=" * 40 + "\n\n")

        arquivo.write(f"Total de clientes: {len(clientes)}\n")
        arquivo.write(f"Total de pedidos: {len(pedidos)}\n\n")

        arquivo.write("PEDIDOS\n\n")

        for pedido in pedidos:
            arquivo.write(f"Código: {pedido['codigo']}\n")
            arquivo.write(f"Cliente: {pedido['nome_cliente']}\n")
            arquivo.write(f"Produto: {pedido['nome_produto']}\n")
            arquivo.write(f"Status: {pedido['status']}\n")
            arquivo.write(f"Total: R$ {pedido['total']:.2f}\n")
            arquivo.write("-" * 30 + "\n")

def gerar_relatorio_cliente(cpf, pedidos):
    os.makedirs("relatorios", exist_ok=True)

    pedidos_cliente = [
        p for p in pedidos if p["cpf_cliente"] == cpf
    ]

    if not pedidos_cliente:
        print("Nenhum pedido encontrado.")
        return

    caminho = f"relatorios/relatorio_{cpf}.txt"

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"RELATÓRIO DO CLIENTE {cpf}\n\n")

        for pedido in pedidos_cliente:
            arquivo.write(f"Código: {pedido['codigo']}\n")
            arquivo.write(f"Produto: {pedido['nome_produto']}\n")
            arquivo.write(f"Status: {pedido['status']}\n")
            arquivo.write(f"Total: R$ {pedido['total']:.2f}\n")
            arquivo.write("-" * 30 + "\n")

    print(f"\nRelatório salvo em: {caminho}")
    print(f"\nRelatório salvo em: {caminho}")