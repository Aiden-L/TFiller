"""
@author Aiden-L
"""

import time
import base64
import os
from tkinter import Tk, Frame, Label, Entry, Button, IntVar, Listbox, Text, StringVar, PhotoImage
from ctosico import img
from win32api import keybd_event as KE
import pyperclip


class BasicWindow:

    def init(self):
        self.main_window = Tk()
        # self.main_window.iconbitmap("ctos.ico")
        tmp = open("tmp.ico", "wb+")
        tmp.write(base64.b64decode(img))  # 写入到临时文件中
        tmp.close()
        self.main_window.iconbitmap("tmp.ico")  # 设置图标
        os.remove("tmp.ico")
        # 标题
        self.main_window.title("TFiller for your convenience")
        self.main_window.resizable(0, 0)

    def window_resizeable(self):
        self.main_window.resizable(True, True)


class MainWindow(BasicWindow):

    config_path = 'C:\\ProgramData\\TFiller\\config.tfiller'
    data_path = 'C:\\ProgramData\\TFiller\\data\\'
    data_cache = []

    def __init__(self):
        # 验证是否第一次使用
        if not os.path.exists(self.data_path):
            # 第一次使用，写入配置文件
            os.makedirs(self.data_path)
            with open(self.config_path, 'w', encoding='utf-8') as f:
                f.write("Version: 1.0.0")
        self.data_name_list = os.listdir(self.data_path)
        # 布局
        self.init()
        list_frame = Frame(self.main_window)
        self.list_box = Listbox(list_frame, height=31)
        self.list_box.bind('<<ListboxSelect>>', self.choose_item)
        self.list_box.pack()
        self.selected = IntVar()
        self.selected.set(0)

        control_frame = Frame(self.main_window)
        # 输入框
        input_frame = Frame(control_frame, width=40)
        self.text_input = Text(input_frame, width=40, height=30, font=10)
        input_frame2 = Frame(control_frame, width=40)
        input_lab = Label(input_frame2, text="文件名:")

        self.name_text = StringVar()
        name_input = Entry(input_frame2, width=35, textvariable=self.name_text)
        self.text_input.grid()
        input_lab.grid(row=0, column=0)
        name_input.grid(row=0, column=1)
        # 按钮
        but_frame = Frame(control_frame)
        but_change = Button(but_frame, text="保存", width=10, command=self.b_change)
        but_del = Button(but_frame, text="删除", width=10, command=self.b_delete)
        but_execute = Button(but_frame, text="执行", width=10, command=self.b_execute)
        but_change.grid(row=0, column=0, padx=10)
        but_del.grid(row=0, column=1, padx=10)
        but_execute.grid(row=0, column=2, padx=10)

        input_frame.grid(pady=6)
        input_frame2.grid(pady=6)
        but_frame.grid(pady=6)
        list_frame.grid(row=0, column=0, padx=5)
        control_frame.grid(row=0, column=1, padx=5)

        for data_name in os.listdir(self.data_path):
            with open(self.data_path+data_name, 'r', encoding='utf-8') as f:
                data = {
                    'name': data_name.split('.')[1],
                    'url': data_name,
                    'value': f.read()
                }
                self.data_cache.append(data)
        for item in self.data_cache:
            self.list_box.insert('end', item['name'])

        self.main_window.mainloop()

    def choose_item(self, event):
        if len(self.list_box.curselection())>0:
            e = self.list_box.curselection()[0]
            self.text_input.delete(1.0, "end")
            self.text_input.insert('end',self.data_cache[e].get('value'))
            self.name_text.set(self.data_cache[e].get('name'))

    def b_change(self):
        # 获取右两方面信息
        # e = self.list_box.curselection()[0]
        text = self.text_input.get(1.0, 'end')
        name = self.name_text.get()
        # 添加
        with open(self.data_path + str(len(self.data_cache)) + '.' + name, 'w', encoding='utf-8') as f:
            f.write(text)
        data = {
            'name': name,
            'url': str(len(self.data_cache)) + '.' + name,
            'value': text
        }
        self.data_cache.append(data)
        self.list_box.insert('end', name)

    def b_delete(self):
        try:
            e = self.list_box.curselection()[0]
            os.remove(self.data_path + self.data_cache[e].get('url'))
            self.data_cache.pop(e)
            self.list_box.delete(e)
        except Exception as error:
            print(error)

    def b_execute(self):
        text_list = self.text_input.get(1.0, 'end').split('\n')
        while text_list[-1] == '':
            text_list.pop()
        # 等待用户
        time.sleep(3)
        for i in range(0, len(text_list)-1):
            # self.addToClipboard(text)
            pyperclip.copy(text_list[i])
            KE(0x11, 0, 0, 0)
            KE(86, 0, 0, 0)
            KE(86, 0, 2, 0)
            KE(0x11, 0, 2, 0)
            KE(0x9, 0, 0, 0)
            KE(0x9, 0, 2, 0)
            time.sleep(0.3)
        pyperclip.copy(text_list[len(text_list)-1])
        KE(0x11, 0, 0, 0)
        KE(86, 0, 0, 0)
        KE(86, 0, 2, 0)
        KE(0x11, 0, 2, 0)


if __name__ == '__main__':
    win0 = MainWindow()

# 打包
# pyinstaller -F -w -i ctos.ico TFillerFree.py
