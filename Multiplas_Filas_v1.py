from collections import deque

# Classe para representar um processo


class Processo:
    def __init__(self, id, prioridade, tempo_execucao):
        self.id = id
        self.prioridade = prioridade
        self.tempo_execucao = tempo_execucao

# Função para exibir o diagrama de execução na CPU


def exibir_diagrama(processos_executados):
    print("\n                 ESCALONAMENTO - MÚLTIPLAS FILAS\n")
    print("# Diagrama de execucao na CPU:\n")
    for processo in processos_executados:
        print(
            f"  Processo {processo.id} | Tempo de Execução: {processo.tempo_execucao} |{'▅ ' * processo.tempo_execucao} ")
    print("\n")


# Função principal do algoritmo


def executar_algoritmo():
    fila_prioridade_0 = deque()  # Fila de prioridade 0 (FIFO)
    fila_prioridade_1 = deque()  # Fila de prioridade 1 (Round Robin)

    # Adicionando alguns processos de exemplo
    fila_prioridade_0.append(Processo("A", 0, 5))
    fila_prioridade_0.append(Processo("B", 0, 4))
    fila_prioridade_1.append(Processo("C", 1, 4))
    fila_prioridade_0.append(Processo("D", 0, 5))
    fila_prioridade_1.append(Processo("E", 1, 4))

    tempo_total = 0  # Tempo total de execução

    # Execução dos processos
    processos_executados = []  # Lista para armazenar os processos executados

    # Execução da fila de prioridade 0 (FIFO)
    while fila_prioridade_0:
        processo_atual = fila_prioridade_0.popleft()
        processos_executados.append(processo_atual)
        tempo_total += processo_atual.tempo_execucao

    # Execução da fila de prioridade 1 (Round Robin)
    quantum = 2  # Tamanho do quantum para o Round Robin
    while fila_prioridade_1:
        processo_atual = fila_prioridade_1.popleft()
        processos_executados.append(processo_atual)
        tempo_restante = processo_atual.tempo_execucao - quantum
        tempo_total += quantum

        if tempo_restante > 0:
            processo_atual.tempo_execucao = tempo_restante
            fila_prioridade_1.append(processo_atual)
        
    # Exibir o diagrama de execução na CPU
    exibir_diagrama(processos_executados)

    # Exibir o tempo total de execução
    # print(f"\nTempo total de execução: {tempo_total} unidades de tempo")


# Executar o algoritmo
executar_algoritmo()
