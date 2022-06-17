#projeto formula de bhaskara
import matplotlib.pyplot as plt




#inserindo dados
print("insira a,b,c para descobrir x ou seja as raizes")
print("insira o coeficiente quadratico: a ")
a = input()
print(f'você designou {a} para(com os sinal de -se negativo):a')
print("insira o coeficiente linear(com os sinal de + ou -): b ")
b = input()
print(f'você designou {b} para: b')
print("insira o coeficiente constante(com os sinal de + ou -): c")
c = input()
print(f'você designou {c} para : c')


print(f'sua função do segundo grau é: {a}.x²{b}x{c}=0')

###############################

delta = float(b)*float(b)-float(4*float(a)*float(c))
raiz_delta = float(delta ** 0.5)

print(f'o delta é: {delta}')
print(delta)
print(f'a raiz quadrada de {delta} é {raiz_delta}')

x1 =  (-float(b)+float(raiz_delta))/(float(2)*float(a))
print (f'resultado 1 é {x1}')
x2 =  (-float(b)-float(raiz_delta))/(float(2)*float(a))
print (f'resultado 2 é {x2}')

plt.scatter(x1,x2)
plt.show()
