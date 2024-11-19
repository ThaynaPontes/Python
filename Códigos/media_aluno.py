media = float(input("Digite a nota média do aluno: "))

if media >= 6:
    print(f"Aluno com média {media} está Aprovado")
elif media <= 4:
    print(f"Aluno com média {media} está reprovado")
else:
    print(f"Aluno com média {media} está em recuperação")
    