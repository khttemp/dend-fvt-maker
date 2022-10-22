# -*- coding: utf-8 -*-

import traceback

from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox as mb

from importPy.tkinterScrollbarFrameClass import *
from importPy.tkinterWidgetClass import *
from importPy.fvtConvert import *

content = -1
fvtConvertFile = None

LS = 0
BS = 1
CS = 2
RS = 3

def openFile():
    global fvtConvertFile
    global content

    if content == -1:
        mb.showerror(title="エラー", message="ゲームを選択してください")
        return

    file_path = fd.askopenfilename(filetypes=[("CSVファイル", "*.CSV")])

    if file_path:
        del fvtConvertFile
        fvtConvertFile = FvtConvert(file_path, content)
        if not fvtConvertFile.open():
            mb.showerror(title="エラー", message=fvtConvertFile.error)
            return

        warnMsg = "変換準備ができました。\n既存のファイルは上書きされます。\nそれでもよろしいですか？"
        result = mb.askokcancel(title="警告", message=warnMsg, icon="warning", parent=root)
        if result:
            try:
                fvtConvertFile.write()
                mb.showinfo(title="成功", message="全てのリストを書込みしました")
            except Exception as e:
                f = open("error_log.txt", "w")
                f.write(traceback.format_exc())
                f.close()
                mb.showerror(title="保存エラー", message="予想外のエラーです。変換失敗しました")

def selectGame():
    global csvLf
    global descLf
    global content
    deleteWidget()

    content = v_radio.get()
    frame = ScrollbarFrame(csvLf)
    CsvWidget(frame.frame, content)
    frame2 = ScrollbarFrame(descLf)
    DescWidget(frame2.frame, content)

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
root.title("電車でD FVT作成 1.0.1")
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
