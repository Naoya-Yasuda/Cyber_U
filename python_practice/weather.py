import tkinter as tk
import requests as rq

url = 'https://weather.tsukumijima.net/api/forecast/city/'


def 押された():  # ボタンがクリックされたら実行
    r = rq.get(url + '170010')  # 170010
    天気 = r.json()  # 辞書形式に変換
    ラベル['text'] = 天気['forecasts'][1]['telop']


w = tk.Tk()  # ウィンドウを作成
ボタン = tk.Button(w, text='ボタン', command=押された)  # ボタンを作成
ボタン.place(x=0, y=0)  # ボタンを配置
ラベル = tk.Label(w, text='明日の天気')  # ラベルを作成
ラベル.place(x=0, y=30)  # ラベルを配置

w.mainloop()  # ウィンドウを表示
