import PySimpleGUI as sg
sg.set_options(font=('', 13))
# DADOS DO ESTUDO SOBRE OS ABSORVENTES
ciclo_anual_absorvente_desc = 195
ciclo_anual_coletor = 1
carbono_ciclo_anual_absorvente_desc = 20.19
carbono_ciclo_anual_coletor = 1.77

# DADOS DO PROGRAMA DE PROTEÇÃO E PROMOÇÃO À DIGNIDADE MENSTRUAL
valor_investido = 140446368
valor_medio_absorvente_descartavel = 16
valor_medio_coletor = 69.90

# CÁLCULO
nova_porcentagem_comp = 48

numero_absorventes_descartaveis = round(valor_investido / valor_medio_absorvente_descartavel)
numero_absorventes_descartaveis = round(numero_absorventes_descartaveis * 8) #8 unidades de absorvente
numero_coletor = round(valor_investido / valor_medio_coletor)

pegada_carbono_absorvente_desc = (numero_absorventes_descartaveis * carbono_ciclo_anual_absorvente_desc) / ciclo_anual_absorvente_desc
pegada_carbono_coletor = (numero_coletor * carbono_ciclo_anual_coletor) / 1
porcentagem_comp = (pegada_carbono_coletor / pegada_carbono_absorvente_desc) * 100
creditos_absorvente_desc = pegada_carbono_absorvente_desc / 1000 * 37

sg.theme('SystemDefaultForReal')

layout = [
    [sg.Text("Bem-vindo ao Simulador de Pegada de Carbono da Distribuição do Programa de Proteção e Promoção da Dignidade Menstrual!", font=('', 13, "bold"), text_color='#F3A2A7')],
    [sg.Text("Resultado da Simulação:", font=('', 13, "bold"))],
    [sg.Text(f"A pegada de carbono de {numero_absorventes_descartaveis:.2f} absorventes descartáveis distribuídos pelo programa do governo é de {pegada_carbono_absorvente_desc:.2f}kg.")],
    [sg.Text(f"A pegada de carbono de {numero_coletor:.2f} coletores menstruais distribuídos é de {pegada_carbono_coletor:.2f}kg,")],
    [sg.Text(f"o que é equivalente a {porcentagem_comp:.2f}% dos absorventes descartáveis.")],
    [sg.Text(f"Convertendo a pegada de carbono dos absorventes descartáveis em créditos de carbono, \nisso seria: US${creditos_absorvente_desc:.2f}, ou seja R${(creditos_absorvente_desc * 5):.2f}")],
    [sg.Checkbox("Deseja testar o cálculo com o seu consumo individual?", default=False, key='-CALCULADORA-', text_color='#52B2B2')],
    [sg.Button('OK'), sg.Button('Sair')],
]

window = sg.Window('Simulador de Pegada de Carbono').Layout(layout)

while True:
    event, values = window.Read()
    if event in (None, 'Sair'):
        break
    elif event == 'OK':
        if values["-CALCULADORA-"] == True:
            absorventes = int(
                sg.popup_get_text("Digite a quantidade média de absorventes que você utiliza em um dia: "))
            dias = int(sg.popup_get_text("Digite a quantidade média de dias do seu período menstrual: "))
            ciclo_anual = dias * 12
            pegada_carbono = ((
                                          ciclo_anual * absorventes) * carbono_ciclo_anual_absorvente_desc) / ciclo_anual_absorvente_desc
            pegada_carbono_coletor_anual = (1 * carbono_ciclo_anual_coletor) / ciclo_anual_coletor
            sg.popup(
                f"Sua pegada de carbono anual é de: {pegada_carbono:.2f}kg \nE caso substituísse por coletores menstruais, sua pegada de carbono anual seria de: {pegada_carbono_coletor_anual}kg")
        else:
            sg.popup("Obrigado por usar o Simulador de Pegada de Carbono")

window.Close()
