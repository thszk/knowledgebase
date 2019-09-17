#!/usr/bin/python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

# -------------------------------------------------------------------------

# métodos de manipulação de grafos e buscas
class Grafo:

    def __init__(self, nomes):
        self.nomes = nomes
        self.grafo = [[0 for i in range(len(nomes))] for j in
                      range(len(nomes))]
        self.color = []
        self.d = []
        self.pi = []

    def busca_em_largura(self, primeiro_vertice):
        self.color = ['w' for u in range(len(self.grafo))]
        self.d = ['inf' for u in range(len(self.grafo))]
        self.pi = [None for u in range(len(self.grafo))]
        self.color[primeiro_vertice] = 'g'
        self.d[primeiro_vertice] = 0
        fila = []
        fila.append(primeiro_vertice)
        while fila != []:
            u = fila[0]
            for v in range(len(self.grafo)):
                if self.grafo[u][v] != 0:
                    if self.color[v] == 'w':
                        self.color[v] = 'g'
                        self.d[v] = self.d[u] + 1
                        self.pi[v] = u
                        fila.append(v)

            fila.pop(0)
            self.color[u] = 'b'

    def adicionar_relacao(
        self,
        origem,
        relacao,
        destino,
        ):
        index_origem = self.nomes.index(origem)
        index_destino = self.nomes.index(destino)
        self.grafo[index_origem][index_destino] = relacao

    def busca_por_all_all_all(self, checked):
        output = ''
        test = ''
        for origem in self.nomes:
            g.busca_em_largura(self.nomes.index(origem))
            for destino in self.nomes:
                index_destino = self.nomes.index(destino)
                if self.pi[index_destino] != None:
                    if not checked:
                        output = output + origem + ' ' \
                            + self.grafo[self.pi[index_destino]][index_destino] \
                            + ' ' + destino + '\n'
                    else:
                        output = output + origem
                        test2 = ''
                        while self.pi[index_destino] != None:
                            index_origem = self.pi[index_destino]
                            test2 = ' --' \
                                + self.grafo[index_origem][index_destino] \
                                + '--> ' + self.nomes[index_destino] \
                                + test2
                            index_destino = index_origem

                        output = output + test2 + '\n'
        return output

    def busca_por_all_all_destino(self, destino, checked):
        output = ''

        for origem in self.nomes:
            index_destino = self.nomes.index(destino)
            g.busca_em_largura(self.nomes.index(origem))
            if self.pi[index_destino] != None:
                if not checked:
                    output = output + origem + ' ' \
                        + self.grafo[self.pi[index_destino]][index_destino] \
                        + ' ' + destino + '\n'
                else:
                    output = output + origem
                    test2 = ''
                    while self.pi[index_destino] != None:
                        index_origem = self.pi[index_destino]
                        test2 = ' --' \
                            + self.grafo[index_origem][index_destino] \
                            + '--> ' + self.nomes[index_destino] + test2
                        index_destino = index_origem

                    output = output + test2 + '\n'

        return output

    def busca_por_all_relacao_all(self, relacao, checked):
        output = ''
        for origem in self.nomes:
            g.busca_em_largura(self.nomes.index(origem))
            for destino in self.nomes:
                index_destino = self.nomes.index(destino)
                if self.pi[index_destino] != None:
                    if self.grafo[self.pi[index_destino]][index_destino] \
                        == relacao:
                        if not checked:
                            output = output + origem + ' ' \
                                + self.grafo[self.pi[index_destino]][index_destino] \
                                + ' ' + destino + '\n'
                        else:
                            output = output + origem
                            test2 = ''
                            while self.pi[index_destino] != None:
                                index_origem = self.pi[index_destino]
                                test2 = ' --' \
                                    + self.grafo[index_origem][index_destino] \
                                    + '--> ' \
                                    + self.nomes[index_destino] + test2
                                index_destino = index_origem

                            output = output + test2 + '\n'

        return output

    def busca_por_all_relacao_destino(
        self,
        relacao,
        destino,
        checked,
        ):
        output = ''

        for origem in self.nomes:
            index_destino = self.nomes.index(destino)
            g.busca_em_largura(self.nomes.index(origem))
            if self.pi[index_destino] != None:
                if self.grafo[self.pi[index_destino]][index_destino] \
                    == relacao:
                    if not checked:
                        output = output + origem + ' ' \
                            + self.grafo[self.pi[index_destino]][index_destino] \
                            + ' ' + destino + '\n'
                    else:
                        output = output + origem
                        test2 = ''
                        while self.pi[index_destino] != None:
                            index_origem = self.pi[index_destino]
                            test2 = ' --' \
                                + self.grafo[index_origem][index_destino] \
                                + '--> ' + self.nomes[index_destino] \
                                + test2
                            index_destino = index_origem

                        output = output + test2 + '\n'

        return output

    def busca_por_origem_all_all(self, origem, checked):
        g.busca_em_largura(self.nomes.index(origem))
        output = ''
        for nome in g.nomes:
            index_destino = self.nomes.index(nome)
            if self.pi[index_destino] != None:
                if not checked:
                    output = output + origem + ' ' \
                        + self.grafo[self.pi[index_destino]][index_destino] \
                        + ' ' + nome + '\n'
                else:
                    output = output + origem
                    test2 = ''
                    while self.pi[index_destino] != None:
                        index_origem = self.pi[index_destino]
                        test2 = ' --' \
                            + self.grafo[index_origem][index_destino] \
                            + '--> ' + self.nomes[index_destino] + test2
                        index_destino = index_origem

                    output = output + test2 + '\n'

        return output

    def busca_por_origem_all_destino(
        self,
        origem,
        destino,
        checked,
        ):
        g.busca_em_largura(self.nomes.index(origem))
        index_destino = self.nomes.index(destino)
        output = ""
        if self.pi[index_destino] != None:
            if not checked:
                output = origem + ' ' \
                    + self.grafo[self.pi[index_destino]][index_destino] \
                    + ' ' + destino
            else:
                output = output + origem
                test2 = ''
                while self.pi[index_destino] != None:
                    index_origem = self.pi[index_destino]
                    test2 = ' --' \
                        + self.grafo[index_origem][index_destino] \
                        + '--> ' + self.nomes[index_destino] + test2
                    index_destino = index_origem

                output = output + test2 + '\n'

        return output

    def busca_por_origem_relacao_all(
        self,
        origem,
        relacao,
        checked,
        ):
        g.busca_em_largura(self.nomes.index(origem))
        output = ''
        for nome in g.nomes:
            index_nome = self.nomes.index(nome)
            if self.pi[index_nome] != None:
                if self.grafo[self.pi[index_nome]][index_nome] \
                    == relacao:
                    if not checked:
                        output = output + origem + ' ' \
                            + self.grafo[self.pi[index_nome]][index_nome] \
                            + ' ' + nome + '\n'
                    else:
                        output = output + origem
                        test2 = ''
                        while self.pi[index_destino] != None:
                            index_origem = self.pi[index_destino]
                            test2 = ' --' \
                                + self.grafo[index_origem][index_destino] \
                                + '--> ' + self.nomes[index_destino] \
                                + test2
                            index_destino = index_origem

                        output = output + test2 + '\n'

        return output

    def busca_por_origem_relacao_destino(
        self,
        origem,
        relacao,
        destino,
        checked,
        ):
        g.busca_em_largura(self.nomes.index(origem))
        output = ''
        index_destino = self.nomes.index(destino)
        if self.pi[index_destino] != None:
            if self.grafo[self.pi[index_destino]][index_destino] \
                == relacao:
                if not checked:
                    output = output + origem + ' ' \
                        + self.grafo[self.pi[index_destino]][index_destino] \
                        + ' ' + destino
                else:
                    output = output + origem
                    test2 = ''
                    while self.pi[index_destino] != None:
                        index_origem = self.pi[index_destino]
                        test2 = ' --' \
                            + self.grafo[index_origem][index_destino] \
                            + '--> ' + self.nomes[index_destino] + test2
                        index_destino = index_origem

                    output = output + test2 + '\n'

        return output

# -------------------------------------------------------------------------

# estrutura com todos nós da rede
nomes = [
    "bipede",
    "quadrupede",
    "pasto",
    "leite",
    "racao",
    "carne",
    "humano",
    "cao",
    "vaca",
    "glandula mamaria",
    "pelo",
    "mamifero",
    "respiracao cutanea",
    "anfibio",
    "pena",
    "ave",
    "pavao",
    "tuiuiu",
    "galinha",
    "vertebrado",
    "peixe",
    "reptil",
    "escama",
    "cobra",
    "animal",
    "invertebrado",
    "platelminto",
    "planaria",
    "agua",
    "pintado",
    "artropode",
    "escorpiao",
    "caranguejo",
    "pequenos animais aquaticos",
    "veneno",
    "inseto",
    "abelha",
    "mel",
    "polen"
]

# adiciona os nós ao grafo
g = Grafo(nomes)

# adiciona relacionamentos

# ligaçao tipo de animal
g.adicionar_relacao("vertebrado", "tipo de", "animal")
g.adicionar_relacao("invertebrado", "tipo de", "animal")

# ligacao eh vertebrado
g.adicionar_relacao("mamifero", "eh", "vertebrado")
g.adicionar_relacao("anfibio", "eh", "vertebrado")
g.adicionar_relacao("ave", "eh", "vertebrado")
g.adicionar_relacao('peixe', "eh", 'vertebrado')
g.adicionar_relacao('reptil', "eh", 'vertebrado')

# ligacao eh mamifero
g.adicionar_relacao('vaca', "eh", 'mamifero')
g.adicionar_relacao('cao', "eh", 'mamifero')
g.adicionar_relacao('humano', "eh", 'mamifero')

# ligacao mamifero possui
g.adicionar_relacao('mamifero', 'possui', 'pelo')
g.adicionar_relacao('mamifero', 'possui', 'glandula mamaria')

# ligacao humano come
g.adicionar_relacao('humano', 'come', 'carne')

# ligacao humano eh
g.adicionar_relacao('humano', 'eh', 'bipede')

# ligacao cao come
g.adicionar_relacao('cao', 'come', 'racao')

# ligacao cao eh
g.adicionar_relacao('cao', 'eh', 'quadrupede')

# ligacao vaca come
g.adicionar_relacao('vaca', 'come', 'pasto')

# ligacao vaca eh
g.adicionar_relacao('vaca', 'eh', 'quadrupede')

# ligacao vaca produz
g.adicionar_relacao('vaca', 'produz', 'leite')

# ligacao eh ave
g.adicionar_relacao('galinha', 'eh', 'ave')
g.adicionar_relacao('tuiuiu', 'eh', 'ave')
g.adicionar_relacao('pavao', 'eh', 'ave')

# liagcao ave possui
g.adicionar_relacao('ave', 'possui', 'pena')

# ligacao ave eh
g.adicionar_relacao('ave', 'eh', 'bipede')

# ligacao anfibio faz
g.adicionar_relacao('anfibio', 'faz', 'respiracao cutanea')

# ligacao eh peixe
g.adicionar_relacao('pintado', 'eh', 'peixe')

# ligacao peixe vive em
g.adicionar_relacao('peixe', 'vive em', 'agua')

# ligacao eh reptil
g.adicionar_relacao('cobra', 'eh', 'reptil')

# ligacao cobra come
g.adicionar_relacao('cobra', 'come', 'carne')

# ligacao reptil possui
g.adicionar_relacao('reptil', 'possui', 'escama')

# ligacao eh invertebrado
g.adicionar_relacao('inseto', 'eh', 'invertebrado')
g.adicionar_relacao('artropode', 'eh', 'invertebrado')
g.adicionar_relacao('platelminto', 'eh', 'invertebrado')

# ligacao eh inseto
g.adicionar_relacao('abelha', 'eh', 'inseto')

# ligacao abelha produz
g.adicionar_relacao('abelha', 'produz', 'mel')

# ligacao abelha come
g.adicionar_relacao('abelha', 'come', 'polen')

# ligacao eh artropode
g.adicionar_relacao('caranguejo', 'eh', 'artropode')
g.adicionar_relacao('escorpiao', 'eh', 'artropode')

# ligacao escorpiao produz
g.adicionar_relacao('escorpiao', 'produz', 'veneno')

# ligacao caranguejo come
g.adicionar_relacao('caranguejo', 'come', 'pequenos animais aquaticos')

# ligacao eh platelminto
g.adicionar_relacao('planaria', 'eh', 'platelminto')

# -------------------------------------------------------------------------

# interface gráfica
win = Tk()
win.title('Semantic Network')
win.geometry()
win.resizable(height=0, width=0)
title_1 = Label(win, text='Inferences')
title_1.grid(column=0, row=1, padx=50, pady=(25, 0))

opcoes = []
opcoes.append('All')
for nome in nomes:
    opcoes.append(nome)

l1 = Label(win, text='Subject')
l1.grid(column=0, row=2, padx=50, pady=(25, 0))
cb_subject = ttk.Combobox(win, values=opcoes, width=10)
cb_subject.grid(column=0, row=3, padx=50, pady=5)
cb_subject.current(0)

l2 = Label(win, text='Relation')
l2.grid(column=0, row=4, padx=50, pady=(25, 0))
cb_relation = ttk.Combobox(win, values=['All', 'tem', 'eh', 'come'], width=10)
cb_relation.grid(column=0, row=5, padx=50, pady=5)
cb_relation.current(0)

l3 = Label(win, text='Predicate')
l3.grid(column=0, row=6, padx=50, pady=(25, 0))
cb_predicate = ttk.Combobox(win, values=opcoes, width=10)
cb_predicate.grid(column=0, row=7, padx=50, pady=5)
cb_predicate.current(0)


def clicked_btn_1():
    txt.config(state=NORMAL)
    txt.delete(1.0, END)
    if cb_subject.get() == cb_predicate.get() and cb_subject.get() \
        != 'All':
        txt.insert(INSERT, 'Sujeito igual ao predicado!')
    else:
        if cb_subject.get() == 'All' and cb_relation.get() == 'All' \
            and cb_predicate.get() == 'All':
            txt.insert(INSERT, g.busca_por_all_all_all(chk_state.get()))
        elif cb_subject.get() == 'All' and cb_relation.get() == 'All' \
            and cb_predicate.get() != 'All':
            txt.insert(INSERT,
                       g.busca_por_all_all_destino(cb_predicate.get(),
                       chk_state.get()))
        elif cb_subject.get() == 'All' and cb_relation.get() != 'All' \
            and cb_predicate.get() == 'All':
            txt.insert(INSERT,
                       g.busca_por_all_relacao_all(cb_relation.get(),
                       chk_state.get()))
        elif cb_subject.get() == 'All' and cb_relation.get() != 'All' \
            and cb_predicate.get() != 'All':
            txt.insert(INSERT,
                       g.busca_por_all_relacao_destino(cb_relation.get(),
                       cb_predicate.get(), chk_state.get()))
        elif cb_subject.get() != 'All' and cb_relation.get() == 'All' \
            and cb_predicate.get() == 'All':
            txt.insert(INSERT,
                       g.busca_por_origem_all_all(cb_subject.get(),
                       chk_state.get()))
        elif cb_subject.get() != 'All' and cb_relation.get() == 'All' \
            and cb_predicate.get() != 'All':
            txt.insert(INSERT,
                       g.busca_por_origem_all_destino(cb_subject.get(),
                       cb_predicate.get(), chk_state.get()))
        elif cb_subject.get() != 'All' and cb_relation.get() != 'All' \
            and cb_predicate.get() == 'All':
            txt.insert(INSERT,
                       g.busca_por_origem_relacao_all(cb_subject.get(),
                       cb_relation.get(), chk_state.get()))
        elif cb_subject.get() != 'All' and cb_relation.get() != 'All' \
            and cb_predicate.get() != 'All':
            txt.insert(INSERT,
                       g.busca_por_origem_relacao_destino(cb_subject.get(),
                       cb_relation.get(), cb_predicate.get(),
                       chk_state.get()))

    txt.config(state=DISABLED)

def clicked_btn_2():
    # exibe a rede de forma dinamica

    DG = nx.DiGraph()
    DG.add_nodes_from(nomes)

    # adiciona relacionamento entre nós
    # ligaçao tipo de animal
    DG.add_edge("vertebrado", "animal")
    DG.add_edge("invertebrado", "animal")

    # ligacao eh vertebrado
    DG.add_edge("mamifero", "vertebrado")
    DG.add_edge("anfibio", "vertebrado")
    DG.add_edge("ave", "vertebrado")
    DG.add_edge('peixe', 'vertebrado')
    DG.add_edge('reptil', 'vertebrado')

    # ligacao eh mamifero
    DG.add_edge('vaca', 'mamifero')
    DG.add_edge('cao', 'mamifero')
    DG.add_edge('humano', 'mamifero')

    # ligacao mamifero possui
    DG.add_edge('mamifero', 'pelo')
    DG.add_edge('mamifero', 'glandula mamaria')

    # ligacao humano come
    DG.add_edge('humano', 'carne')

    # ligacao humano eh
    DG.add_edge('humano', 'bipede')

    # ligacao cao come
    DG.add_edge('cao', 'racao')

    # ligacao cao eh
    DG.add_edge('cao', 'quadrupede')

    # ligacao vaca come
    DG.add_edge('vaca', 'pasto')

    # ligacao vaca eh
    DG.add_edge('vaca', 'quadrupede')

    # ligacao vaca produz
    DG.add_edge('vaca', 'leite')

    # ligacao eh ave
    DG.add_edge('galinha', 'ave')
    DG.add_edge('tuiuiu', 'ave')
    DG.add_edge('pavao', 'ave')

    # liagcao ave possui
    DG.add_edge('ave', 'pena')

    # ligacao ave eh
    DG.add_edge('ave', 'bipede')

    # ligacao anfibio faz
    DG.add_edge('anfibio', 'respiracao cutanea')

    # ligacao eh peixe
    DG.add_edge('pintado', 'peixe')

    # ligacao peixe vive em
    DG.add_edge('peixe', 'agua')

    # ligacao eh reptil
    DG.add_edge('cobra', 'reptil')

    # ligacao cobra come
    DG.add_edge('cobra', 'carne')

    # ligacao reptil possui
    DG.add_edge('reptil', 'escama')

    # ligacao eh invertebrado
    DG.add_edge('inseto', 'invertebrado')
    DG.add_edge('artropode', 'invertebrado')
    DG.add_edge('platelminto', 'invertebrado')

    # ligacao eh inseto
    DG.add_edge('abelha', 'inseto')

    # ligacao abelha produz
    DG.add_edge('abelha', 'mel')

    # ligacao abelha produz
    DG.add_edge('abelha', 'mel')

    # ligacao abelha come
    DG.add_edge('abelha', 'polen')

    # ligacao eh artropode
    DG.add_edge('caranguejo', 'artropode')
    DG.add_edge('escorpiao', 'artropode')

    # ligacao escorpiao produz
    DG.add_edge('escorpiao', 'veneno')

    # ligacao caranguejo come
    DG.add_edge('caranguejo', 'pequenos animais aquaticos')

    # ligacao eh platelminto
    DG.add_edge('planaria', 'platelminto')

    # adicionando tipo de relacionamento
    labels = {
        # ligaçao tipo de animal
        ("vertebrado", "animal"): 'tipo de',
        ("invertebrado", "animal"): 'tipo de',

        # ligacao eh vertebrado
        ("mamifero", "vertebrado"): 'eh',
        ("anfibio", "vertebrado"): 'eh',
        ("ave", "vertebrado"): 'eh',
        ('peixe', 'vertebrado'): 'eh',
        ('reptil', 'vertebrado'): 'eh',

        # ligacao eh mamifero
        ('vaca', 'mamifero'): 'eh',
        ('cao', 'mamifero'): 'eh',
        ('humano', 'mamifero'): 'eh',

        # ligacao mamifero possui
        ('mamifero', 'pelo'): 'possui',
        ('mamifero', 'glandula mamaria'): 'possui',

        # ligacao humano come
        ('humano', 'carne'): 'come',

        # ligacao humano eh
        ('humano', 'bipede'): 'eh',

        # ligacao cao come
        ('cao', 'racao'): 'come',

        # ligacao cao eh
        ('cao', 'quadrupede'): 'eh',

        # ligacao vaca come
        ('vaca', 'pasto'): 'come',

        # ligacao vaca eh
        ('vaca', 'quadrupede'): 'eh',

        # ligacao vaca produz
        ('vaca', 'leite'): 'produz',

        # ligacao eh ave
        ('galinha', 'ave'): 'eh',
        ('tuiuiu', 'ave'): 'eh',
        ('pavao', 'ave'): 'eh',

        # liagcao ave possui
        ('ave', 'pena'): 'possui',

        # ligacao ave eh
        ('ave', 'bipede'): 'eh',

        # ligacao anfibio faz
        ('anfibio', 'respiracao cutanea'): 'faz',

        # ligacao eh peixe
        ('pintado', 'peixe'): 'eh',

        # ligacao peixe vive em
        ('peixe', 'agua'): 'vive em',

        # ligacao eh reptil
        ('cobra', 'reptil'): 'eh',

        # ligacao cobra come
        ('cobra', 'carne'): 'come',

        # ligacao reptil possui
        ('reptil', 'escama'): 'possui',

        # ligacao eh invertebrado
        ('inseto', 'invertebrado'): 'eh',
        ('artropode', 'invertebrado'): 'vive em',
        ('platelminto', 'invertebrado'): 'vive em',

        # ligacao eh inseto
        ('abelha', 'inseto'): 'eh',

        # ligacao abelha produz
        ('abelha', 'mel'): 'produz',

        # ligacao abelha produz
        ('abelha', 'polen'): 'come',

        # ligacao eh artropode
        ('caranguejo', 'artropode'): 'eh',
        ('escorpiao', 'artropode'): 'eh',

        # ligacao escorpiao produz
        ('escorpiao', 'veneno'): 'possui',

        # ligacao caranguejo come
        ('caranguejo', 'pequenos animais aquaticos'): 'come',

        # ligacao eh platelminto
        ('planaria', 'platelminto'): 'eh',
    }

    # seed é para nao ficar aleatorio, se nao tiver ele fica mudando a posicao toda hr,
    # cada valor que se troca muda o aleatorio que ficara fixo
    # k limita para nao ficar uma distancia muito proxima ou muito longe os vertices
    pos = nx.spring_layout(DG, seed=57, k=5)
    nx.draw_networkx_edge_labels(DG, pos, edge_labels=labels, width=1.0)
    nx.draw_networkx(DG, pos, with_labels=True, node_size=500, edge_color='black', font_size=10)
    plt.show()


btn_2 = Button(win, text='Show network', command=clicked_btn_2)
btn_2.grid(column=0, row=8, padx=50, pady=(25, 0))

btn = Button(win, text='Search', command=clicked_btn_1)
btn.grid(column=0, row=9, padx=50, pady=(5, 0))

chk_state = BooleanVar()
chk_state.set(False)  # set check state
chk = Checkbutton(win, text='Show path', var=chk_state)
chk.grid(column=0, row=10, padx=1, pady=(5, 0))

txt = scrolledtext.ScrolledText(win, width=50, height=10)
txt.insert(INSERT, 'Here are the inferences')
txt.grid(column=0, row=11, padx=50, pady=20)
txt.config(state=DISABLED)

win.mainloop()
