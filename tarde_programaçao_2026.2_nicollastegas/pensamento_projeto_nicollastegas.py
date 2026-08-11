'''
>>projeto açaiteria:



'''



# Ufa, quebrei a maldiçao
# print('Olá Mundo!')

print('_' * 48 + '\n')
print('Bem-vindo ao Sistema de vendas - açaiteria!\n')
print('1 - cadastrar produto')
print('2 - listar produtos')
print('3 - Realizar venda')
print('4 - combos de açai')
print('5 - bebidas')
print('6 - sobre nos')
print('7 -  fale conosco')
print('8 - envie seu feedback')
print('9 - recomendaçoes')
print('0 - Sair Do Sistema')
print('\n-------------------------------\n')

opçao_definida = int(input('digite a opçao desejada '))

if opçao_definida == 1:
 print('cadastrando produto...')

elif opçao_definida == 2:
    print('listando produtos...')

elif opçao_definida == 3:
    print('realizando a venda...')

elif opçao_definida == 4:
   print('combos de açai...')

elif opçao_definida == 5:
   print('bebidas...')

elif opçao_definida == 6:
    print('sobre nós...')

elif opçao_definida == 7:
    print('fale conosco...')

elif opçao_definida == 8: 
   print('envie seu feedback...')

elif opçao_definida == 9: 
   print('recomendaçoes...')

elif opçao_definida == 0:
    print('saindo do sistema...') 

else: print('opçao invalida, escolha novamente!')