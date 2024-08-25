nome = str(input("Nome do Aluno: "))
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a seunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
resultado = ("")
if media <= 0 or media == "":
    resultado = ("Media {}:, nome: {},"
                 "Voce ainda não somou nenhum ponto para ser mostrado"
                 .format(media, nome))
elif media >= 1 and media <= 6:
    resultado = ("Media {}:, nome: {} Você esta Reprovado".format(media, nome))
elif media == 7 and media <= 9:
    resultado = ("Media {}:, nome: {}, Parabéns!, Você esta Aprovado"
                 .format(media, nome))
elif media == 10:
    resultado = ("Media {}:, nome: '{}' Você conseguiu nota máxima"
                 .format(media, nome))
else:
    "Algo deu errado"
print(resultado)
