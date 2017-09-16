import tkinter as tk
import crypt


class XE_CRYPTO(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand='true')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Main, First, Second):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(Main)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Main(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        buttonframe = tk.Frame(self, width=250, height=200, bg="gray32")
        buttonframe.pack(fill='both', expand='yes', side='top')
        start_button = tk.Button(buttonframe, height=4, width=4, font=("Courier New", 18), text="Encrypt", command=lambda: controller.show_frame(First))
        start_button.pack(side='left', expand='yes', fill='x')
        decrypt_button = tk.Button(buttonframe, height=4,  width=4, font=("Courier New", 18), text="Decrypt", command=lambda: controller.show_frame(Second))
        decrypt_button.pack(side='left', expand='yes', fill='x')

        addLabel = tk.Label(self, font=("courier New", 14), bg="gray32", fg="white", text="Based on XE Cryption Algorithm").pack(side='top', fill='x', expand='true')
        img = tk.PhotoImage(file='pic.png')
        picLabel = tk.Label(self, image=img, bg="gray32")
        picLabel.image = img
        picLabel.pack(side='top', fill='both', expand='true')

        status = tk.Label(self, text="Thanks for using...", font=("Courier New", 9), bd=1, anchor='w')
        status.pack(side='bottom', fill='x')


class First(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        buttonframe = tk.Frame(self, width=250, height=250)
        buttonframe.pack(fill='both', expand='yes', side='top')
        start_button = tk.Button(buttonframe, width=77, font=("Courier New", 9), text="Main", command=lambda: controller.show_frame(Main))
        start_button.pack(side='left', expand='yes', fill='x')
        decrypt_button = tk.Button(buttonframe, width=77, font=("Courier New", 9), text="Decrypt", command=lambda: controller.show_frame(Second))
        decrypt_button.pack(side='left', expand='yes', fill='x')

        label1_1 = tk.Label(self, height=1, font=("Courier New", 11), text="Enter the message below to be encrypted", bg="gray32", fg="white")
        label1_1.pack(side='top', fill='x', expand='yes')

        textframe1 = tk.Frame(self, bg="gray32", width=400, height=250)
        textframe1.pack(side='top', fill='both', expand='true')
        textframe1.grid_propagate(False)
        textframe1.grid_rowconfigure(0, weight=1)
        textframe1.grid_columnconfigure(0, weight=1)

        text1 = tk.Text(textframe1, borderwidth=3, relief="sunken")
        text1.config(font=("Courier New", 9), undo='true', wrap='word')
        text1.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)

        scroll = tk.Scrollbar(textframe1, command=text1.yview)
        scroll.grid(row=0, column=1, sticky='nsew')
        text1['yscrollcommand'] = scroll.set

        passframe = tk.Frame(self, width=400, height=20)
        passframe.pack(side='top', expand='true')
        passlabel = tk.Label(passframe, text="Enter the password", font=("Courier New", 9), bg="gray32", fg="white", width=50)
        passlabel.pack(side='left', expand='true')
        password = tk.Text(passframe, height=1, font=("Courier New", 11))
        password.pack(side='right', fill='x', expand='true')

        def encryption():
            m = text1.get("1.0", "end-1c")
            p = password.get("1.0", "end-1c")
            code = crypt.encrypt(m, p)
            return code

        encrypt_now_button = tk.Button(self, text="Encrypt Now", font=("Courier New", 11), width=50, command=lambda: X())
        encrypt_now_button.pack(side='top', expand='yes', fill='x')

        label1_1 = tk.Label(self, height=1, font=("Courier New", 11), text="Please copy the encrypted code", bg="gray32", fg="white")
        label1_1.pack(side='top', fill='x', expand='yes')

        textframe12 = tk.Frame(self, bg="gray32", width=400, height=200)
        textframe12.pack(side='top', fill='both', expand='true')
        textframe12.grid_propagate(False)
        textframe12.grid_rowconfigure(0, weight=1)
        textframe12.grid_columnconfigure(0, weight=1)

        text12 = tk.Text(textframe12, borderwidth=3, relief="sunken")
        text12.config(font=("Courier New", 9), undo='true', wrap='word')
        text12.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)

        scroll2 = tk.Scrollbar(textframe12, command=text12.yview)
        scroll2.grid(row=0, column=1, sticky='nsew')
        text12['yscrollcommand'] = scroll2.set

        def X():
            code = encryption()
            XEcode = code
            text12.delete("1.0", "end-1c")
            text12.insert(tk.END, XEcode)

        status = tk.Label(self, text="Thanks for using...", font=("Courier New", 9), bd=1, anchor='w')
        status.pack(side='top', fill='x')

class Second(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        buttonframe = tk.Frame(self, width=250, height=250)
        buttonframe.pack(fill='both', expand='yes', side='top')
        start_button = tk.Button(buttonframe, width=77, font=("Courier New", 9), text="Encrypt", command=lambda: controller.show_frame(First))
        start_button.pack(side='left', expand='yes', fill='x')
        decrypt_button = tk.Button(buttonframe, width=77, font=("Courier New", 9), text="Main", command=lambda: controller.show_frame(Main))
        decrypt_button.pack(side='left', expand='yes', fill='x')

        label2_1 = tk.Label(self, height=1, font=("Courier New", 11), text="Paste the XE code below to decrypt", bg="gray32", fg="white")
        label2_1.pack(side='top', fill='x', expand='yes')

        textframe2 = tk.Frame(self, bg="gray32", width=400, height=250)
        textframe2.pack(side='top', fill='both', expand='true')
        textframe2.grid_propagate(False)
        textframe2.grid_rowconfigure(0, weight=1)
        textframe2.grid_columnconfigure(0, weight=1)

        text2 = tk.Text(textframe2, borderwidth=3, relief="sunken")
        text2.config(font=("Courier New", 9), undo='true', wrap='word')
        text2.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)

        scroll = tk.Scrollbar(textframe2, command=text2.yview)
        scroll.grid(row=0, column=1, sticky='nsew')
        text2['yscrollcommand'] = scroll.set

        passframe = tk.Frame(self, width=400, height=20)
        passframe.pack(side='top', expand='true')
        passlabel = tk.Label(passframe, text="Enter the password", font=("Courier New", 9), bg="gray32", fg="white", width=50)
        passlabel.pack(side='left', expand='true')
        password = tk.Text(passframe, height=1, font=("Courier New", 11))
        password.pack(side='right', fill='x', expand='true')

        def decryption():
            c = text2.get("1.0", "end-1c")
            p = password.get("1.0", "end-1c")
            message = crypt.decrypt(c, p)
            return message

        decrypt_now_button = tk.Button(self, text="Decrypt Now", font=("Courier New", 11), width=50, command=lambda: D())
        decrypt_now_button.pack(side='top', expand='yes', fill='x')

        label2_1 = tk.Label(self, height=1, font=("Courier New", 11), text="Please copy the message", bg="gray32", fg="white")
        label2_1.pack(side='top', fill='x', expand='yes')

        textframe22 = tk.Frame(self, bg="gray32", width=400, height=200)
        textframe22.pack(side='top', fill='both', expand='true')
        textframe22.grid_propagate(False)
        textframe22.grid_rowconfigure(0, weight=1)
        textframe22.grid_columnconfigure(0, weight=1)

        text22 = tk.Text(textframe22, borderwidth=3, relief="sunken")
        text22.config(font=("Courier New", 9), undo='true', wrap='word')
        text22.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)

        scroll2 = tk.Scrollbar(textframe22, command=text22.yview)
        scroll2.grid(row=0, column=1, sticky='nsew')
        text22['yscrollcommand'] = scroll2.set

        def D():
            code = decryption()
            XEcode = code
            text22.delete("1.0", "end-1c")
            text22.insert(tk.END, XEcode)

        status = tk.Label(self, text="Thanks for using...", font=("Courier New", 9), bd=1, anchor='w')
        status.pack(side='top', fill='x')


XE = XE_CRYPTO()
XE.title('XE-Crypto')
XE.wm_iconbitmap('icon.ico')
XE.mainloop()


