'''
idade = int(input("Digite a idade: "))
if idade < 16:
    print("Não Pode Votar")
elif idade >= 16 and idade < 18:
    print("Voto Facultativo")
elif idade >= 18 and idade < 70:
    print ("Voto Obrigadotório")
else:
    print ("Voto Facultativo")

print("\n\n")
print("----------------X---------------")
print("\n")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

maior = n1 if n1 > n2 else n2

print("O maior número é: " + str(maior))
print("\n")

nome = str(input("Digite o seu nome: "))
print("Muito prazer, {}!".format(nome))

print("\n")

n1 = int(input("Digite um número: \n"))
n2 = int(input("Digite outro número: \n"))
s = n1 + n2
print('A soma entre {} e {} é {}'.format(n1, n2, s))

print('\n')

mont = float(input('Digite o valor em Reais: '))
dol = mont/4.20
print('Com R$ {} você pode comprar US$ {:.2f}'.format(mont, dol)) 

print('\n')

print ('------Antecessor e Sucessor-----')
n = int (input("Digite um número  "))
a = n-1
s = n+1
print ('Com base no número digitado ({}), seu antecessor é {}, e seu sucessor é {}'.format (n, a, s))

print('\n')

print ('---Dobro, Triplo, Raiz Quadrada---')
n = int(input('Digite um número para realizarmos o cálculo:  '))
d = n * 2
t = n * 3
rq = pow (n, (1/2))
print('O número digitado foi: ', n)
print('O dobro é: {} \nO triplo é: {} \nA raiz quadrada é: {:.2f}'.format(d, t, rq))
'''
print('\n')

print('----Média do aluno----')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A média do aluno é: {:.2f}'.format(m))

