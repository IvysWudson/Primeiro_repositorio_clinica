
from PySimpleGUI import PySimpleGUI as sg
from PySimpleGUI import VSeparator, Column
import sqlite3

def conectar_bd():
    try:
        conn = sqlite3.connect("pacientes.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS pacientes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    data_entrada TEXT,
                    tipo TEXT)""")
        return conn, cur
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None,None

def desconecta_bd(conn):
    if conn:
        try:
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Erro ao desconectar ao banco de dados: {e}")

def salvar_pacientes(nome,idade,data_entrada,tipo, conn, cur):
    try:
        cur.execute('INSERT INTO pacientes(nome,idade,data_entrada,tipo) VALUES(?,?,?,?)',
                       (nome,idade,data_entrada,tipo))
        print("Dados salvos com sucesso!")
        conn.commit()
    except Exception as e:
        print("Erro ao salvas os dados: {e}")



sg.theme('DarkAmber')

up_layout=[
    [sg.Image("file (1).png")]
]

down_layout = [
    [
        sg.Text("Nome"), sg.Input(key='-NOME-'),sg.Text('Idade'), 
        sg.Combo([str(i) for i in range(18, 66)], readonly=True,size=(3,1), key='-IDADE-'),sg.Push()],

    [
        sg.Text("Cidade"),sg.Input(size=(15,1)),sg.Text("UF"),
        sg.Input(size=(2,1)),sg.Push()],

    [
        sg.CalendarButton("Data de nascimento",target='-BIRTH-', format='%d-%m-%y'),
        sg.Input(key='-BIRTH-',size=(10,1), readonly=True),
        sg.CalendarButton("Data de entrada", target="-DATA-", format='%d-%m-%y'),
        sg.Input(key='-DATA-',size=(10,1), readonly=True),sg.Push()],

    [
        sg.Text("Tipo"), 
        sg.Combo(['Involuntaria', 'Voluntaria', 'Compulsoria'], key='-TIPO-', 
              size=(11, 1),readonly=True),sg.Push()],

    [sg.Button("Salvar",key='-SALVAR-')]
]
main_layout=[
    [sg.Column(up_layout),
     VSeparator(),
     sg.Column(down_layout)]

]
conn, cur = conectar_bd()
if conn and cur:
    window= sg.Window("Cadastro de pacientes", main_layout)

    while True:
        event, values, = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == '-SALVAR-':
            nome = values["-NOME-"]
            idade = int(values["-IDADE-"])  # Converter idade para inteiro
            data_entrada = values["-DATA-"]
            tipo = values["-TIPO-"]

            salvar_pacientes(nome, idade, data_entrada, tipo, conn, cur)



    window.close()

    desconecta_bd(conn)

else:
    print("Não foi possivel conectar ao banco de dados!")


    