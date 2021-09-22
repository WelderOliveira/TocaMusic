class tocaOSom:

    def __init__(self):
        self.a = True
        self.resultado = []
        self.tocando = []
        self.lista_Musicas = []
        self.lista_Comandos = []

    def play(self):
        if len(self.lista_Musicas) >= 1:
            # while True:
            #     for x in range(len(self.lista_Musicas)):
                # while not self.end:
            self.tocando = self.lista_Musicas[0]
        return self.tocando

    def next(self, musica):
        if musica in self.lista_Musicas and musica != self.tocando:
            i = self.lista_Musicas.index(musica)
            self.lista_Musicas.pop(i)
            self.lista_Musicas.insert(1, musica)

    def adicionar_musica(self, musica):
        return self.lista_Musicas.append(musica)

    def deletar_musica(self, musica):
        try:
            return self.lista_Musicas.remove(musica)
        except:
            pass
        # pass

    def adicionar_comando(self, comando):
        # Stack
        return self.lista_Comandos.insert(0, comando)

    def desfazer(self, comando):
        pass

    def listar(self):
        if len(self.lista_Musicas) != 0:
            print(*self.lista_Musicas, sep=',')
        else:
            print('[vazia]')
        # return

    def current(self):
        if not self.tocando:
            print("Toque! Toque, Dijê!")
        else:
            print(self.tocando)

    def checagemComando(self, comando, musica):
        if comando == 'add':
            self.adicionar_comando(comando)
            self.adicionar_musica(musica)

        if comando == 'del':
            # comando, musica = inp
            self.adicionar_comando(comando)
            self.deletar_musica(musica)

        if comando == 'next':
            self.adicionar_comando(comando)
            self.next(musica)

    def main(self):
        while self.a:
            inp = str(input('')).split()

            if len(inp) > 1:
                comando, musica = inp
                self.checagemComando(comando, musica)

            elif len(inp) == 1:
                comando = inp
                self.adicionar_comando(comando)
                if comando[0] == 'list':
                    self.listar()
                if comando[0] == 'play':
                    self.play()
                if comando[0] == 'fight':
                    self.a = False
                if comando[0] == 'current':
                    self.current()

        # for _ in self.lista_Comandos:
        #     print(_)
        print('Jedi Wagner, assuma o comando!')


ini = tocaOSom()
ini.main()
