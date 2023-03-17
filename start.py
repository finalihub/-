# 导入需要用到的库
import tkinter
from tkinter import *
from tkinter.filedialog import *
from PIL import Image,ImageTk
import qrcode
import json
import requests
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

with open('l.txt', encoding='utf-8') as file_obj:
    contents = file_obj.read()
    a = contents.rstrip()

with open('bg_color.txt', encoding='utf-8') as file_obj:
    contents = file_obj.read()
    j = contents.rstrip()



la = ["QR code generater","Enter the link","BIB","Select the icon","Save the QB code"]
lan = []
if a == "en":
    lan.append("QR code generater")#0
    lan.append("Enter the link")#1
    lan.append("BIB")#2
    lan.append("Select the icon")#3
    lan.append("Save the QB code")#4
    lan.append("Set up")#5
    lan.append("language")#6
    lan.append("UI style")#7
    lan.append("white")#8
    lan.append("palegreen")#9
    lan.append("orange")#10
    lan.append("light blue")#11
    lan.append("Save")#12
else:
    if a == "ch":
        lan.append("二维码生成器")#0
        lan.append("输入链接")#1
        lan.append("生成")#2
        lan.append("选择图标")#3
        lan.append("保存二维码")#4
        lan.append("设置")#5
        lan.append("语言")#6
        lan.append("UI风格")#7
        lan.append("白色")#8
        lan.append("浅绿")#9
        lan.append("橙色")#10
        lan.append("浅蓝")#11
        lan.append("保存")#12

# 设置界面函数
def set_ui_white():
    with open("bg_color.txt","w",encoding="utf-8") as s:
        s.write("white")
def set_ui_palegreen():
    with open("bg_color.txt","w",encoding="utf-8") as s:
        s.write("palegreen")
def set_ui_orange():
    with open("bg_color.txt","w",encoding="utf-8") as s:
        s.write("orange")
def set_ui_light_blue():
    with open("bg_color.txt","w",encoding="utf-8") as s:
        s.write("light blue")

def save_1():
    sys.exit()

def set_l_ch():
    with open("l.txt","w",encoding="utf-8") as f:
        f.write("ch")
def set_l_en():
    with open("l.txt","w",encoding="utf-8") as f:
        f.write("en")
def set_up():
    global j
    top = tkinter.Tk()
    top.config(background = j)
    top.title(lan[5])
    top.geometry('600x400+400+100')
    top.resizable(0, 0)
    top.iconbitmap("bg2.ico")
    label1 = Label(top,text = lan[5],fg = "black",font = ("微软雅黑",20),bg=j)
    label2 = Label(top,text = lan[6],fg = "black",font = ("微软雅黑",10),bg=j)
    label1.place(x = 225,y = 10,width = 150,height = 30)
    label2.place(x = 10,y = 50,width = 150,height = 30)
    button1 = Button(top,text = "English",fg = "black",bg = j,command = set_l_en)
    button2 = Button(top,text = "中文",fg = "black",bg = j,command = set_l_ch)
    button1.place(x = 100,y = 80,width = 100,height = 20)
    button2.place(x = 400,y = 80,width = 100,height = 20)
    # 设置界面风格
    label4 = Label(top,text = lan[7],fg = "black",font = ("微软雅黑",10),bg=j)
    label4.place(x = 10,y = 110,width = 150,height = 30)
    button3 = Button(top,text = lan[8],fg = "black",bg = j,command = set_ui_white)#bai
    button4 = Button(top,text = lan[9],fg = "black",bg = j,command = set_ui_palegreen)#lv
    button5 = Button(top,text = lan[10],fg = "black",bg = j,command = set_ui_orange)#cheng
    button6 = Button(top,text = lan[11],fg = "black",bg = j,command = set_ui_light_blue)#lan
    button3.place(x = 100,y = 140,width = 80,height = 20)
    button4.place(x = 400,y = 140,width = 80,height = 20)
    button5.place(x = 200,y = 140,width = 80,height = 20)
    button6.place(x = 300,y = 140,width = 80,height = 20)
    # 保存
    button7 = Button(top, text=lan[12], fg="black",
                     bg=j, command=save_1)
    button7.place(x = 250,y = 300,width = 80,height = 30)











def openfile():
    global filename,image_name
    filename = askopenfilename()
    image_name = Image.open(filename)
    image_name = image_name.resize((200, 200), Image.ANTIALIAS)#缩放图片
    im_root = ImageTk.PhotoImage(image_name)  # 预设打开的图片
    canvas1.create_image(100,100,image=im_root,bg = j)  # 嵌入预设的图片
    canvas1.place(x = 50,y = 100,width = 200,height = 200)
    root.mainloop()
def creat():
    global img,filename,image_name
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=1)
    url = entry1.get()
    qr.add_data(url)
    qr.make(fit=True)
    try:
        image_name
    except NameError:
        a = 0
    else:
        a = 1
    if a == 1:
        img = qr.make_image()
        img = img.convert("RGBA")
        icon = image_name
        icon = icon.convert("RGBA")
        imgWight, imgHeight = img.size
        iconWight = int(imgWight / 3)
        iconHeight = int(imgHeight / 3)
        icon = icon.resize((iconWight, iconHeight), Image.ANTIALIAS)
        posW = int((imgWight - iconWight) / 2)
        posH = int((imgHeight - iconHeight) / 2)
        img.paste(icon, (posW, posH), icon)
        img1 = img.resize((200, 200), Image.ANTIALIAS)
        im_root = ImageTk.PhotoImage(img1)  # 预设打开的图片
        canvas2.create_image(100,100,image=im_root)  # 嵌入预设的图片
        canvas2.place(x = 360,y = 100,width = 200,height = 200)
    else:
        filename = "bg.jpg"
        image_name = Image.open(filename)
        image_name = image_name.resize((200, 200), Image.ANTIALIAS)#缩放图片
        im_root = ImageTk.PhotoImage(image_name)  # 预设打开的图片
        canvas1.create_image(100,100,image=im_root)  # 嵌入预设的图片
        canvas1.place(x = 50,y = 100,width = 200,height = 200)
        img = qr.make_image()
        img = img.convert("RGBA")
        icon = image_name
        icon = icon.convert("RGBA")
        imgWight, imgHeight = img.size
        iconWight = int(imgWight / 3)
        iconHeight = int(imgHeight / 3)
        icon = icon.resize((iconWight, iconHeight), Image.ANTIALIAS)
        posW = int((imgWight - iconWight) / 2)
        posH = int((imgHeight - iconHeight) / 2)
        img.paste(icon, (posW, posH), icon)
        img1 = img.resize((200, 200), Image.ANTIALIAS)
        im_root = ImageTk.PhotoImage(img1)  # 预设打开的图片
        canvas2.create_image(100,100,image=im_root)  # 嵌入预设的图片
        canvas2.place(x = 360,y = 100,width = 200,height = 200)
    root.mainloop()
def savefile():
    pathname = asksaveasfilename(defaultextension = '.png',initialfile = '新的二维码.png')
    img.save(pathname)


root = tkinter.Tk()
root.config(background = j)
root.title("二维码生成器")
root.geometry('600x400+400+100')
root.resizable(0, 0)
root.iconbitmap("bg2.ico")
# title = ttk.Label(root, text="Image converter", font=(
#     'Georgia', 28)).grid(row=0, columnspan=8)
# choice = tkinter.StringVar()
button1 = Button(root, text=lan[3], font='微软雅黑',
                    fg='black', bg=j, command=openfile)  # 设置按钮
button2 = Button(root, text=lan[4], font=('微软雅黑'),
                     fg='black', bg=j, command=savefile)  # 设置按钮
button1.place(x=90, y=330, width=200, height=50)  # 显示按钮
button2.place(x = 320,y = 330,width = 200,height = 50)#显示按钮
label1 = Label(root, text=lan[0], font=('微软雅黑', 20),
                   fg='black',bg=j)  # 设置组件
label2 = Label(root, text=lan[1], font=('微软雅黑', 10),
                   fg='black',bg=j)  # 设置组件

button3 = Button(root, text=lan[5], font=('微软雅黑'),
                     fg='black', bg=j, command=set_up)  # 设置按钮
button3.place(x = 500,y = 10,width = 70,height = 30)#显示按钮
if a == "ch":
    label1.place(x=150, y=5, width=300, height=50)
    label2.place(x=25, y=20, width=130, height=50)
else:
    if a== "en":
        label1.place(x=135, y=5, width=340, height=50)
        label2.place(x=25, y=20, width=130, height=50)
entry1 = ttk.Entry(root, font=('微软雅黑', 20))  # 设置输入框
entry1.place(x=50, y=60, width=510, height=30)  # 显示组件
canvas1 = Canvas(root,width = 300,height = 300,bg = j)#创建画布
canvas2 = Canvas(root,width = 300,height = 300,bg = j)#创建画布
canvas1.place(x = 50,y = 100,width = 200,height = 200)
canvas2.place(x = 360,y = 100,width = 200,height = 200)
button = Button(root, text=lan[2], font=('微软雅黑', 15),
                    fg='black', bg=j, command=creat)  # 设置按钮
button.place(x=280, y=200, width=50, height=40)  # 显示按钮

root.mainloop()