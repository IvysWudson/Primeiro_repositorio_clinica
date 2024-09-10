import PySimpleGUI as sg

# Layout da primeira janela
layout1 = [
    [sg.Button("Abrir outra janela", key='-JANELA2-')],
    [sg.Button("Fechar", key='-FECHAR-')]
]

# Criação da primeira janela
main_window = sg.Window("Janela 1", layout1)

# Loop principal da primeira janela
while True:
    event, values = main_window.read()

    if event == sg.WINDOW_CLOSED or event == '-FECHAR-':
        break

    # Abrir segunda janela
    if event == '-JANELA2-':
        layout2 = [
            [sg.Text("Esta é a segunda janela!")],
            [sg.Button("Fechar segunda janela", key='-FECHAR2-')]
        ]

        # Criação da segunda janela
        second_window = sg.Window("Janela 2", layout2)

        # Loop da segunda janela
        while True:
            second_event, second_values = second_window.read()

            if second_event == sg.WINDOW_CLOSED or second_event == '-FECHAR2-':
                second_window.close()
                break

# Fechar a primeira janela quando o loop terminar
main_window.close()