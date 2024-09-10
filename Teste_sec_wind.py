import PySimpleGUI as sg
import sqlite3
import bcrypt



user = []
password = []
def janela_2():
    layout_janela_2 = [
            [sg.Text("Novo usuário"), sg.Input(key='-NEWUSER-')],
            [sg.Text("Nova senha"), sg.Input(key='-NEWPASSWORD-', password_char='*')],
            [sg.Text("Repita a senha"), sg.Input(key='-REPEATPASSWORD-', password_char='*')],
            [sg.Button("Terminar", key='-FINISH-')]
        ]

        # Criação da segunda janela
    second_window = sg.Window("Janela número 2", layout_janela_2)

        # Loop para eventos da segunda janela
    while True:
        second_event, second_values = second_window.read()

        # Fechar a segunda janela
        if second_event == sg.WINDOW_CLOSED or second_event == '-FINISH-':
            second_window.close()
            break



def janela_1():
    layout_janela_1 = [
        [sg.Text('Usuário'), sg.Input(key='-USER-'), sg.Push()],
        [sg.Text('Senha'), sg.Input(key='-PASSWORD-', password_char='*'), sg.Push()],
        [sg.Button("Login", key='-LOGIN-'), sg.Button("Cadastrar", key='-REGISTER-')]
    ]

    # Criação da janela principal
    window = sg.Window("Janela 1", layout_janela_1)

    # Loop principal para eventos
    while True: 
        # Ler eventos e valores da janela principal
        event, values = window.read()

        # Fechar a janela principal se o botão de fechar for pressionado
        if event == sg.WINDOW_CLOSED:
            break

        if event == '-LOGIN-':
            if values['-USER-'] in user and values['-PASSWORD-']  == password[user.index(values['-USER-'])]:
                sg.popup("Login bem sucedido!")
            else: 
                sg.popup("Usuario ou senha incorretos!")
            
            
     # Se o botão "Cadastrar" for pressionado, abre a segunda janela
        if event == '-REGISTER-':
            janela_2()






