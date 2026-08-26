#Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar
#candidatos menores de 18 anos.
#● O programa deve pedir o Ano de Nascimento do candidato.
#● Se for menor de 18, o programa deve informar que ele não pode participar e pular
#a coleta dos demais dados (telefone, email etc) para esse candidato.
#● Se for maior de 18, o programa prossegue com o input() para os demais dados.


for i in range(12):
    print("Bem-vindo ao processo seletivo!")
    nome = input("DNome completo: ")
    nascimento = int(input("Ano de Nascimento: "))
    limite = 2008

    if nascimento > limite:
        print("Você não pode participar do processo seletivo.")
        continue

    telefone = input("Número de telefone]: ")
    email = input("E-mail: ")
    print("Candidato cadastrado com sucesso. Boa sorte!")