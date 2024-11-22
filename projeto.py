class Clientes:
    def __init__(self, id, nome= str, cpf= str, email= str, telefone= str) -> None:
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

class Quarto:
    def __init__(self, id=int, nome= str, valor= float, disponibilidade= bool) -> None:
        self.id = id
        self.nome = nome
        self.valor = valor
        self.disponibilidade = disponibilidade

class Reserva_quartos:
    def __init__(self, id= int, data_inicio= str, id_quarto= int, id_cliente= int, fim_reserva= str) -> None:
        self.id = id
        self.data_inicio = data_inicio
        self.id_quarto = id_quarto
        self.id_cliente = id_cliente
        self.fim_reserva = fim_reserva

class Hotel:
    def __init__(self, nome= str) -> None:
        self.nome= nome
        self.lista_reservas = []
        self.lista_clientes = []
        self.lista_de_quartos = []
        self.historico_reservas = []

#Quartos: Add, ver, editar e excluir
    def addQuarto(self):
        nome = input('Nome do quarto: ')
        valor = float(input('Valor do quarto: '))
       
        quarto = Quarto(id= self.id_quarto, nome= nome, valor= valor)
        self.id_quartos += 1
       
        self.lista_de_quartos.append(quarto)
        return f"Quarto cadastrado no sistema!"
    
    def verQuartos(self):
        for quarto in self.lista_de_quartos:
            print(f"""
            ID: {quarto.id}
            Nome: {quarto.nome}
            Valor: R${quarto.valor}
            Disponibilidade: {quarto.disponibilidade}
            """)

    def editar_quartos(self):
        id_quarto = int(input('ID do quarto: '))
        quarto_encontrado = False
        
        for quarto in self.lista_de_quartos:
            if quarto.id == id_quarto:
                quarto_encontrado = True
                while True:
                    quarto_editar_menu = input("""
                    O que você quer editar:
                    1 - Nome
                    2 - Valor
                    0 - Voltar
                    """)
                    match quarto_editar_menu:
                        case "1":
                            novo_nome = input('Digite o novo nome:')
                            quarto.nome = novo_nome
                        case "2":
                            



        



