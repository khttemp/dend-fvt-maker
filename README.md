# dend-fvt-maker

## 概要

dend-fvt-maker は、電車でD LightningStage、BurningStage、ClimaxStage、RisingStage のセリフを、CSVで読み込んで一気にFVTファイルを作成するソフトウェアである。

## 動作環境

* 電車でDが動くコンピュータであること
* OS: Windows 10 64bit の最新のアップデートであること
* OSの端末が日本語に対応していること

※ MacOS 、 Linux などの Unix 系 OS での動作は保証できない。


## 免責事項

このプログラムを使用して発生したいかなる損害も製作者は責任を負わない。

このプログラムを実行する前に、自身のコンピュータのフルバックアップを取得して、
安全を担保したうえで実行すること。
このプログラムについて、電車でD 作者である、地主一派へ問い合わせてはいけない。

このソフトウェアの更新やバグ取りは、作者の義務ではなく解消努力目標とする。
Issue に上げられたバグ情報が必ず修正されるものではない。

* ライセンス：MIT

電車でD の正式なライセンスを持っていること。

本プログラムに関連して訴訟の必要が生じた場合、東京地方裁判所を第一審の専属的合意管轄裁判所とする。

このプログラムのバイナリを実行した時点で、この規約に同意したものと見なす。

## 実行方法

![title](https://github.com/khttemp/dend-fvt-maker/blob/master/image/title.png)

1. ラジオボタンで、ゲームを選ぶ。

    そうするとCSVの様式の例を見れる。

2. メニュの「ファイルの開く」でCSVファイルを開く。

3. OKボタンをクリックすると、読み込んだCSVを元にFVTファイルを作成する。

### 依存ライブラリ

* Tkinter

  Windows 版 Python3 系であれば、インストール時のオプション画面で tcl/tk and IDLE のチェックがあったと思う。
  tcl/tk and IDLE にチェックが入っていればインストールされる。
  
  Linux 系 OS では、 パッケージ管理システムを使用してインストールする。

### 動作環境

以下の環境で、ソースコード版の動作確認を行った

* OS: Windows 10 64bit
* Python 3.7.9 64bit
* pip 21.2.4 64bit
* PyInstaller 3.4 64bit
* 横1024×縦768ピクセル以上の画面解像度があるコンピュータ

### ソースコードの直接実行

Windows であれば以下のコマンドを入力する。


````
> python maker.py
````

これで、実行方法に記載した画面が現れれば動作している。


### FAQ

* Q. ImportError: No module named tkinter と言われて起動しない

  * A. 下のようなメッセージだろうか？ それであれば、 tkinter がインストールされていないので、インストールすること。
  
  ````
  > python editor.py
  Traceback (most recent call last):
    File "maker.py", line 6, in <module>
      from tkinter import *
  ImportError: No module named tkinter
  ````

* Q. ダウンロードがブロックされる、実行がブロックされる、セキュリティソフトに削除される

  * A. ソフトウェア署名などを行っていないので、ブラウザによってはダウンロードがブロックされる
  * A. 同様の理由でセキュリティソフトが実行を拒否することもある。

### Windows 版実行バイナリ（ .exeファイル ）の作成方法

pyinstaller か py2exe ライブラリをインストールする。 pip でも  easy_install  でも構わない。

下は、 pyinstaller を使用して、Windows 版実行バイナリ（ .exeファイル ）を作る例である。

````
> pyinstaller maker.py --onefile --add-data "./resource/*;./"
（ コンソール出力は省略 ）
````

dist フォルダーが作られて、 editor.exe が出力される。

### Virustotal

![virustotal](https://github.com/khttemp/dend-fvt-maker/blob/master/image/virustotal.png)

以上。