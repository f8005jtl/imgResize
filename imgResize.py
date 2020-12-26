"""
画像を一括リサイズするプログラム SambeMemo
参考:https://note.nkmk.me/python-pillow-image-resize/
使い方：
1. dirディレクトリを作る
2. .jpgの画像ファイルを入れる
3. 本プログラムを実行する
"""
import os # for os.path.splitext()
import glob # for glob.glob()
from PIL import Image # for Image.open(f)

# 出力サイズの設定
imgSizeTuple = (200,200) # 横幅,高さ

files = glob.glob('./dir/*.jpg')# フォルダ内のファイルリストを取得

for fname in files:# ファイル一つずつ読込処理する
    img = Image.open(fname) # ファイルを開く
    img_resize = img.resize((imgSizeTuple[0],imgSizeTuple[1]))# 指定サイズにリサイズ
    ftitle, fext = os.path.splitext(fname)#ファイルの拡張子を取得
    img_resize.save(ftitle + '_cut' + fext)# ファイル名を指定して保存
