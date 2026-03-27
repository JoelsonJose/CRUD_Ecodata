teste = input('Qual número você quer saber se é ')

from tabulate import tabulate


menu = '''
======================================
      ♻️ CADASTRO DE LIXEIRAS
======================================

Seja bem vindo ao menu de cadastro
Selecione a opção desejada:

[1] Inserir
[2] Listar
[3] Atualizar
[4] Deletar

========================= Ecodata ====
'''

lixeiras = {}


def inserir():
    print('============================================')
    print('         🗑️ CADASTRAR NOVA LIXEIRA         ')
    print('============================================\n')
    numeroSerie = input('Qual o número de série da lixeira? ')

    if numeroSerie in lixeiras:
        print(f'⚠️ Já existe uma lixeira cadastrada com o número de série {numeroSerie}.')
        return

    endereco = input('Qual o endereço que a lixeira foi instalada? ')
    situacao = input('Qual a SITUAÇÃO atual da lixeira (Ativa/Inativa/Cheia/Em Manutenção)? ')
    dataInstalacao = input('Qual a data de instalação da lixeira (DD/MM/AAAA)? ')
    capacidade = input('Qual a CAPACIDADE da lixeira (em litros)? ')

    lixeiras[numeroSerie] = {
        'Número de Série': numeroSerie,
        'Endereço': endereco,
        'Situação': situacao,
        'Data de Instalação': dataInstalacao,
        'Capacidade': capacidade
    }

    print(f'\n✅ A lixeira com número de série {numeroSerie} foi cadastrada com sucesso!')
    print('Voltando para o Menu de cadastro...')



def listar():
    print('============================================')
    print('          📝 LISTAR LIXEIRAS              ')
    print('============================================')
    if not lixeiras:
        print("⚠️ Nenhuma lixeira cadastrada.")
        return

    print("\n📋 Lista de Lixeiras Cadastradas:\n")
    tabela = []

    for numeroSerie, dados in lixeiras.items():
        linha = [
            numeroSerie,
            dados.get('Endereço', ''),
            dados.get('Situação', ''),
            dados.get('Data de Instalação', ''),
            dados.get('Capacidade', '')
        ]
        tabela.append(linha)

    cabecalho = ["Número de Série", "Endereço", "Situação", "Data de Instalação", "Capacidade"]
    print(tabulate(tabela, headers=cabecalho, tablefmt="fancy_grid"))


def atualizar():
    print('============================================')
    print('          ✏️ ATUALIZAR LIXEIRA              ')
    print('============================================')
    numeroSerie = input('Digite o número de série da lixeira que deseja atualizar: ')
    if numeroSerie not in lixeiras:
        print('⚠️ Lixeira não encontrada.')
        return

    print('\nCampos disponíveis para atualização:')
    print('[1] Número de Série')
    print('[2] Endereço')
    print('[3] Situação')
    print('[4] Data de Instalação')
    print('[5] Capacidade')

    opcao = input('\nEscolha o número correspondente ao campo que deseja atualizar: ')

    if opcao == '1':
        novoNumero = input('Digite o novo número de série: ')
        if novoNumero in lixeiras:
            print('⚠️ Já existe uma lixeira com esse número de série.')
        else:
            lixeiras[novoNumero] = lixeiras.pop(numeroSerie)
            lixeiras[novoNumero]['Número de Série'] = novoNumero
            print('✅ Número de série atualizado com sucesso!')

    elif opcao == '2':
        novoEndereco = input('Digite o novo endereço: ')
        lixeiras[numeroSerie]['Endereço'] = novoEndereco
        print('✅ Endereço atualizado com sucesso!')

    elif opcao == '3':
        novaSituacao = input('Digite a nova situação: ')
        lixeiras[numeroSerie]['Situação'] = novaSituacao
        print('✅ Situação atualizada com sucesso!')

    elif opcao == '4':
        novaData = input('Digite a nova data de instalação: ')
        lixeiras[numeroSerie]['Data de Instalação'] = novaData
        print('✅ Data de instalação atualizada com sucesso!')

    elif opcao == '5':
        novaCapacidade = input('Digite a nova capacidade: ')
        lixeiras[numeroSerie]['Capacidade'] = novaCapacidade
        print('✅ Capacidade atualizada com sucesso!')

    else:
        print('⚠️ Opção inválida.')


def Deletar():
    print('============================================')
    print('           ❌ DELETAR LIXEIRA               ')
    print('============================================')
    numeroSerie = input('Digite o número de série da lixeira que deseja deletar: ')
    if numeroSerie not in lixeiras:
        print('⚠️ Lixeira não encontrada.')
        return

    print('\nO que deseja deletar:')
    print('[1] Deletar toda a lixeira')
    print('[2] Deletar alguns dados da lixeira')

    opcao = input('Escolha uma opção: ')

    if opcao == "1":
        confirmacao = input('Tem certeza que deseja deletar toda a lixeira (Sim/Não)? ')
        if confirmacao.lower() == 'sim':
            del lixeiras[numeroSerie]
            print('✅ Lixeira removida com sucesso!')
        else:
            print('❌ Ação cancelada.')

    elif opcao == "2":
        print('\nCampos disponíveis para deletar:')
        print('[1] Endereço')
        print('[2] Situação')
        print('[3] Data de Instalação')
        print('[4] Capacidade')

        campo = input('\nEscolha o número correspondente ao campo que deseja deletar: ')

        if campo == "1":
            lixeiras[numeroSerie]['Endereço'] = ""
            print('✅ Endereço deletado com sucesso!')

        elif campo == "2":
            lixeiras[numeroSerie]['Situação'] = ""
            print('✅ Situação deletada com sucesso!')

        elif campo == "3":
            lixeiras[numeroSerie]['Data de Instalação'] = ""
            print('✅ Data de instalação deletada com sucesso!')

        elif campo == "4":
            lixeiras[numeroSerie]['Capacidade'] = ""
            print('✅ Capacidade deletada com sucesso!')

        else:
            print('⚠️ Opção inválida.')


while True:
    opcao = input(menu)
    if opcao == "1":
        inserir()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        Deletar()
    else:
        print("⚠️ Opção inválida.")
