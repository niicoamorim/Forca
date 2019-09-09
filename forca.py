import random

tabuleiro = ['''
>>>>>>>>>>>FORCA<<<<<<<<<<<

+-----+            
|     |
      | 
      | 
      | 
      |
==============''','''
>>>>>>>>>>>FORCA<<<<<<<<<<<

+-----+            
|     |
O     | 
      | 
      | 
      |
==============''','''
>>>>>>>>>>>FORCA<<<<<<<<<<<

+-----+            
|     |
O     | 
|     | 
      | 
      |
==============''','''
>>>>>>>>>>>FORCA<<<<<<<<<<<

 +-----+            
 |     |
 O     | 
/|     | 
       | 
       |
 ==============''','''
>>>>>>>>>>>FORCA<<<<<<<<<<<

 +-----+            
 |     |
 O     | 
/|\    | 
       | 
       |
 ==============''','''
>>>>>>>>>>>FORCA<<<<<<<<<<<

 +-----+            
 |     |
 O     | 
/|     | 
/      | 
       |
 ==============''','''
>>>>>>>>>>>FORCA<<<<<<<<<<<

 +-----+            
 |     |
 O     | 
/|\    | 
/ \    | 
       |
 ==============''',]

class Forca:

    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_errada = []
        self.letras_certas = []

    def adv_letra(self, letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_errada:
            self.letras_errada.append(letra)
        else:
            return False
        return True

    def final_jogo(self):
        return self.venceu() or (len(self.letras_errada) == 6)

    def venceu(self):
        if '_' not in self.esconder_palavra():
            return True
        return False

    def esconder_palavra(self):
        verif = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                verif += '_'
            else:
                verif += letra
        return verif

    def mostrar_status(self):
        print(tabuleiro[len(self.letras_errada)])
        print('\nPalavra :' + self.esconder_palavra())
        print('\Letras erradas')
        for letra in self.letras_errada:
            print(letra,)
        print()
        for letra in self.letras_certas:
            print(letra,)


def gerar_palavra():
        with open('palavras.txt', 'rt') as p:
            bank = p.readlines()
        return bank[random.randint(0, len(bank))].strip()


def main():

    jogo = Forca(gerar_palavra())

    while not jogo.final_jogo():
        jogo.mostrar_status()
        letra_digitada = input('Digite uma letra')
        jogo.adv_letra(letra_digitada)

    jogo.mostrar_status()

    if jogo.venceu():
        print('\nAí ta certo. Venceu!')
    else:
        print('\nPerdeu, zé mané.')
        print(f'A palavra era {jogo.palavra}.')


if __name__ == "__main__":
    main()