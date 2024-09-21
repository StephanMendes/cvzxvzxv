import random

class Jokenpo:
    def __init__(self, jogador1: int, jogador2: bool = False):
        self.opcoes = {
            1:"Pedra",
            2:"Papel",
            3:"Tesoura",
            4:"Lagarto",
            5:"Spock"
        }
        
        self.resultados = {
            (3, 2): "Tesoura corta papel",          # Tesoura vence papel
            (2, 1): "Papel cobre pedra",            # Papel vence pedra
            (1, 4): "Pedra esmaga lagarto",         # Pedra vence lagarto
            (4, 5): "Lagarto envenena Spock",       # Lagarto vence Spock
            (5, 3): "Spock esmaga tesoura",         # Spock vence tesoura
            (3, 4): "Tesoura decapita lagarto",     # Tesoura vence lagarto
            (4, 2): "Lagarto come papel",           # Lagarto vence papel
            (2, 5): "Papel refuta Spock",           # Papel vence Spock
            (5, 1): "Spock vaporiza pedra",         # Spock vence pedra
            (1, 3): "Pedra amassa tesoura"          # Pedra vence tesoura
        }
        
        self.jogador1 = jogador1
        self.jogador2 = jogador2 or random.randint(1, 5)
    
    
    def tela_jogo(self):
        print(self.opcoes_jogo())
        print(self.escolhas_feitas())
        print(self.resultado_jogo())
    
    
    def opcoes_jogo(self):
        return '''[1]: Pedra\n[2]: Papel\n[3]: Tesoura\n[4]: Lagarto\n[5]: Spock '''
    
    
    def escolhas_feitas(self):
        return f"\nO Pc escolheu: {self.opcoes.get(self.jogador2)}\nO Jogador escolheu: {self.opcoes.get(self.jogador1)}\n"
    
    
    def resultado_jogo(self):
        if self.jogador2 == self.jogador1:
            print("Empate")
        else:
            resultado = self.resultados.get((self.jogador1, self.jogador2)) or self.resultados.get((self.jogador2, self.jogador1))
            if resultado:
                if self.resultados.get((self.jogador1, self.jogador2)):
                    return f"O Jogador Ganhou!\n{resultado}"
                else:
                    return f"O Jogador Perdeu!\n{resultado}"
            else:
                return "Resultado inválido"

if __name__ == "__main__":
    start = Jokenpo(
        jogador1=1
    )
    
    start.tela_jogo()