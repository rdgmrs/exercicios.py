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

delta = int(b)*int(b)-int(4*int(a)*int(c))
raiz_delta = int(delta ** 0.5)

print(f'o delta é: {delta}')
print(delta)
print(f'a raiz quadrada de {delta} é {raiz_delta}')

x1 =  (-int(b)+int(raiz_delta))/(int(2)*int(a))
print (f'resultado 1 é {x1}')
x2 =  (-int(b)-int(raiz_delta))/(int(2)*int(a))
print (f'resultado 2 é {x2}')

plt.scatter(x1,x2)
plt.show()
