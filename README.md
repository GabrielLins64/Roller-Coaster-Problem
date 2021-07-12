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

### Sumário

- [Sumário](#sumário)
- [Descrição](#descrição)
  - [Introdução](#introdução)
  - [Proposta do Problema](#proposta-do-problema)
    - [Caso carro único](#caso-carro-único)
    - [Caso 2 carros](#caso-2-carros)
    - [Caso 3 carros](#caso-3-carros)
- [Instalação (Linux)](#instalação-linux)
- [Relatório](#relatório)
  - [Formulação do problema](#formulação-do-problema)
  - [Descrição dos algoritmos](#descrição-dos-algoritmos)
  - [Descrição da implementação](#descrição-da-implementação)
    - [Classe Montanha](#classe-montanha)
    - [Classe Passageiro](#classe-passageiro)
    - [Classe Carro](#classe-carro)
  - [Resultados](#resultados)
- [Referências](#referências)

<hr>

### Descrição

Trabalho acadêmico da disciplina de Programação Concorrente e Paralela. Consiste na implementação, em *Python*, da resolução do problema de concorrência *Roller Coaster*.

#### Introdução

O Problema da Montanha Russa (Roller Coaster) é um exemplo lúdico de um problema muito comum em controle de processos. O problema simula uma montanha russa onde pessoas entram na fila esperando a vez, depois entram no carro, que quando estiver cheio, parte para a viagem até retornar para pegar novos passageiros.

Para resolvê-lo deve-se usar princípios básico de programação concorrente.

#### Proposta do Problema

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

**3.** Dentro do diretório raiz do projeto, crie um ambiente virtual *Python* para instalar as dependências do projeto:

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

### Relatório

#### Formulação do problema

#### Descrição dos algoritmos

#### Descrição da implementação

##### Classe Montanha

##### Classe Passageiro

##### Classe Carro

<hr>

#### Resultados

<hr>

### Referências

[1] **Elliot Forbes**. *Learning Concurrency in Python*. Packt Publishing: 2017.
