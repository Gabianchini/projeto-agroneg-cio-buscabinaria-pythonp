Busca binária Python


def busca_binaria(vacascadastradas, minimo, maximo, buscar):


    if maximo < minimo:
        return -1
    meio = (minimo + maximo) // 2
    if vacascadastradas[meio] == buscar:
        return meio
    elif vacascadastradas[meio] > buscar:
        return busca_binaria(vacascadastradas, minimo, meio - 1, buscar)
    else:
        return busca_binaria(vacascadastradas, meio + 1, maximo, buscar)

vacascadastradas = [1, 2, 3, 4, 5, 6, 7, 8]
nomevacas = ['Judite', 'Mimosa', 'Claudinha', 'Lurdes','Munique','Lolo','Gordinha','Fifi']


codigo = input('Digite o codigo para pesquisar: ')
vaca_procurada = int(codigo)
busca_binaria(vacascadastradas, 0, len(vacascadastradas) - 1, vaca_procurada)

resposta = busca_binaria(vacascadastradas, 0, len(vacascadastradas) - 1, vaca_procurada)
if(int(resposta) != -1):
    print('Sua busca retornou: ', nomevacas[int(resposta)])
else:
    print('Nada foi encontrado!')
