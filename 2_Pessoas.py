"""Criando a CLASSE Pessoa"""
class Pessoa:
    def __init__(self, n, i, p, a):
        self.nome = n
        self.idade = i
        self.peso = p
        self.altura = a

    def apresentacao(self):
        print(f"O nome da pessoa consultada é {self.nome}; \nA idade dele(a) é: {self.idade};")

    def fazer_aniversario(self):
        self.idade +=1
        print(f"Feliz aniversario, {self.nome}!!! Sua nova idade agora é:{self.idade}.")


pessoa1 = Pessoa("Grace", 30. 55, 1.60)
pessoa2 = Pessoa("Alan", 25, 70, 1.80)

"""Chamando os métodos"""

pessoa1.apresentacao() 
pessoa1.fazer_aniversario()
pessoa1.apresentacao()
