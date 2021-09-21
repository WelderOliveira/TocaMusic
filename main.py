class tocaOSom:

    def __init__(self):
        self.lista_Musicas = []
        self.lista_Comandos = []

    def play(self):
        if len(self.lista_Musicas) >= 1:
            self.tocando = self.lista_Musicas[0]
        return self.tocando

    def next(self, musica):
        if musica in self.lista_Musicas and musica != self.tocando:
            for i in range(len(self.lista_Musicas)):
                self.tocando = self.lista_Musicas[i]
                self.proximaTocar = self.lista_Musicas[i + 1]
        return self.proximaTocar

    def adicionar_musica(self, musica):
        return self.lista_Musicas.append(musica)

    def deletar_musica(self, musica):
        return self.lista_Musicas.remove(musica)
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
        return self.lista_Musicas[0]

    def main(self):
        inp = input('Adicionar').split()
        # print(len(inp))
        if len(inp) > 1:
            # print("Entrei 1")
            comando, musica = inp
            self.adicionar_comando(comando)
            self.adicionar_musica(musica)
        elif len(inp) == 1:
            # print("Entrei 2")
            comando = inp
            # print(comando)
            if comando[0] == 'fight':
                print('Jedi Wagner, assuma o comando!')
                exit()
            elif comando[0] == 'list':
                self.listar()
            else:
                self.adicionar_comando(comando)
        # print(f'Antes{inp}')
        while inp[0] != 'fight':
            # print(f'Dps{inp[0]}')
            # print(inp)
            inp = input('tester').split()
            # print(inp)

            if len(inp) > 1:
                comando, musica = inp
                # print(comando)
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

            elif len(inp) == 1:
                comando = inp
                self.adicionar_comando(comando)
                if inp[0] == 'list':
                    self.listar()
        if inp[0] == 'fight':
            print('Jedi Wagner, assuma o comando!')
            exit()

        # listar()
        # print(self.lista_Musicas)
        # print(self.lista_Comandos)


ini = tocaOSom()
ini.main()
