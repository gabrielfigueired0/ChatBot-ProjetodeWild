from datetime import datetime
import os

def gerar_relatorio_geral(clientes, pedidos):
    os.makedirs("relatorios", exist_ok=True)

    caminho = "relatorios/relatorio_geral.txt"
    linha = "=" * 40
    separador = "=" * 30
    agora = datetime.now().strftime('%d/%m/%Y %H:%M')


    with open(caminho, "w",encoding="utf-8") as arquivo:
        arquivo.write("=" * 40 + "\n")
        arquivo.write("RELATÓRIO GERAL\n")
        arquivo.write(
            f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
        )
        arquivo.write("=" * 40 + "\n\n")

        print (linha)
        print ("            RELATÓRIO GERAL")
        print (f"  Gerado em {agora}")
        print(linha)

        arquivo.write(f"Total de clientes: {len(clientes)}\n")
        arquivo.write(f"Total de pedidos: {len(pedidos)}\n\n")

        print (f"\n Total de clientes : {len(clientes)}")
        print (f"  Total de pedidos :  {len(pedidos)}")

        arquivo.write("PEDIDOS\n\n")
        print ("PEDIDOS")
        print (separador)


        for pedido in pedidos:
            arquivo.write(f"Código: {pedido['codigo']}\n")
            arquivo.write(f"Cliente: {pedido['nome_cliente']}\n")
            arquivo.write(f"Produto: {pedido['nome_produto']}\n")
            arquivo.write(f"Status: {pedido['status']}\n")
            arquivo.write(f"Total: R$ {pedido['total']:.2f}\n")
            arquivo.write("-" * 30 + "\n")

            print (f"Código : {pedido['codigo']}\n")
            print (f"Cliente : {pedido['nome_cliente']}\n")
            print (f"Produto : {pedido['nome_produto']}\n")
            print (f"Status : {pedido['status']}\n")
            print (f"Total : R$ {pedido['total']:.2f}\n")
            print(separador)

    print(f"\n Relatório salvo em : {caminho}\n")

def gerar_relatorio_cliente(cpf, pedidos, clientes):
    os.makedirs("relatorios", exist_ok=True)
 
    pedidos_cliente = [p for p in pedidos if p["cpf_cliente"] == cpf]
 
    if not pedidos_cliente:
        print("\n  Nenhum pedido encontrado para este CPF.")
        return
 
    # Busca o nome do cliente na lista de clientes
    cliente = next((c for c in clientes if c["cpf"] == cpf), None)
    nome = cliente["nome"] if cliente else "Cliente não encontrado"
 
    caminho = f"relatorios/relatorio_{cpf}.txt"
    linha = "=" * 40
    separador = "-" * 30
    agora = datetime.now().strftime('%d/%m/%Y %H:%M')
 
    total_geral = sum(p["total"] for p in pedidos_cliente)
 
    with open(caminho, "w", encoding="utf-8") as arquivo:
        # ── cabeçalho ──────────────────────────────
        arquivo.write(linha + "\n")
        arquivo.write(f"RELATÓRIO DO CLIENTE\n")
        arquivo.write(f"Gerado em: {agora}\n")
        arquivo.write(linha + "\n\n")
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"CPF:  {cpf}\n\n")
 
        print(linha)
        print("      RELATÓRIO DO CLIENTE")
        print(f"  Gerado em: {agora}")
        print(linha)
        print(f"\n  Nome: {nome}")
        print(f"  CPF:  {cpf}\n")
 
        # ── pedidos ────────────────────────────────
        arquivo.write("SEUS PEDIDOS\n\n")
        print("  SEUS PEDIDOS")
        print(separador)
 
        for pedido in pedidos_cliente:
            arquivo.write(f"Código:  {pedido['codigo']}\n")
            arquivo.write(f"Produto: {pedido['nome_produto']}\n")
            arquivo.write(f"Status:  {pedido['status']}\n")
            arquivo.write(f"Total:   R$ {pedido['total']:.2f}\n")
            arquivo.write(separador + "\n")
 
            print(f"  Código:  {pedido['codigo']}")
            print(f"  Produto: {pedido['nome_produto']}")
            print(f"  Status:  {pedido['status']}")
            print(f"  Total:   R$ {pedido['total']:.2f}")
            print(separador)
 
        # ── total geral ────────────────────────────
        arquivo.write(f"\nTotal gasto: R$ {total_geral:.2f}\n")
        print(f"\n  Total gasto: R$ {total_geral:.2f}")
 
    print(f"  Relatório salvo em: {caminho}\n")