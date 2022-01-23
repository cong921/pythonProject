# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import easyocr
import random
from cnocr import CnOcr


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
def shotScr():
    os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb shell screencap -p /sdcard/01.png')
    os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb pull /sdcard/01.png /Users/liningbo/Desktop')

def weakUp():
    os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb shell input keyevent 224')
    os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb shell input swipe 300 1000 300 500')
    os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb shell input text 5355')
    os.system('sleep 3')
def sleep(s):
    os.system('sleep '+str(s))
def click(L):
    print('/Users/liningbo/.android-sdk-macosx/platform-tools//adb shell input tap '+str(L[0])+' '+str(L[1]))
    os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb shell input tap '+str(L[0])+' '+str(L[1]))
def jingdong():
    os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb shell am start -n com.jingdong.app.mall/.main.MainActivity')
    os.system('sleep 5 ')
    # my
    os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb shell input tap 1272 3116')
    os.system('sleep 3')
    # bean
    # os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb shell input tap 473 1654')
    # os.system('sleep 3')
    # os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb shell input tap 1295 1633')
# Press the green button in the gutter to run the script.
def getPosition(charStr):
    sleep(3)
    shotScr()
    # 创建reader对象
    reader = easyocr.Reader(['ch_sim'], gpu=False)
    # 读取图像
    result = reader.readtext('/Users/liningbo/Desktop/01.png')
    print(type(result))
    L=[]
    if(isinstance(result,list)):
        for i in range(len(result)):
            if result[i][1].find(charStr)>=0:
                m=result[i][0]
                d=m
                print(m)
                x=(d[1][0]-d[0][0])*random.uniform(0.3,0.7)+m[0][0]
                y=(m[2][1]-m[0][1])*(random.uniform(0.3,0.7))+m[0][1]
                L.append(int(x))
                L.append(int(y))
                print(L)
                return L
    print("Predicted Chars:", type)
def back():
    os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb shell input keyevent 4')
if __name__ == '__main__':
    weakUp()
    jingdong()
    click(getPosition('签到领'))
    L=getPosition("升级赚")
    click(L)
    while(isinstance(L,list)):

        L=getPosition('去')
        click(L)
        sleep(8)
        back()
    # click(L)
    # L=click(getPosition('更多任务'))
    # click(L)
    # click(getPosition('去逛逛'))
    # sleep(9)
    # back()
    # click(getPosition('去逛逛'))
    # sleep(9)
    # back()
    # click(getPosition('去逛逛'))
    # sleep(9)
    # back()
    # click(getPosition('去逛逛'))
    # sleep(9)
    # back()

    # weakUp()
    # os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb connect') # 连接/Users/liningbo/.android-sdk-macosx/platform-tools//adb
    # weakUp()
    # jingdong()
    # os.system('/Users/liningbo/.android-sdk-macosx/platform-tools//adb disconnect') # 连接/Users/liningbo/.android-sdk-macosx/platform-tools//adb
    # print_hi('PyCharm')






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
