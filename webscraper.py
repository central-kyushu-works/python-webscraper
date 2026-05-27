#https://viewer.impress.co.jp/viewer.html?group_name=a4cba557_6a0bcfcd3e1dc&pdf=p502258all&page=1
# Central Kyushu Works 2026.5.26

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

# オプションのインスタンスをアプリケーションモードとして作成
options = Options()
options.add_argument("--app=local")


# ブラウザ(Chrome)をURL無しで起動し、最大化、F11キーしておく
driver = webdriver.Chrome(options=options)
time.sleep(0.5)
driver.maximize_window()
time.sleep(0.5)
pyautogui.press('f11')

#次の10秒間スリープしている間にブラウザに現れる「Chromeは自動テストソフトウェアによって制御されています」バーを×で閉じて表示領域を広くしておく
time.sleep(10)


# スクリーンショットを撮影して保存するサブ
def getimage(p):
    #引数のpはページ番号でなく、出力画像ファイルの追番用かつエミュレートで→キーを押す(ページ送り)の回数
    print("N="+str(p))
    #カーソルキーの→をエミュレートしてWebのページ送り
    pyautogui.press('right')
    time.sleep(2)

    #スクリーンショット取得と画像ファイル出力
    fpng="C:\\Users\\user2\\Pictures\\page"+str(p).zfill(3)+".png"
    pyautogui.screenshot(fpng)
    time.sleep(1)


#最初のページはサブ呼び出しせずに取得
page=1
url="https://viewer.impress.co.jp/viewer.html?group_name=a4cba557_6a0bcfcd3e1dc&pdf=p502258all&page="+str(page)
driver.get(url)
time.sleep(1.5)

#スクリーンショット取得と画像ファイル出力
fpng="C:\\Users\\user2\\Pictures\\page001.png"
pyautogui.screenshot(fpng)
time.sleep(1)

#2ページ目以降はサブ呼び出しし、カーソルキーエミュレートでページ送りして表示
for i in range(2,6):
  getimage(i)

print("done!")

#詳しい人は終了処理を追加して
