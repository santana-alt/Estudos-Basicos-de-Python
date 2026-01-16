#Faça um programa que receba dois valores inteiros (a e b), e faça a divisão de a por b SEM UTILIZAR o operador / ou //. 
# Obs.: considere sempre que a >= b

a = int(input())
b = int(input())
resposta = 0

while a >= b:
  a-=b
  resposta += 1
print(resposta)