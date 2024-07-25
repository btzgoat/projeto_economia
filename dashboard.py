from dataclasses import dataclass
import os

lista_de_transacoes = []
lista_de_categorias = []

def limpar_campo():
    os.system('cls')

def voltar_ao_menu():
    input('Pressione ENTER para voltar ao menu de opções...')

@dataclass
class Categoria:
    nome: str
    def adicionar_nova_categoria(nome):
        nova_categoria = Categoria(nome=nome)
        lista_de_categorias.append(nova_categoria)
        return nova_categoria
    
@dataclass
class Transações():
    valor: int
    categoria: str
    def adicionar_nova_transacao(valor, categoria):
        nova_transacao = Transações(
            valor = valor,
            categoria = categoria
            )
        
        lista_de_transacoes.append(nova_transacao)
        return nova_transacao
    
@dataclass
class Saldo():
    saldo_total: int = 0
    def atualizar_saldo(valor):
        Saldo.saldo_total += valor

@dataclass
class Dashboard():

    def exibir_opcoes():
        while True:
            print('''Escolha uma das opções de acordo com o seu desejo:
                  ''')
            print('1. Acessar saldo total')
            print('2. Registrar nova transação')
            print('3. Listar transações')
            print('''4. Sair
                 ''')
            comando = int(input('Digite a opção que você deseja: '))
            if comando == 1:
                limpar_campo()
                print(f'Esse é o seu saldo atual: {Saldo.saldo_total}')
                voltar_ao_menu()
                limpar_campo()
            elif comando == 2:
                limpar_campo()
                valor_transacao = int(input('Digite o valor da transação que você deseja adicionar:'))
                categoria_transacao = input('Digite a categoria da transação que você deseja adicionar:')
                Transações.adicionar_nova_transacao(valor_transacao, categoria_transacao)
                Saldo.atualizar_saldo(valor_transacao)
                voltar_ao_menu()
                limpar_campo()
            elif comando == 3:
                limpar_campo()
                for transacao in lista_de_transacoes:
                    print(f'Valor: {transacao.valor} / Categoria: {transacao.categoria}')
                voltar_ao_menu()
                limpar_campo()
            elif comando == 4:
                limpar_campo()
                print('Saindo...')
                break
        else:
            limpar_campo()
            print('Opção inválida, tente novamente!')

        input('Pressione ENTER para continuar...')
        limpar_campo()


Dashboard.exibir_opcoes()