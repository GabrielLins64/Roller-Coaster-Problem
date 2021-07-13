<!-- For rendering markdown LaTeX into pdf -->
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
		MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

<center>
	<img src="assets/uslogo.png">
  <h2> Universidade Estadual do Ceará &ndash; UECE </h2>
</center>

---

**Curso:** Ciência da Computação<br>
**Disciplina:** Programação Paralela e Concorrente<br>
**Docente:** Marcial Porto Fernandez<br>
**Discente:** Gabriel Furtado Lins Melo<br>
**Matrícula:** 1394225

---

<h1> The Roller Coaster Problem </h1>

<h3> Sumário </h3>

- [Descrição](#descrição)
- [Instalação (Linux)](#instalação-linux)
- [Execução](#execução)
- [Relatório](#relatório)
  - [Formulação do problema](#formulação-do-problema)
    - [Caso carro único](#caso-carro-único)
    - [Caso 2 carros](#caso-2-carros)
    - [Caso 3 carros](#caso-3-carros)
  - [Descrição dos algoritmos](#descrição-dos-algoritmos)
  - [Descrição da implementação](#descrição-da-implementação)
    - [Classe Montanha Russa](#classe-montanha-russa)
    - [Classe Passageiro](#classe-passageiro)
    - [Classe Carro](#classe-carro)
  - [Resultados](#resultados)
    - [Caso carro único](#caso-carro-único-1)
    - [Caso 2 carros](#caso-2-carros-1)
    - [Caso 3 carros](#caso-3-carros-1)
- [Referências](#referências)

<hr>

### Descrição

Trabalho acadêmico da disciplina de Programação Concorrente e Paralela. Consiste na implementação, em *Python*, da resolução do problema de concorrência *Roller Coaster*.

<hr>

### Instalação (Linux)

**1.** Instale o Python 3.9, o gerenciador de pacotes Python (pip) e o gerenciador de ambientes virtuais Python:

```
sudo apt install python3.9
sudo apt install python3-pip
sudo pip install --upgrade pip
sudo pip install virtualenv
```


**2.** Clone este repositório com:

```
git clone git@github.com:GabrielLins64/Roller-Coaster-Problem.git
```

**3.** Navegue ao diretório raiz do projeto e crie um ambiente virtual *Python* para instalar as dependências do projeto:

```
$ cd Roller-Coaster-Problem
$ python3.9 -m venv env
```

**4.** Ative o ambiente virtual:

```
$ source env/bin/activate
```

**5.** Atualize a versão do pip no ambiente virtual (necessário para algumas dependências):

```
$ pip install --upgrade pip
```

**6.** Instale as dependências do projeto com:

```
$ pip install -r requirements.txt
```

*Quando quiser desativar o ambiente virtual use:

```
$ deactivate
```

<hr>

### Execução

Para configurar os parâmetros dos experimentos, altere as variáveis em `rollerCoaster/configs.json`.

Antes de executar o código, ative o ambiente virtual e, se necessário, instale as dependências, conforme o indicado na seção de [instalação](#instalação-linux). Então, no diretório raiz do projeto, execute com:

```
(env) $ python -m rollerCoaster
```

<hr>

### Relatório

#### Formulação do problema

Conforme Fernández (2021), o Problema da Montanha Russa (Roller Coaster) é um exemplo lúdico de um problema muito comum em controle de processos. O problema simula uma montanha russa onde pessoas entram na fila esperando a vez, depois entram no carro, que quando estiver cheio, parte para a viagem até retornar para pegar novos passageiros.

Para resolvê-lo deve-se usar princípios básico de programação concorrente.

O problema da Montanha Russa usa apenas três processos: a montanha russa, o processo main(), os passageiros e o(s) carro(s). Para facilitar o entendimento, sugiro usar para nomes das classes: MontanhaRussa(), Passageiro() e Carro().

O sistema não possui um "controlador" (ou a pessoa que controla a movimentação da montanha russa), isto é,  a função MontanhaRussa() apenas cria os carros e os passageiros. Depois disso, os Passageiro() e Carro() se autocontrolarão sozinhos, isto é, os passageiros saberão a hora de esperar na fila, entrar no carro, sair do carro e o carro saberá quando sair, conforme as condições foram atendidas.

Desenvolver um algoritmo concorrente e códigos para a montanha russa, o carro e os passageiros. Desenvolver uma solução para sincronizá-los usando exclusão mútua com espera bloqueada. Pense em escrever o código genérico, prevendo os demais casos....

Atenção: os tempos indicados não são realistas mas coerentes, para que o tempo de execução do programa seja tolerável (2-3 min).

##### Caso carro único

O primeiro caso é apenas para aquecimento...

Considere a montanha russa com apenas 1 (um) carro com C lugares. Considere n passageiros, que chegam repetidamente e esperam em uma fila na plataforma para entrar no carro, que pode acomodar C passageiros, sendo C < n.

O tempo de chegada dos n passageiros à montanha russa é Tp, que é aleatório. Atenção: os passageiros deverão ser criados pela função MonhanhaRussa() continuamente atendendo o tempo estabelecido. No entanto, o carro só pode partir e começar o passeio pelo trilho quando estiver cheio (existir o número de pessoas na fila suficiente para enche-lo). Considere um tempo Te como o tempo em que todos os passageiros embarquem e desembarquem do carro. O carro então inicia o passeio que leva um tempo Tm e quando chegar na plataforma, os passageiros saem e entram os novos passageiros.

Considere n = 52, C = 4, Te = 1 seg, Tm = 10 seg, Tp = 1 a 3 seg.

##### Caso 2 carros

Considere agora que existem m carros na montanha russa, sendo m> 1. Uma vez que existe apenas um trilho, os carros não podem passar sobre os outros, isto é, eles devem percorrer o trilho na ordem em que começou. Mais uma vez, um carro só pode sair quando estiver cheio.

Considere n = 92 , m = 2, C = 4, Te = 1 seg, Tm = 10 seg, Tp = 1 a 3 seg.

##### Caso 3 carros

Esse é o ultimo caso, três carros simultâneos.

Considere n = 148, m = 3, C = 4,  Te = 1 seg, Tm = 10 seg, Tp = 1 a 3 seg.

#### Descrição dos algoritmos

Temos parte do código sequencial, e parte do código concorrente, com a utilização de Threads. As partes sequenciais se tratam das quais se faz necessária uma ordem de execução definida, como a chegada de pessoas na fila da montanha russa, ou mesmo o embarque e o desembarque de passageiros do carro. Já as partes concorrentes se referem aos eventos de pessoas chegarem na fila, ao mesmo tempo que carros recebem ou deixam passageiros, bem como outros carros podem estar já em movimento nestes instantes.

Portanto, teremos 2 principais partes concorrentes, sendo uma destas multiplicada pela quantidade de carros, se tratando da corrida dos carros que estão cheios. Visualizando em pseudo-código, podemos ter a seguinte representação deste modelo:

```
função montanha_russa (parâmetros) {
  Thread (função carros () {
    Para cada carro: # Laço sequencial p/ manter a ordem dos carros
      esperar_esvaziar();
      esperar_embarque_passageiros();
      Thread(iniciar_corrida) # Feito como thread, para que o laço avance para o próximo carro na fila enquanto este está em sua corrida
  });

  Thread (função abrir_fila () {
    Para cada passageiro: # Chegada sequencial de passageiros na fila
      entrar_na_fila() # Tempo de chegada aleatório
  })
}
```

#### Descrição da implementação

O código consiste em 3 classes principais: [MontanhaRussa](#classe-montanha-russa), [Passageiro](#classe-passageiro) e [Carro](#classe-carro). Para a devida comunicação entre as Threads, são utilizadas variáveis (arrays) de acesso global, isto é, memória compartilhada para armazenar os passageiros inicializados, os passageiros na fila e os carros da montanha russa. Como mecanismo de exclusão mútua, é utilizada a espera bloqueada. Os detalhes de implementação de cada fluxo de funcionamento são descritos abaixo para cada classe.


##### Classe Montanha Russa

A classe de Montanha Russa tem a função exclusivamente de, dados os parâmetros de entrada, inicializar todos os carros e passageiros em suas devidas Threads. A partir de então, estes se autogerenciam. Recebe, como parâmetros de instanciamento, as variáveis de configuração do problema (n, m, C, Te, Tm e Tp).

A classe consiste nos métodos:

- inicializar()     : Cria os carros e passageiros
- abrir_fila()      : Função de Thread que insere passageiros na fila global.
- iniciar_carros()  : Thread que inicia os carros e suas Threads
- comecar()         : Inicia todas as Threads de Carros e Passageiros

##### Classe Passageiro

A classe Passageiro é responsável por colocar sua instância na fila global, no tempo de chegada deste passageiro (escolhido aleatoriamente dentre os possíveis valores de Tp), bem como por gerenciar seu embarque, consequentemente removendo-o da fila, e desembarque. Cada passageiro é identificado por um número de *ticket* único, gerado em sua inicialização pela Montanha Russa.

Seus métodos são:

- chegar()      : Coloca o passageiro na fila
- embarcar()    : Embarca o passageiro em um carro
- desembarcar() : Desembarca o passageiro de um carro

##### Classe Carro

A classe Carro é responsável por verificar constantemente a fila (espera ocupada) no aguardo por passageiros até que o embarque de C (sua capacidade) passageiros seja realizado. Então, realiza seu passeio dormindo por Tm segundos, de maneira concorrente, enquanto o próximo carro, quando houver, começa a aguardar mais passageiros. Ao término do passeio, a instância faz com que cada passageiro em sua lista de passageiros embarcados seja desembarcado, e então é liberado para mais passageiros entrarem.

Para permitir a interrupção da execução, seja no processo de execução ou após todos os passageiros da fila já terem andado e nenhum restar, foi necessária a utilização de uma variável booleana global *EXECUTANDO*, de forma a interromper a execução da Thread que, para cada carro, constantemente verifica novos passageiros na fila. Tal verificação é dada com um laço infinito (de condição igual à variável global mencionada), devido a impossibilidade, no Python, de forçar a "morte" de uma Thread. Tal mecanismo de segurança existe para evitar a possibilidade de deixar um recurso crítico aberto ou bloqueado.

Os métodos desta classe são:

- aguardar_passageiros()  : Espera ocupada até embarcar todos os C passageiros
- iniciar_passeio()       : Inicia o passeio da instância de Thread do Carro
    Suspende a Thread do carro por Tm segundos (passeio) e, em seguida, desembarca todos os seus passageiros

<hr>

#### Resultados

A execução da instância do problema ocorreu sem problemas (*deadlocks* ou *starvations*) para qualquer um dos casos. A única característica que pode ser considerada indesejada é a de que, dado o início do passeio (suspensão de um carro através do método time.sleep()), a execução do programa só conseguirá ser interrompida após a finalização deste passeio. A seguir mostramos alguns *logs* para cada caso requisitado na [formulação do problema](#formulação-do-problema).

##### Caso carro único

Parâmetros de entrada:
```
n = 52 , m = 1, C = 4, Te = 1 seg, Tm = 10 seg, Tp = 1 a 3 seg
```

<div style="display: flex;">
  <div style="flex: 50%; padding: 5px;">
    <img src="assets/results/results1_1.jpg" style="width: 100%">
  </div>
  <div style="flex: 50%; padding: 5px;">
    <img src="assets/results/results1_2.jpg" style="width: 100%">
  </div>
</div>

##### Caso 2 carros

Parâmetros de entrada:
```
n = 92 , m = 2, C = 4, Te = 1 seg, Tm = 10 seg, Tp = 1 a 3 seg
```

<div style="display: flex;">
  <div style="flex: 50%; padding: 5px;">
    <img src="assets/results/results2_1.jpg" style="width: 100%">
  </div>
  <div style="flex: 50%; padding: 5px;">
    <img src="assets/results/results2_2.jpg" style="width: 100%">
  </div>
</div>

##### Caso 3 carros

Parâmetros de entrada:
```
n = 148 , m = 3, C = 4, Te = 1 seg, Tm = 10 seg, Tp = 1 a 3 seg
```

<div style="display: flex;">
  <div style="flex: 50%; padding: 5px;">
    <img src="assets/results/results3_1.jpg" style="width: 100%">
  </div>
  <div style="flex: 50%; padding: 5px;">
    <img src="assets/results/results3_2.jpg" style="width: 100%">
  </div>
</div>

<hr>

### Referências

[1] **Elliot Forbes**. *Learning Concurrency in Python*. Packt Publishing: 2017.

[2] FERNÁNDEZ, Marcial. Problema da Montanha Russa. **Marcial Fernández**, 2021. Disponível em: <http://marcial.larces.uece.br/cursos/programacao-concorrente-e-paralela-2020-2/problema-da-montanha-russa>. Acesso em 12 de julho de 2021.
