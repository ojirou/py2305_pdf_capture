import pyautogui as pgui
import time
import os
def main():
    print('Input PDF file name')
    PdfName = input('>> ')
    PdfPath='D:\\'+PdfName
    os.mkdir(PdfPath)
    print('マウスをフレームの左上に置いてクリック')
    dummy = input('>> ')
    PosUpperLeft=pgui.position()
    print('マウスをフレームの右下に置いてクリック')
    dummy = input('>> ')
    PosLowerRight=pgui.position()
    print('マウスをページ送りボタンに置いてクリック')
    dummy = input('>> ')
    PosButton=pgui.position()
    x1=PosUpperLeft[0]
    y1=PosUpperLeft[1]
    dx=PosLowerRight[0]-PosUpperLeft[0]
    dy=PosLowerRight[1]-PosUpperLeft[1]
    print(x1, y1, dx, dy)
    # type(x1)
    for num in range(1, 2000):
        num=int(num)
        s=f'{num:03}'
        filename=PdfPath+'\\'+\
        PdfName+'_'+str(s)+'.png' 
        pgui.screenshot(filename, region=(x1, y1, dx, dy))
        pgui.click(PosButton, duration=0.4)
        time.sleep(1)
if __name__ == "__main__":
    main()
