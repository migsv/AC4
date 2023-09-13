from time import sleep
#Elabore uma função e_primo(num) que retorna se um número num é primo ou não. 
#Caso num não seja primo, liste todos os números pelos quais num é divisível.


def e_primo(num):
    resultado = num
    if num == 2:
        return resultado
print('-'*80)
nm = int(input('Digite aqui um número: '))
multiplo = 0
print('-'*80)
print(f'O número {nm} é multiplo de: ')
for conta in range(1, nm + 1):
    if nm % conta == 0:
        print('multiplo de', conta)
        multiplo += 1
resultado = e_primo(multiplo)
print('')
if resultado == 2:
    print('É primo!')
else:
    print('Não é primo!')
print('')
#Faça um programa que receba o valor de uma dívida e mostre as opções de parcelamento. 
# O resultado final deve conter as opções de 1, 3, 6, 9 ou 12 parcelas, 
# e o percentual de juros para cada parcela deve ser determinado conforme a primeira tabela, abaixo. 
# O relatório com as opções de pagamento deve conter os seguintes dados: valor dos juros, valor total da dívida (incluindo juros), 
# quantidade de parcelas e valor da parcela. A segunda tabela, abaixo, mostra um exemplo de como o resultado deve ser exibido. 
# No momento, não é necessário formatar os valores.

sleep(3)
print('-'*80)
print('')
print('Calculadora de dívida')
print('')
print('-'*80)


def cal_divida(divida):
    print('N° de parcelas:')
    print('')
    for cal1 in range(1, 2):
        print('Parcela(s) de', cal1)
    for cal2 in range(3, 13, 3):
        print('Parcela(s) de', cal2)
    print(' ')
    print('Valor dos juros:')
    print(' ')
    for juros in range(10, 26, 5):
        print('Juros de', juros)
    print(' ')
    juros_10 = divida * 0.10
    juros_15 = divida * 0.15
    juros_20 = divida * 0.20
    juros_25 = divida * 0.25
    divida_final10 = round((divida + juros_10)/3, 2)
    divida_final15 = round((divida + juros_15)/6, 2)
    divida_final20 = round((divida + juros_20)/9, 2)
    divida_final25 = round((divida + juros_25)/12, 2)
    print('-'*80)
    print(f'Valor dos juros: 0 \nValor total: {divida} \nQuantidade de parcelas: 1 \nValor de parcela: {divida}')
    print('-'*80)
    print(f'Valor dos juros {juros_10} \nValor total {divida + juros_10} \nQuantidade de parcelas 3 \nValor de parcela {divida_final10}')
    print('-'*80)
    print(f'Valor dos juros {juros_15} \nValor total {divida + juros_15} \nQuantidade de parcelas 6 \nValor de parcela {divida_final15}')
    print('-'*80)
    print(f'Valor dos juros {juros_20} \nValor total {divida + juros_20} \nQuantidade de parcelas 9 \nValor de parcela {divida_final20}')
    print('-'*80)
    print(f'Valor dos juros {juros_25} \nValor total {divida + juros_25} \nQuantidade de parcelas 12 \nValor de parcela {divida_final25}')
cal_divida(1000)

#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
# [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

print('')
print('-'*80)


print('Leitor de números entre valores')

print('-'*80)

itvl_020 = 0
itvl_2650 = 0
itvl_5175 = 0
itvl_76100 = 0
while True: 
    numero = int(input('Diga um número (para finalizar o programa digite um valor negativo): '))
    if numero < 0:
        print('Não há')
        break
    elif 0 <= numero <= 25:
        itvl_020 += 1
    elif 26 <= numero <= 50:
        itvl_2650 += 1
    elif 51 <= numero <= 75:
        itvl_5175 += 1
    elif 76 <+ numero <= 100:
        itvl_76100 += 1
print(f'A quantidade de números presentes entre o intervalo de [0-20] é de {itvl_020}')
print(f'A quantidade de números presentes entre o intervalo de [26-50] é de {itvl_2650}')
print(f'A quantidade de números presentes entre o intervalo de [51-75] é de {itvl_5175}')
print(f'A quantidade de números presentes entre o intervalo de [76-100] é de {itvl_76100}')
