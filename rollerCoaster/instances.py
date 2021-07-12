import threading
import signal
import sys
import time
import random

RUNNING = True

fila = []
carros = []
passageiros = []

def signal_handler(signal, frame):
    global RUNNING
    global fila
    global carros
    global passageiros

    try:
        for i in range(len(fila)):
            del fila[i]
        for i in range(len(carros)):
            del carros[i]
        for i in range(len(passageiros)):
            del passageiros[i]
    except Exception:
        pass

    print("\nCleaned! Exiting")
    RUNNING = False

signal.signal(signal.SIGINT, signal_handler)
forever = threading.Event()

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

    def __init__(self, ticket, Te, Tp):
        self.ticket = ticket
        self.Te = Te
        self.Tp = Tp

    def chegar(self):
        """Coloca o passageiro na fila"""
        global fila
        time.sleep(self.Tp)
        fila.append(self)
        print(f"Passageiro {self.ticket} entrou na fila.")

    def embarcar(self):
        """Embarca o passageiro em um carro"""
        global fila
        print(f"Passageiro {self.ticket} embarcando...")

        fila.pop(0)
        time.sleep(self.Te)
        
        print(f"Passageiro {self.ticket} embarcou!")
        return self

    def desembarcar(self):
        """Desembarca o passageiro de um carro"""

        print(f"Passageiro {self.ticket} desembarcando...")
        time.sleep(self.Te)

        print(f"Passageiro {self.ticket} desembarcou!")


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
        self.cheio = False

    def aguardar_passageiros(self):
        global fila
        global RUNNING
        if (not RUNNING):
            return

        print(f"Carro {self.id} aguardando passageiros.")

        # Aguardando até o carro estar cheio
        while (len(self.passageiros) < self.C and RUNNING):
            if (len(fila) > 0):
                passageiro = fila[0].embarcar()
                self.passageiros.append(passageiro)
        
        self.cheio = True

    def iniciar_passeio(self):
        global RUNNING
        if (not RUNNING):
            return

        print(f"Carro {self.id} iniciando passeio.")
        time.sleep(self.Tm)
        print(f"Carro {self.id} terminou o passeio!")

        for passageiro in self.passageiros:
            passageiro.desembarcar()
            del passageiro
        
        self.passageiros = []
        self.cheio = False


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
        self.n = n
        self.m = m
        self.C = C
        self.Te = Te
        self.Tm = Tm
        self.Tp = Tp
        self.inicializado = False

    def inicializar(self):
        """Cria os carros e passageiros"""
        global carros
        global passageiros

        for i in range(self.m):
            carro = Carro(i, self.C, self.Tm)
            carros.append(carro)

        for i in range(self.n):
            passageiro = Passageiro(i, self.Te, random.choice(self.Tp))
            passageiros.append(passageiro)

        self.inicializado = True

    def abrir_fila(self):
        """Função de Thread que insere passageiros na fila global."""
        global passageiros
        print(f"A fila foi aberta!")

        for passageiro in passageiros:
            passageiro.chegar()

    def iniciar_carros(self):
        global carros
        global RUNNING

        while (RUNNING):
            for carro in carros:
                while (carro.cheio):
                    time.sleep(0.1)
                carro.aguardar_passageiros()
                thread = threading.Thread(target=carro.iniciar_passeio)
                thread.start()

    def comecar(self):
        if (not self.inicializado):
            self.inicializar()

        thread_carros = threading.Thread(target=self.iniciar_carros)
        thread_carros.start()

        thread_abrir_fila = threading.Thread(target=self.abrir_fila)
        thread_abrir_fila.start()
        thread_abrir_fila.join()