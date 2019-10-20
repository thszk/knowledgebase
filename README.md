# Base de Conhecimento

Esta implementação demonstra de forma simplificada o funcionamento de uma base de conhecimento usando busca não informada.


## Instalação

A implementação usa os softwares listados abaixo, com o comando para instalação individual em distribuições Linux (Debian, Ubuntu e derivados). Ou se preferir pode utilizar o script de instalação.

### Instalação Manual

- Python 3.7.3

```
  $ sudo apt install python3-dev
```

- pip 9.0.1

```
  $ sudo apt install python3-pip
  $ pip3 install setuptools
```

- TKinter 8.6

```
  $ sudo apt install python3-tk
```

- Matplotlib 3.1.0

```
  $ pip3 install matplotlib==3.1.0
```

- Networkx 2.3

```
  $ pip3 install networkx==2.3
```

- Pillow

```
  $ pip3 install Pillow
```

### Script de Instalação

Dê permissão de execução ao script:

```
  $ chmod +x src/install-dependencies.sh
```

Execute com permissão de root:

```
  $ sudo src/install-dependencies.sh
```


## Execução

Com o terminal aberto na pasta do projeto execute o comando:

```
  $ python3 src/semantic-network.py
```


## Como Utilizar

Ao iniciar o programa será exibida uma tela contendo 3 campos de seleção, esses campos estão identificados como Sujeito (Subject), Relação (Relation) e Predicado (Predicate), com botões de exibir a rede (Show network) em forma de diagrama gerado programaticamente, exibir imagem da rede (Show network image) para exibir o diagrama estático, Buscar (Search) a existência de relações entre nós e podendo também exibir o resultado através do caminho entre sujeito e predicado com sua relação(ões) (Show Path).

Ao clicar nos campos de seleção será exibida uma lista contendo nós e relações da base, pode ser clicado no item para o selecionar e depois no botão Buscar para procurar a ocorrência na rede semântica. Também é possível escrever nos campos para fazer a busca.

Exemplo de buscas:

- All - All - All : exibe todas as relações entre nós na rede

- Sujeito - All - All : exibe todas as relações que Sujeito tem com outros nós

- Sujeito - Relação - All : exibe todos os nós que Sujeito tem com a Relação especificada.

- Sujeito - Relação - Predicado : exibe a relação especificada, se existir.

- All - Relação - All : exibe todas Relações especificadas que existem na rede e seus nós.

Recursos auxiliares:

Está disponível uma representação da rede semântica em forma de diagrama no arquivo ``` ./resources/base.png``` , criado através da ferramenta online [draw.io](https://www.draw.io/). Esse recurso também pode ser visualizado clicando no botão ```Show network image``` pelo software.


## Sistemas Operacionais Suportados

Debian GNU/Linux 10 (Buster)*

Ubuntu 16.04 LTS ou superior*

Windows 10*

*(Com todas as bibliotecas e dependências devidamente instaladas.)


## Desenvolvedores

André Luiz Santana Treu Afonso | contato: ra166034@ucdb.br

João Luiz Aguiar Takayama | contato: ra165631@ucdb.br

Thiago Suzuqui Lodi | contato: ra165478@ucdb.br

## Estrutura de diretórios

src/ - contém o código fonte do projeto e script para instalação de dependências

resources/ - contém o executável do programa draw.io, arquivo para edição do diagrama e imagem png do diagrama.