class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes'

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)


vingadores = Filme('Vingadores Guerra Infinita', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
tmep = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Está na playlist? {demolidor in playlist_fim_de_semana}')
