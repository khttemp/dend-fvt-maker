import random
import os

from tkinter import *

LS = 0
BS = 1
CS = 2
RS = 3

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("resource"), relative_path)

class CsvWidget():
    def __init__(self, frame, content):
        self.csvNumLb = Label(frame, text="FVT\n番号", font=("", 20), width=5, borderwidth=1, relief="solid")
        self.csvNumLb.grid(row=0, column=0, sticky=W+E)

        self.faceNumLb = Label(frame, text="FACE\n番号", font=("", 20), width=5, borderwidth=1, relief="solid")
        self.faceNumLb.grid(row=0, column=1, sticky=W+E)
        
        if content > LS:
            self.faceImgXposLb = Label(frame, text="FACE\n横長さ", font=("", 20), width=6, borderwidth=1, relief="solid")
            self.faceImgXposLb.grid(row=0, column=2, sticky=W+E)

            self.faceImgYposLb = Label(frame, text="FACE\n縦長さ", font=("", 20), width=6, borderwidth=1, relief="solid")
            self.faceImgYposLb.grid(row=0, column=3, sticky=W+E)

            self.faceImgWidthLb = Label(frame, text="FACE\nX座標", font=("", 20), width=6, borderwidth=1, relief="solid")
            self.faceImgWidthLb.grid(row=0, column=4, sticky=W+E)

            self.faceImgHeightLb = Label(frame, text="FACE\nY座標", font=("", 20), width=6, borderwidth=1, relief="solid")
            self.faceImgHeightLb.grid(row=0, column=5, sticky=W+E)

        columnCnt = 0
        if content > LS:
            columnCnt = 4

        self.effectLb = Label(frame, text="効果", font=("", 20), width=5, borderwidth=1, relief="solid")
        self.effectLb.grid(row=0, column=columnCnt + 2, sticky=N+S+W+E)

        self.voiceNumLb = Label(frame, text="VO\n番号", font=("", 20), width=5, borderwidth=1, relief="solid")
        self.voiceNumLb.grid(row=0, column=columnCnt + 3, sticky=W+E)

        self.txtLb = Label(frame, text="テキスト", font=("", 20), width=10, borderwidth=1, relief="solid")
        self.txtLb.grid(row=0, column=columnCnt + 4, sticky=N+S+W+E)

        path = ""
        randList = []
        if content == LS:
            path = resource_path("LS.csv")
        elif content == BS:
            path = resource_path("BS.csv")
        elif content == CS:
            randList = [31]
            path = resource_path("CS.csv")
        elif content == RS:
            path = resource_path("RS.csv")
            
        f = open(path)
        lines = f.readlines()
        f.close()
        lines.pop(0)

        l = list(range(0, len(lines)))
        if content == BS:
            randList = [0]
            l.pop(0)
        elif content == CS:
            randList = [31]
            l.pop(31)
        elif content == RS:
            randList = [574]
            l.pop(574)
        randList.extend(random.sample(l, 3))
        randList.sort()

        row = 0
        maxNum = -1
        for rand in randList:
            row += 1
            line = lines[rand].strip()
            arr = line.split(",")
            fvtNum = int(arr[0])
            faceNum = int(arr[1])

            contentCnt = 0
            if content > LS:
                contentCnt = 4
                faceX = int(arr[2])
                faceY = int(arr[3])
                faceW = int(arr[4])
                faceH = int(arr[5])

            effect = int(arr[contentCnt + 2])
            voNum = int(arr[contentCnt + 3])

            text = arr[contentCnt + 4]
            if maxNum < len(text.encode("shift-jis")):
                maxNum = len(text.encode("shift-jis"))

            self.csvNumLb = Label(frame, text=fvtNum, font=("", 20), width=5, borderwidth=1, relief="solid")
            self.csvNumLb.grid(row=row, column=0, sticky=W+E)

            self.faceNumLb = Label(frame, text=faceNum, font=("", 20), width=5, borderwidth=1, relief="solid")
            self.faceNumLb.grid(row=row, column=1, sticky=W+E)
            
            if content > LS:
                self.faceImgXposLb = Label(frame, text=faceX, font=("", 20), width=6, borderwidth=1, relief="solid")
                self.faceImgXposLb.grid(row=row, column=2, sticky=W+E)

                self.faceImgYposLb = Label(frame, text=faceY, font=("", 20), width=6, borderwidth=1, relief="solid")
                self.faceImgYposLb.grid(row=row, column=3, sticky=W+E)

                self.faceImgWidthLb = Label(frame, text=faceW, font=("", 20), width=6, borderwidth=1, relief="solid")
                self.faceImgWidthLb.grid(row=row, column=4, sticky=W+E)

                self.faceImgHeightLb = Label(frame, text=faceH, font=("", 20), width=6, borderwidth=1, relief="solid")
                self.faceImgHeightLb.grid(row=row, column=5, sticky=W+E)
                

            self.effectLb = Label(frame, text=effect, font=("", 20), width=5, borderwidth=1, relief="solid")
            self.effectLb.grid(row=row, column=columnCnt + 2, sticky=N+S+W+E)

            self.voiceNumLb = Label(frame, text=voNum, font=("", 20), width=5, borderwidth=1, relief="solid")
            self.voiceNumLb.grid(row=row, column=columnCnt + 3, sticky=W+E)

            self.txtLb = Label(frame, text=text, font=("", 20), width=maxNum, borderwidth=1, relief="solid", anchor="w")
            self.txtLb.grid(row=row, column=columnCnt + 4, sticky=N+S+W+E)

class DescWidget():
    def __init__(self, frame, content):
        fontSize = 14
        self.faceNumLb = Label(frame, text="FACE番号", font=("", fontSize), anchor="w", borderwidth=1, relief="solid")
        self.faceNumLb.grid(row=0, column=0, sticky=N+S+W+E)
        self.faceNumDescLb = Label(frame, text="FACEのイメージファイルの番号を指定する。\n0を指定すれば画像なし", font=("", fontSize), width=44, borderwidth=1, relief="solid", anchor="w", justify="left")
        self.faceNumDescLb.grid(row=0, column=1, sticky=W+E)

        self.faceSizeLb = Label(frame, text="FACEサイズ", font=("", fontSize), anchor="w", borderwidth=1, relief="solid")
        self.faceSizeLb.grid(row=1, column=0, sticky=N+S+W+E)
        self.faceSizeDescLb = Label(frame, text="切り取り方法は右の図を参照。\nデフォは[-1,-1,-1,-1]", font=("", 16), borderwidth=1, relief="solid", anchor="w", justify="left")
        self.faceSizeDescLb.grid(row=1, column=1, sticky=W+E)

        self.effectLb = Label(frame, text="効果", font=("", fontSize), anchor="w", borderwidth=1, relief="solid")
        self.effectLb.grid(row=2, column=0, sticky=N+S+W+E)
        effectText = ""
        effectText += "0（普通【ゲームの速度に合わせて】）\n"
        effectText += "1（揺らす【ゲームの速度に合わせて】）\n"
        effectText += "2（下から出る【LSのみ使われた】）\n"
        effectText += "3（画像がもっと下の位置【ゲームの速度に合わせて】）\n"
        effectText += "4（揺らす）\n"
        effectText += "5（画像がもっと下の位置）\n"
        effectText += "6（画面の中央から現れる【LSのみ使われた】）\n"
        effectText += "7（普通）"
        self.effectDescLb = Label(frame, text=effectText, font=("", fontSize), anchor="w", borderwidth=1, relief="solid", justify="left")
        self.effectDescLb.grid(row=2, column=1, sticky=W+E)

        self.voiceLb = Label(frame, text="VO番号", font=("", fontSize), anchor="w", borderwidth=1, relief="solid")
        self.voiceLb.grid(row=3, column=0, sticky=N+S+W+E)
        self.voiceDescLb = Label(frame, text="VOの音声ファイルの番号を指定する。\n0を指定すれば音声なし", font=("", fontSize), anchor="w", borderwidth=1, relief="solid", justify="left")
        self.voiceDescLb.grid(row=3, column=1, sticky=W+E)

        self.txtLb = Label(frame, text="テキストの\nタグ", font=("", fontSize), anchor="w", borderwidth=1, relief="solid")
        self.txtLb.grid(row=4, column=0, sticky=W+E)
        self.txtDescLb = Label(frame, text="<BR>、<PAGE>、<WAIT120>\n<FC#255016000></FC>などなど・・・", font=("", fontSize), anchor="w", borderwidth=1, relief="solid", justify="left")
        self.txtDescLb.grid(row=4, column=1, sticky=W+E)

        self.padding = Label(frame, width=33, font=("", fontSize), anchor="w", borderwidth=1)
        self.padding.grid(row=0, column=2, sticky=N+W+E)

        if content > LS:
            self.canvas = Canvas(frame, bg="white", width=300, height=300)
            self.canvas.place(relx=1.0, rely=0.0, anchor=N+E)
            
            path = ""
            if content == BS:
                path = resource_path("BS.png")
            elif content == CS:
                path = resource_path("CS.png")
            elif content == RS:
                path = resource_path("RS.png")
            image = PhotoImage(file=path)
            self.canvas.photo = image
            self.canvas.create_image(160, 160, image=self.canvas.photo)
