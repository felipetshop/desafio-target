import json
import os

ARQUIVO_ESTOQUE = 'data/estoque.json'

proximo_id_movimentacao = 1

def carregar_estoque():
    
    if not os.path.exists(ARQUIVO_ESTOQUE):
        print(f"Erro: O arquivo '{ARQUIVO_ESTOQUE}' não foi encontrado.")
        return {"estoque": []}
    
    try:
        with open(ARQUIVO_ESTOQUE, 'r') as f:
            dados = json.load(f)
            isinstance(dados, dict) and "estoque" in dados and isinstance(dados["estoque"], list)
            return dados
            
    except json.JSONDecodeError:
        print(f"Erro no arquivo '{ARQUIVO_ESTOQUE}'.")
        return {"estoque": []}
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o estoque: {e}")
        return {"estoque": []}

def salvar_estoque(dados):
    
    try:
        with open(ARQUIVO_ESTOQUE, 'w') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar o estoque: {e}")

def listar_produtos(estoque):
    if not estoque["estoque"]:
        print("\n Estoque vazio.")
        return
        
    print("\n--- Produtos em Estoque ---")
    print(f"{'Código':<8} | {'Descrição':<30} | {'Qtde Atual':>10}")
    print("-" * 55)
    for produto in estoque["estoque"]:
        print(f"{produto['codigoProduto']:<8} | {produto['descricaoProduto']:<30} | {produto['estoque']:>10}")
    print("-" * 55)

def registrar_movimentacao(estoque):
    global proximo_id_movimentacao
    
    listar_produtos(estoque)
    
    while True:
        try:
            cod_produto = int(input("\nInforme o Código do Produto para movimentar: "))
            produto_encontrado = next((p for p in estoque["estoque"] if p["codigoProduto"] == cod_produto), None)
            
            if produto_encontrado:
                break
            else:
                print(f"Produto com código {cod_produto} não encontrado.")
        except ValueError:
            print("Entrada inválida.")

    
    while True:
        tipo = input("Informe o Tipo da Movimentação (E para Entrada / S para Saída): ").strip().upper()
        if tipo in ['E', 'S']:
            break
        else:
            print("Opção inválida. Digite 'E' para Entrada ou 'S' para Saída.")
    while True:
        try:
            quantidade = int(input("Informe a Quantidade a ser movimentada: "))
            if quantidade > 0:
                break
            else:
                print("A quantidade deve ser um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida.")

    descricao_mov = input("Descrição para a movimentação: ")

    if tipo == 'E':
        produto_encontrado["estoque"] += quantidade
        operacao = "ENTRADA"
    else: 
        if produto_encontrado["estoque"] >= quantidade:
            produto_encontrado["estoque"] -= quantidade
            operacao = "SAÍDA"
        else:
            print(f"\nERRO: Quantidade insuficiente em estoque para {produto_encontrado['descricaoProduto']}.")
            print(f"Estoque atual: {produto_encontrado['estoque']}. Tentativa de saída: {quantidade}.")
            return 

   
    print("\n" + "="*50)
    print(f"Movimentação Registrada com Sucesso!")
    print(f"ID da Movimentação: {proximo_id_movimentacao}")
    print(f"Operação: {operacao} de {quantidade} unidades")
    print(f"Produto: {produto_encontrado['descricaoProduto']} (Cód: {cod_produto})")
    print(f"Descrição: {descricao_mov}")
    print(f"Novo Estoque Final: {produto_encontrado['estoque']}")
    print("="*50)
    
    proximo_id_movimentacao += 1

def menu_principal():
    global proximo_id_movimentacao
    
   
    estoque_dados = carregar_estoque()
    
    if not estoque_dados["estoque"]:
         print("\nNão foi possível carregar o estoque. Verifique o arquivo JSON.")

    while True:
        print("\n" + "#"*30)
        print(" **Sistema de Gestão de Estoque** ")
        print("#"*30)
        print("1. Registrar **Movimentação** (Entrada/Saída)")
        print("2. Listar Produtos e Estoque Atual")
        print("3. Sair e Salvar Alterações")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            registrar_movimentacao(estoque_dados)
        elif escolha == '2':
            listar_produtos(estoque_dados)
        elif escolha == '3':
            print("\nSalvando estoque e encerrando o programa...")
            salvar_estoque(estoque_dados)
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução
if __name__ == "__main__":
    menu_principal()