# -*- coding: utf-8 -*-

import struct
import random
import os
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

decryptFile = None
content = -1
errorMsg = ""
fvtList = []

LS = 0
BS = 1
CS = 2
RS = 3

class Scrollbarframe():
    def __init__(self, parent):
        self.canvas = Canvas(parent, width=parent.winfo_width(), height=parent.winfo_height())
        self.frame = Frame(self.canvas)
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.scrollbar = Scrollbar(parent, orient=HORIZONTAL, command=self.canvas.xview)
        self.scrollbar.pack(side=BOTTOM, fill=X)
        
        self.canvas.create_window((0,0), window=self.frame, anchor="nw")
        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        self.canvas.pack()

        self.canvas.bind("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class csvWidget():
    global content
    
    def __init__(self, frame):
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

class descWidget():
    global content
    
    def __init__(self, frame):
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
        effectText += "7（揺らす）"
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
        
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("resource"), relative_path)

def openFile():
    global content
    global errorMsg
    global fvtList

    if content == -1:
        mb.showerror(title="エラー", message="ゲームを選択してください")
        return

    file_path = fd.askopenfilename(filetypes=[("CSVファイル", "*.CSV")])

    if file_path:
        fvtList = []
        if not fvtConvert(file_path):
            mb.showerror(title="エラー", message=errorMsg)
            return

        warnMsg = "変換準備ができました。\n既存のファイルは上書きされます。\nそれでもよろしいですか？"
        result = mb.askokcancel(title="警告", message=warnMsg, icon="warning", parent=root)
        if result:
            try:
                writeFvt(fvtList)
                mb.showinfo(title="成功", message="全てのリストを書込みしました")
            except Exception as e:
                f = open("error_log.txt", "w")
                f.write(e)
                f.close()
                mb.showerror(title="保存エラー", message="予想外のエラーです。変換失敗しました")

def selectGame():
    global csvLf
    global descLf
    global content
    deleteWidget()

    content = v_radio.get()
    frame = Scrollbarframe(csvLf)
    csvWidget(frame.frame)
    frame2 = Scrollbarframe(descLf)
    descWidget(frame2.frame)

def fvtConvert(file_path):
    global content
    global errorMsg
    global fvtList

    f = open(file_path)
    lines = f.readlines()
    f.close()

    lines.pop(0)

    fvtList = []
    cnt = 1
    for line in lines:
        cnt += 1
        line = line.strip()
        arr = line.split(",")

        try:
            fvtNum = int(arr[0])
            fvtNumList = [ d["fvtNum"] for d in fvtList ]
            if fvtNum in fvtNumList:
                errorMsg = "重複してるFVT番号があります[ {0} ]".format(fvtNum)
                return False
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
        except:
            errorMsg = "{0}行に数字で変換できない要素があります".format(cnt)
            return False
        
        try:
            text = arr[contentCnt + 4].encode("shift-jis")
        except:
            errorMsg = "{0}行のテキストをShift-jis変換できません".format(cnt)
            return False

        newLine = bytearray()
        header = ""
        if content == LS:
            header = "DEND_FVT"
        elif content == BS:
            header = "D2_FVT"
        elif content == CS:
            header = "D3_FVT"
        elif content == RS:
            header = "D4_FVT"

        newLine.extend(header.encode("shift-jis"))
        newLine.extend(struct.pack("<h", faceNum))
        if content > LS:
            newLine.extend(struct.pack("<h", faceX))
            newLine.extend(struct.pack("<h", faceY))
            newLine.extend(struct.pack("<h", faceW))
            newLine.extend(struct.pack("<h", faceH))
        newLine.extend(struct.pack("<b", effect))
        newLine.extend(struct.pack("<h", voNum))

        newLine.extend(struct.pack("<h", len(text)))
        newLine.extend(text)

        fvtInfo = {"fvtNum":fvtNum, "info":newLine}
        fvtList.append(fvtInfo)

    return True

def writeFvt(fvtList):
    for fvt in fvtList:
        fvtNum = fvt["fvtNum"]
        f = open("{0:03}.FVT".format(fvtNum), "wb")
        f.write(fvt["info"])
        f.close()

def deleteWidget():
    global csvLf
    global descLf
    children = csvLf.winfo_children()
    for child in children:
        child.destroy()

    children = descLf.winfo_children()
    for child in children:
        child.destroy()
        
root = Tk()
root.title("電車でD FVT作成 1.0.0")
root.geometry("1024x768")

menubar = Menu(root)
menubar.add_cascade(label='ファイルを開く', command= lambda: openFile())
root.config(menu=menubar)

v_radio = IntVar()
v_radio.set(-1)

lsRb = Radiobutton(root, text="Lightning Stage", command = selectGame, variable=v_radio, value=LS)
lsRb.place(relx=0.05, rely=0.03)

bsRb = Radiobutton(root, text="Burning Stage", command = selectGame, variable=v_radio, value=BS)
bsRb.place(relx=0.3, rely=0.03)

csRb = Radiobutton(root, text="Climax Stage", command = selectGame, variable=v_radio, value=CS)
csRb.place(relx=0.55, rely=0.03)

rsRb = Radiobutton(root, text="Rising Stage", command = selectGame, variable=v_radio, value=RS)
rsRb.place(relx=0.8, rely=0.03)

csvLf = ttk.LabelFrame(root, text="CSVの様式（CSVの1行目はヘッダー扱いになり、読み込みを省略する）")
csvLf.place(relx=0.05, rely=0.12, relwidth=0.9, relheight=0.3)

descLf = ttk.LabelFrame(root, text="作成方法")
descLf.place(relx=0.05, rely=0.45, relwidth=0.9, relheight=0.5)

root.mainloop()
