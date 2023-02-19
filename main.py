import PySimpleGUI as sg
import qrcode

title = 'QRコードメーカー'


# QRコード生成
def make_qrcode(value):
    img = qrcode.make(value)
    img.save('qrcode.png')


# ホーム画面のレイアウト
def make_window1():
    main_layout = [[sg.Text('QRコード作成', key='text')],
                   [sg.Input(key='input')],
                   [sg.Button('作成')]]
    return sg.Window(title, main_layout)


# QRコード表示のレイアウト
def make_window2(value):
    sub_layout = [[sg.Text(value)],
                  [sg.Image(filename='qrcode.png')],
                  [sg.Button('もう一度')]]
    return sg.Window(title, sub_layout)


# inputに入力がない場合の処理
def failure():
    message = '入力がありません。\n' \
              '入力してください。'
    window['text'].update(message)


window = make_window1()

# アプリ画面の作成
while True:
    event, values = window.read()

    if event == '作成':
        if values['input'] == '':
            failure()
        else:
            make_qrcode(values['input'])
            window.close()
            window = make_window2(values['input'])
    if event == 'もう一度':
        window.close()
        window = make_window1()
    if event is None:
        break

window.close()
