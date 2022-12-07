from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('Usuário'), sg.Input(key = 'usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Text('Email'), sg.Input(key='email', size=(20, 1))],
    [sg.Text('Telefone'), sg.Input(key='telefone', size=(20, 1))],
    [sg.Checkbox('Deseja salvar as informações de login?')],
    [sg.Button('Login')] 
]

janela = sg.Window('Cadastro', layout)

while True:
    event, valor = janela.read()
    if event == sg.WINDOW_CLOSED:
        break



