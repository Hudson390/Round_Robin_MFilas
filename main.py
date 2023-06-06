# Definindo a estrutura de uma fila
class Fila:
    def __init__(self, quantum):
        self.processos = []
        self.quantum = quantum

    def adicionar_processo(self, processo):
        self.processos.append(processo)

    def executar_processo(self):
        if len(self.processos) > 0:
            processo = self.processos.pop(0)
            if processo["tempo_restante"] > self.quantum:
                processo["tempo_restante"] -= self.quantum
                print("Executando processo",
                      processo["nome"], "por", self.quantum, "unidades de tempo.")
                self.processos.append(processo)
            else:
                print("Executando processo", processo["nome"], "por",
                      processo["tempo_restante"], "unidades de tempo.")

    def vazia(self):
        return len(self.processos) == 0

# Simulando o escalonamento de múltiplas filas


def escalonar_filas(filas):
    tempo_total = 0
    while True:
        fila_atual = filas[0]
        if fila_atual.vazia():
            filas.pop(0)
            if len(filas) == 0:
                break
            continue
        fila_atual.executar_processo()
        tempo_total += 1


# Criando as filas e adicionando processos
fila1 = Fila(2)
fila2 = Fila(4)

fila1.adicionar_processo({"nome": "P1", "tempo_restante": 6})
fila1.adicionar_processo({"nome": "P2", "tempo_restante": 4})
fila2.adicionar_processo({"nome": "P3", "tempo_restante": 8})
fila2.adicionar_processo({"nome": "P4", "tempo_restante": 10})

# Adicionando as filas em uma lista
filas = [fila1, fila2]

# Executando o escalonamento das filas
escalonar_filas(filas)
