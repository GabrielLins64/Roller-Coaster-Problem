import threading
import signal
import sys
import time
import random
from .report import gerar_relatorio

# --------------------------------------------
# Variáveis globais

# Controle de execução
EXECUTANDO = True
NUM_CARROS = 0

# Filas
fila = []
carros = []
tempos_espera_passageiros = []

# Contadores/Semáforos p/ controle de ordem
proximo_carro = 0
proximo_passageiro = 0
desembarques = 0

# --------------------------------------------


def finalizar(signal, frame):
    global EXECUTANDO
    global fila
    global carros
    global tempos_espera_passageiros

    EXECUTANDO = False
    time.sleep(0.5)

    print("Limpando a memória para sair...", end="")
    try:
        del fila[:]
        del carros[:]
        print(" Pronto!")
    except Exception as err:
        print("\nProblema na limpeza:", err)


# Registrando sinal de finalização da execução
signal.signal(signal.SIGINT, finalizar)


class Passageiro:
    """Classe do Passageiro da Montanha Russa

    Parameters\n
    ----------
      ticket : int
          Número do ticket do passageiro (para saber sua ordem na fila)\n
      Te : int
          Tempo de embarque e desembarque\n
      Tc : int
          Tempo de chegada daquele passageiro na fila
    """

    def __init__(self, ticket, Te):
        self.ticket = ticket
        self.Te = Te
        self.tempo_aguardo_inicial = 0

    def chegar(self):
        """Coloca o passageiro na fila"""
        global fila

        fila.append(self)
        self.tempo_aguardo_inicial = time.time()

        print(f"Passageiro {self.ticket} entrou na fila.")

    def embarcar(self):
        """Embarca o passageiro em um carro"""
        global fila
        global carros
        global proximo_passageiro
        global proximo_carro
        global tempos_espera_passageiros
        global EXECUTANDO

        if (not EXECUTANDO):
            return

        time.sleep(0.5)

        while (carros[proximo_carro].cheio and EXECUTANDO):
            time.sleep(0.1)

        print(
            f"Passageiro {self.ticket} embarcando no carro {proximo_carro}...")

        fila.pop(0)
        tempos_espera_passageiros.append(
            time.time() - self.tempo_aguardo_inicial
        )

        time.sleep(self.Te)
        carros[proximo_carro].passageiros.append(self)

        print(f"Passageiro {self.ticket} embarcou!")
        proximo_passageiro += 1

    def desembarcar(self, id_carro):
        """Desembarca o passageiro de um carro"""

        print(f"Passageiro {self.ticket} desembarcando do carro {id_carro}...")
        time.sleep(self.Te)

        print(f"Passageiro {self.ticket} desembarcou!")

    def iniciar(self):
        global proximo_passageiro
        global EXECUTANDO

        self.chegar()

        while (proximo_passageiro != self.ticket and EXECUTANDO):
            time.sleep(0.05)

        self.embarcar()


class Carro:
    """Classe do Carro da Montanha Russa

    Parameters\n
    ----------
      id : int
          ID do Carro\n
      C : int
          Quantidade de lugares de cada carro\n
      Tm : int
          Tempo do passeio
    """

    def __init__(self, id, C, Tm):
        self.id = id
        self.C = C
        self.Tm = Tm
        self.passageiros = []
        self.tempo_inicial = 0
        self.tempo_de_movimento = 0
        self.cheio = False

    def aguardar_passageiros(self):
        """Espera ocupada até embarcar todos os C passageiros"""
        global proximo_carro
        global EXECUTANDO
        global NUM_CARROS

        print(f"Carro {self.id} aguardando passageiros.")

        while (len(self.passageiros) < self.C and EXECUTANDO):
            pass

        self.cheio = True
        proximo_carro = 0 if self.id == NUM_CARROS - 1 else proximo_carro + 1

    def iniciar_passeio(self):
        """Inicia o passeio da instância de Thread do Carro"""
        global EXECUTANDO

        if (not EXECUTANDO):
            return

        print(f"Carro {self.id} iniciando passeio.")
        time.sleep(self.Tm)
        print(f"Carro {self.id} terminou o passeio!")

        self.tempo_de_movimento += self.Tm

    def parar(self):
        """Para o carro para os passageiros desembarcarem"""
        global EXECUTANDO
        global desembarques

        for passageiro in self.passageiros:
            if (not EXECUTANDO):
                return
            passageiro.desembarcar(self.id)
            del passageiro

        self.passageiros = []
        self.cheio = False
        desembarques += self.C

    def iniciar(self):
        global EXECUTANDO

        self.tempo_inicial = time.time()

        while (EXECUTANDO):
            self.aguardar_passageiros()
            self.iniciar_passeio()
            self.parar()

    def relatorio(self):
        report = {
            "id": self.id,
            "tempo_total": time.time() - self.tempo_inicial,
            "tempo_de_movimento": self.tempo_de_movimento
        }
        report["tempo_parado"] = report["tempo_total"] \
            - self.tempo_de_movimento

        return report


class MontanhaRussa:
    """Classe da Montanha Russa

    Parameters\n
    ----------
      n : int
          Número de passageiros\n
      m : int
          Número de carros\n
      C : int
          Quantidade de lugares de cada carro\n
      Te : int
          Tempo de embarque / desembarque\n
      Tm : int
          Tempo do passeio\n
      Tp : list
          Array com os possíveis tempos de chegada de cada passageiro
    """

    def __init__(self, n, m, C, Te, Tm, Tp):
        self.horario_inicio = time.ctime()
        self.inicio = time.time()
        self.n = n
        self.m = m
        self.C = C
        self.Te = Te
        self.Tm = Tm
        self.Tp = Tp

    def criar_passageiros(self):
        """Cria os passageiros em seus devidos tempos"""
        global EXECUTANDO

        for i in range(self.n):
            if (not EXECUTANDO):
                return
            passageiro = Passageiro(i, self.Te)
            thread_passageiro = threading.Thread(target=passageiro.iniciar)

            time.sleep(random.uniform(self.Tp[0], self.Tp[1] + 0.000001))
            thread_passageiro.start()

    def ligar_carros(self):
        """Cria e inicializa as instâncias de carros"""
        global carros

        for i in range(self.m):
            carro = Carro(i, self.C, self.Tm)
            carros.append(carro)
            thread_carro = threading.Thread(target=carro.iniciar)
            thread_carro.start()

    def verificar_termino(self):
        """Espera ocupada para finalizar o programa

        Aguarda até todos os passageiros terem sido criados, então
        aguarda até que a fila esteja vazia e, por fim, aguarda
        """
        global desembarques
        global tempos_espera_passageiros
        global carros
        global EXECUTANDO

        while (desembarques < self.n):
            if (not EXECUTANDO):
                return
            time.sleep(0.1)

        EXECUTANDO = False
        time.sleep(0.5)

        parametros = self.__dict__
        parametros["tempo_execucao"] = time.time() - self.inicio
        tempos_carros = [carro.relatorio() for carro in carros]

        gerar_relatorio(parametros, tempos_espera_passageiros, tempos_carros)

        finalizar(None, None)

    def comecar(self):
        """Cria os carros e passageiros"""
        global NUM_CARROS

        NUM_CARROS = self.m
        random.seed()

        self.ligar_carros()
        self.criar_passageiros()
        self.verificar_termino()
