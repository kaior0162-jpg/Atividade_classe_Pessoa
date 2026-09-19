class Aluno:

    def __init__(self, nome, matricula, nota1, nota2, nota3, nota4, nota5):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5

    def caucular_media(self):
        soma = self.nota1 + self.nota2 + self.nota3 + self.nota4 + self.nota5
        self.media = soma/5

        return self.media

    def verificar_situacao(self):
        media = self.caucular_media()
        if media >= 7:
            print(f"O {self.nome} foi aprovado. ")

        else:
            print(f"O {self.nome} foi reprovado. ")


Carlin = Aluno("Carlin",555, 6, 3, 5, 8, 9)
Camundongo = Aluno("Camundongo", 4444, 6, 5, 7, 8,2)

#Carlin.caucular_media()
Carlin.verificar_situacao()