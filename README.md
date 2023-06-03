# Round_Robin_MFilas

Explicação passo a passo:

1. Definimos a classe Fila que representa cada fila de processos. Cada fila tem uma lista de processos e um quantum, que define o tempo máximo de execução de cada processo.

2. Criamos instâncias das filas fila1 e fila2 e adicionamos processos a elas, especificando o nome e o tempo restante de cada processo.

3. Criamos uma lista filas e adicionamos as filas criadas.

4. A função escalonar_filas simula o escalonamento das filas. O tempo total é controlado por um laço while.

5. Em cada iteração, a fila atual é obtida a partir do início da lista filas. Se a fila estiver vazia, ela é removida da lista e o laço continua para a próxima iteração.

6. Se a fila não estiver vazia, o primeiro processo da fila é executado. Se o tempo restante do processo for maior que o quantum da fila, o processo é executado pelo quantum e o tempo restante é atualizado. 

7. O processo é então adicionado novamente à fila. Caso contrário, o processo é executado até o final.
