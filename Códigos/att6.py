turno=input("digite a letra m ou v ou n para saber o seu turno: ")

if turno== 'm' or turno== 'M':
    print(f"o seu turno digitado a cima {turno} é Matutino")
elif turno== 'v' or turno== 'V':
    print(f"o seu turno digitado a cima {turno} é Vesperino")
elif turno == 'n' or turno== 'N':
    print(f"o turno digitado a cima {turno} é Noturno")
else:
    print(f"turno digitado {turno} Não Existe")