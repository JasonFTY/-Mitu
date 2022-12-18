from PIL import Image
from time import time
from numpy import load,save
from random import randint as r
from tkinter import filedialog as fd
import os
from sys import exit as e
def deldirf(dir_path):
    for root, dirs, files in os.walk(dir_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
def RGBcalc(src,ary):
    sa = []
    def add255(sn,an):
        s = sn + an
        if s > 255:
            s = s - 256
        if s < 0:
            s = 256 + s
        return s
    #print(src)
    for i in range(len(src)):
        sa.append(add255(src[i],ary[i]))
    return sa
def lock(src,psd,userpsd,dit):
    img = Image.open(src)
    psd = list(load(psd,allow_pickle=True))
    loarray = psd[0]
    if userpsd == psd[1]:
        st = time()
        arn = 0
        print(f'开始加密 {src}')
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                srccolor = list(img.getpixel((x,y)))
                if len(srccolor) == 4:
                    del srccolor[3]
                    src = tuple(srccolor)
                if arn == 4999:
                    arn = 0
                    loarray = psd[0]
                    #print(loarray[arn])
                edcolor = tuple(RGBcalc(list(srccolor),loarray[arn]))
                arn += 1
                img.putpixel((x,y),edcolor)
        arn = 0
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                srccolor = list(img.getpixel((x,y)))
                if len(srccolor) == 4:
                    del srccolor[3]
                    src = tuple(srccolor)
                if arn == 4999:
                    arn = 0
                    loarray = psd[0]
                    #print(loarray[arn])
                edcolor = tuple(RGBcalc(list(srccolor),loarray[arn]))
                arn += 1
                img.putpixel((x,y),edcolor)
        img.convert('RGB')
        ft = time()
        print(dit)
        img.save(dit)
        print(f'操作完成，耗时{int(ft-st)}秒')
    else:
        print('密码错误')
def unlock(src,psd,userpsd,dit):
    img = Image.open(src)
    psd = list(load(psd,allow_pickle=True))
    loarray = psd[0]
    if userpsd == psd[1]:
        st = time()
        arn = 0
        print(f'开始解密 {src}')
        #print(psd)
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                srccolor = list(img.getpixel((x,y)))
                if len(srccolor) == 4:
                    del srccolor[3]
                    src = tuple(srccolor)
                if len(srccolor) == 4:
                    del srccolor[3]
                if arn == 4999:
                    arn = 0
                    loarray = psd[0]
                    #print(loarray)
                tc = [loarray[arn][0]*-1,loarray[arn][1]*-1,loarray[arn][2]*-1]
                edcolor = tuple(RGBcalc(list(srccolor),tc))
                arn += 1
                img.putpixel((x,y),edcolor)
        arn = 0
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                srccolor = list(img.getpixel((x,y)))
                if len(srccolor) == 4:
                    del srccolor[3]
                    src = tuple(srccolor)
                if arn == 4999:
                    arn = 0
                    loarray = psd[0]
                    #print(loarray)
                tc = [loarray[arn][0]*-1,loarray[arn][1]*-1,loarray[arn][2]*-1]
                edcolor = tuple(RGBcalc(list(srccolor),tc))
                arn += 1
                img.putpixel((x,y),edcolor)
        img.convert('RGB')
        ft = time()
        img.save(dit)
        print(f'操作完成，耗时{int(ft-st)}秒')
    else:
        print('密码错误')
def gencreatepsd(upassword):
    psdarray = []
    for i in range(5000):
        na = [r(-120,120),r(-120,120),r(-120,120)]
        psdarray.append(na)
    info = [psdarray,upassword]
    pth = fd.asksaveasfilename(filetypes=[('NPY数组文件','.npy')])
    save(f'{pth}.npy',info)


def main():
    print('密图 v1.0\n作者：FTY')
    print('='*20)
    while True:
        print('主菜单\n\n1 加密图片\n2 解密图片\n3 生成密码簿\nexit 退出密图\n--------------------')
        cm = input('输入指令 ')
        print('-'*20)
        if cm == '1':
            while True:
                print(f'\n加密图片\n{"="*20}\n注意：请妥善保存密码簿，密码簿是加密/解密图片的关键部分\n\n1 加密图片\nback 返回主菜单\n{"-"*20}')
                cm1 = input('输入指令 ')
                print('-'*20)
                if cm1 != 'back':
                    psdp = fd.askopenfilename(filetypes=[('NPY密码簿','.npy')],title='选择密码簿')
                    up = input('输入密码簿的密码 ')
                    pict = fd.askopenfilenames(filetypes=[('PNG图像','.png')],title='选择图片')
                    for i in pict:
                        lock(i,psdp,up,i)
                else:
                    break
        if cm == '2':
            while True:
                print(f'\n解密图片\n{"="*20}\n注意：请妥善保存密码簿，密码簿是加密/解密图片的关键部分\n\n1 解密图片\nback 返回主菜单\n{"-"*20}')
                cm1 = input('输入指令 ')
                print('-'*20)
                if cm1 != 'back':
                    psdp = fd.askopenfilename(filetypes=[('NPY密码簿','.npy')],title='选择密码簿')
                    up = input('输入密码簿的密码 ')
                    pict = fd.askopenfilenames(filetypes=[('PNG图像','.png')],title='选择图片')
                    md = input('您希望解密后的文件覆盖原文件吗(是/否) ')
                    if md == '是':
                        for i in pict:
                            unlock(i,psdp,up,i)
                    else:
                        nd = fd.askdirectory(title='选择保存目录')
                        for i in pict:
                            unlock(i,psdp,up,f'{nd}/{time()}.png')
                        os.startfile(nd)
                else:
                    break
        if cm == '3':
            print(f'\n创建密码簿\n{"="*20}')
            upsd = input('请设置密码簿的密码 ')
            gencreatepsd(upsd)
            print('-'*20)
        if cm == 'exit':
            e()
main()