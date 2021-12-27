from tkinter import *

class Bank(Frame):
    PIN = '0000'
    balance = 10000
    date = '23/03/2022'
    SMS = False

    def __init__(self, name=None):
        Frame.__init__(self, name)
        self.pack()
        bg = PhotoImage(file='Background.png')
        self.background = Label(image=bg)
        self.background.img = bg
        self.background.pack()

        # keyboard
        img = PhotoImage(file='B1.png')
        b1 = Button(self.background, highlightthickness=0, bd=0, height=30, width=30, image=img)
        self.b1 = img
        b1.place(x=354, y=396)

        img = PhotoImage(file='B2.png')
        b2 = Button(self.background, highlightthickness=0, bd=0, height=30, width=30, image=img)
        self.b2 = img
        b2.place(x=401, y=396)

        img = PhotoImage(file='B3.png')
        b3 = Button(self.background, highlightthickness=0, bd=0, height=30, width=30, image=img)
        self.b3 = img
        b3.place(x=447, y=396)

        img = PhotoImage(file='B4.png')
        b4 = Button(self.background, highlightthickness=0, bd=0, height=30, width=30, image=img)
        self.b4 = img
        b4.place(x=354, y=443)

        img = PhotoImage(file='B5.png')
        b5 = Button(self.background, highlightthickness=0, bd=0, height=30, width=30, image=img)
        self.b5 = img
        b5.place(x=401, y=443)

        img = PhotoImage(file='B6.png')
        b6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=30, image=img)
        self.b6 = img
        b6.place(x=447, y=443)

        img = PhotoImage(file='B7.png')
        b7 = Button(self.background, highlightthickness=0, bd=0, height=30, width=30, image=img)
        self.b7 = img
        b7.place(x=354, y=490)

        img = PhotoImage(file='B8.png')
        b8 = Button(self.background, highlightthickness=0, bd=0, height=30, width=30, image=img)
        self.b8 = img
        b8.place(x=401, y=490)

        img = PhotoImage(file='B9.png')
        b9 = Button(self.background, highlightthickness=0, bd=0, height=30, width=30, image=img)
        self.b9 = img
        b9.place(x=447, y=490)

        img = PhotoImage(file='B-.png')
        bmin = Button(self.background, highlightthickness=0, bd=0, height=30, width=30, image=img)
        self.bmin = img
        bmin.place(x=354, y=537)

        img = PhotoImage(file='B0.png')
        b0 = Button(self.background, highlightthickness=0, bd=0, height=30, width=30, image=img)
        self.b0 = img
        b0.place(x=401, y=537)

        img = PhotoImage(file='B+.png')
        bplus = Button(self.background, highlightthickness=0, bd=0, height=30, width=30, image=img)
        self.bplus = img
        bplus.place(x=447, y=537)

        img = PhotoImage(file='CANCEL.png')
        bcancel = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.bcancel = img
        bcancel.place(x=492, y=396)

        img = PhotoImage(file='CLEAR.png')
        bcl = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.bcl = img
        bcl.place(x=492, y=443)

        img = PhotoImage(file='ENTER.png')
        bent = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.bent = img
        bent.place(x=492, y=490)

        img = PhotoImage(file='B NO.png')
        bno = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.bno = img
        bno.place(x=492, y=537)

        # side buttons
        img = PhotoImage(file='SB.png')
        sb1 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
        self.sb1 = img
        sb1.place(x=55, y=146)

        sb2 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb2 = img
        sb2.place(x=55, y=195)

        sb3 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb3 = img
        sb3.place(x=55, y=244)

        sb4 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb4 = img
        sb4.place(x=55, y=293)

        sb5 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
        self.sb5 = img
        sb5.place(x=788, y=146)

        sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb6 = img
        sb6.place(x=788, y=195)

        sb7 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb7 = img
        sb7.place(x=788, y=244)

        sb8 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb8 = img
        sb8.place(x=788, y=293)

        img = PhotoImage(file='pay.png')
        bread = Button(self.background, highlightthickness=0, activebackground='#5E8A49', bd=0, height=151, width=115, image=img)
        self.bread = img
        bread.place(x=691, y=403)

        img = PhotoImage(file='addcard.png')
        crd = Button(self.background, highlightthickness=0, activebackground='#5E8A49', bd=0, height=37, width=223,
                       image=img, command=lambda: carddone())
        self.crd = img
        crd.place(x=50, y=430)

        def carddone():
            crd.place_forget()
            card_read()


        def card_read():
            bgs = []
            for step in range(1, 146):
                lnk = str(step) + '.png'
                bgs.append(lnk)

            def change(i=1):
                if i < 75:
                    img = bgs
                    img2 = PhotoImage(file=img[i])
                    self.background.configure(image=img2)
                    self.background.image = img2
                    self.background.after(1, change, i + 1)
                else:
                    pinwin()

            change()
            def pinwin():
                img2 = PhotoImage(file='pinwindow.png')
                self.background.configure(image=img2)
                self.background.image = img2
                print_wind = Entry(self.background, bd=0, show='*', font='Arial 30')
                print_wind.place(x=415, y=250, height=30, width=65)

                def print_digit(number):
                    value = print_wind.get() + str(number)
                    print_wind.delete(0, END)
                    print_wind.insert(0, value)

                def delete_digit():
                    value = print_wind.get()
                    value = value[:len(value) - 1]
                    print_wind.delete(0, END)
                    print_wind.insert(0, value)

                def clear():
                    value = ''
                    print_wind.delete(0, END)
                    print_wind.insert(0, value)

                def check_pin():
                    pin = Bank.PIN
                    value = print_wind.get()
                    value = value[:4]
                    if pin == value:
                        print_wind.place_forget()
                        self.main_page()
                    else:
                        print_wind.place_forget()
                        card_read()

                img = PhotoImage(file='B1.png')
                b1 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(1))
                self.b1 = img
                b1.place(x=354, y=396, height=30, width=30)

                img = PhotoImage(file='B2.png')
                b2 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(2))
                self.b2 = img
                b2.place(x=401, y=396, height=30, width=30)

                img = PhotoImage(file='B3.png')
                b3 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(3))
                self.b3 = img
                b3.place(x=447, y=396, height=30, width=30)

                img = PhotoImage(file='B4.png')
                b4 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(4))
                self.b4 = img
                b4.place(x=354, y=443, height=30, width=30)

                img = PhotoImage(file='B5.png')
                b5 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(5))
                self.b5 = img
                b5.place(x=401, y=443, height=30, width=30)

                img = PhotoImage(file='B6.png')
                b6 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(6))
                self.b6 = img
                b6.place(x=447, y=443, height=30, width=30)

                img = PhotoImage(file='B7.png')
                b7 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(7))
                self.b7 = img
                b7.place(x=354, y=490, height=30, width=30)

                img = PhotoImage(file='B8.png')
                b8 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(8))
                self.b8 = img
                b8.place(x=401, y=490, height=30, width=30)

                img = PhotoImage(file='B9.png')
                b9 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(9))
                self.b9 = img
                b9.place(x=447, y=490, height=30, width=30)

                img = PhotoImage(file='B0.png')
                b0 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(0))
                self.b0 = img
                b0.place(x=401, y=537, height=30, width=30)

                img = PhotoImage(file='CANCEL.png')
                bcancel = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                                 command=lambda: delete_digit())
                self.bcancel = img
                bcancel.place(x=492, y=396)

                img = PhotoImage(file='ENTER.png')
                bent = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                              command=lambda: check_pin())
                self.bent = img
                bent.place(x=492, y=490)

                img = PhotoImage(file='CLEAR.png')
                bcl = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                             command=lambda: clear())
                self.bcl = img
                bcl.place(x=492, y=443)

    def main_page(self):

        img3 = PhotoImage(file='mainpage.png')
        self.background.configure(image=img3)
        self.background.image = img3

        img = PhotoImage(file='SB.png')
        sb1 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img,
                     command=lambda: self.make_deposit())
        self.sb1 = img
        sb1.place(x=55, y=146)

        sb2 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: self.make_money())
        self.sb2 = img
        sb2.place(x=55, y=195)

        sb3 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: self.show_balance())
        self.sb3 = img
        sb3.place(x=55, y=244)

        sb4 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: self.show_user())
        self.sb4 = img
        sb4.place(x=55, y=293)

        sb5 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img,
                     command=lambda: self.show_info())
        self.sb5 = img
        sb5.place(x=788, y=146)

        sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: self.pin_checking())
        self.sb6 = img
        sb6.place(x=788, y=195)

        sb7 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: self.sms())
        self.sb7 = img
        sb7.place(x=788, y=244)

        sb8 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: quit())
        self.sb8 = img
        sb8.place(x=788, y=293)

        img = PhotoImage(file='ENTER.png')
        bent = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.bent = img
        bent.place(x=492, y=490)

    def show_balance(self):
        img3 = PhotoImage(file='showbalace.png')
        self.background.configure(image=img3)
        self.background.image = img3
        balance_info = Label(self.background, bg='#F8F8F8', highlightthickness=0, text=str(Bank.balance) + ' руб.',
                             font='Arial 15')
        balance_info.place(x=370, y=176)
        def close():
            balance_info.place_forget()
            self.main_page()

        img = PhotoImage(file='SB.png')
        sb4 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: close())
        self.sb4 = img
        sb4.place(x=55, y=293)

        sb8 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: quit())
        self.sb8 = img
        sb8.place(x=788, y=293)

        self.sb1 = img
        sb1 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
        sb1.place(x=55, y=146)

        sb2 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb2 = img
        sb2.place(x=55, y=195)

        sb3 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb3 = img
        sb3.place(x=55, y=244)

        sb5 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
        self.sb5 = img
        sb5.place(x=788, y=146)

        sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb6 = img
        sb6.place(x=788, y=195)

        sb7 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb7 = img
        sb7.place(x=788, y=244)

        img = PhotoImage(file='ENTER.png')
        bent = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.bent = img
        bent.place(x=492, y=490)

    def make_deposit(self):
        bgs = []
        for step in range(1, 37):
            lnk = 'load' + str(step) + '.png'
            bgs.append(lnk)

        def loading(i=1):
            if i < 35:
                img0 = bgs
                img7 = PhotoImage(file=img0[i])
                self.background.configure(image=img7)
                self.background.image = img7
                self.background.after(1, loading, i + 1)
            else:
                mkdep()

        loading()

        def mkdep():
            img4 = PhotoImage(file='makedep.png')
            self.background.configure(image=img4)
            self.background.image = img4
            print_wind = Entry(self.background, bd=0, font='Arial 20')
            print_wind.place(x=290, y=190, height=30, width=300)

            def print_digit(number):
                value = print_wind.get() + str(number)
                print_wind.delete(0, END)
                print_wind.insert(0, value)

            def delete_digit():
                value = print_wind.get()
                value = value[:len(value) - 1]
                print_wind.delete(0, END)
                print_wind.insert(0, value)

            def clear():
                value = ''
                print_wind.delete(0, END)
                print_wind.insert(0, value)

            def dep():
                sum = int(print_wind.get())
                Bank.balance += sum
                value = ''
                print_wind.delete(0, END)
                print_wind.insert(0, value)
                print_wind.place_forget()


                def loading(i=0):
                    bgs = []
                    for step in range(1, 36):
                        lnk = 'load' + str(step) + '.png'
                        bgs.append(lnk)
                    if i < 30:
                        img0 = bgs
                        img7 = PhotoImage(file=img0[i])
                        self.background.configure(image=img7)
                        self.background.image = img7
                        self.background.after(1, loading, i + 1)
                    else:
                        doing()
                loading()

                def doing(i=1):
                    bgs = []
                    for step in range(1, 7):
                        lnk = 'loaddone.png'
                        bgs.append(lnk)
                    if i < 5:
                        img5 = bgs
                        img6 = PhotoImage(file=img5[i])
                        self.background.configure(image=img6)
                        self.background.image = img6
                        self.background.after(1, doing, i + 1)
                    else:
                        self.make_deposit()

            def close():
                print_wind.place_forget()
                self.main_page()

            img = PhotoImage(file='B1.png')
            b1 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(1))
            self.b1 = img
            b1.place(x=354, y=396, height=30, width=30)

            img = PhotoImage(file='B2.png')
            b2 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(2))
            self.b2 = img
            b2.place(x=401, y=396, height=30, width=30)

            img = PhotoImage(file='B3.png')
            b3 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(3))
            self.b3 = img
            b3.place(x=447, y=396, height=30, width=30)

            img = PhotoImage(file='B4.png')
            b4 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(4))
            self.b4 = img
            b4.place(x=354, y=443, height=30, width=30)

            img = PhotoImage(file='B5.png')
            b5 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(5))
            self.b5 = img
            b5.place(x=401, y=443, height=30, width=30)

            img = PhotoImage(file='B6.png')
            b6 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(6))
            self.b6 = img
            b6.place(x=447, y=443, height=30, width=30)

            img = PhotoImage(file='B7.png')
            b7 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(7))
            self.b7 = img
            b7.place(x=354, y=490, height=30, width=30)

            img = PhotoImage(file='B8.png')
            b8 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(8))
            self.b8 = img
            b8.place(x=401, y=490, height=30, width=30)

            img = PhotoImage(file='B9.png')
            b9 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(9))
            self.b9 = img
            b9.place(x=447, y=490, height=30, width=30)

            img = PhotoImage(file='B0.png')
            b0 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(0))
            self.b0 = img
            b0.place(x=401, y=537, height=30, width=30)

            img = PhotoImage(file='CANCEL.png')
            bcancel = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                             command=lambda: delete_digit())
            self.bcancel = img
            bcancel.place(x=492, y=396)

            img = PhotoImage(file='ENTER.png')
            bent = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                          command=lambda: dep())
            self.bent = img
            bent.place(x=492, y=490)

            img = PhotoImage(file='CLEAR.png')
            bcl = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: clear())
            self.bcl = img
            bcl.place(x=492, y=443)

            img = PhotoImage(file='SB.png')
            sb8 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: quit())
            self.sb8 = img
            sb8.place(x=788, y=293)

            sb4 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: close())
            self.sb4 = img
            sb4.place(x=55, y=293)

            sb1 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
            self.sb1 = img
            sb1.place(x=55, y=146)

            sb2 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb2 = img
            sb2.place(x=55, y=195)

            sb3 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb3 = img
            sb3.place(x=55, y=244)

            sb5 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
            self.sb5 = img
            sb5.place(x=788, y=146)

            sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb6 = img
            sb6.place(x=788, y=195)

            sb7 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb7 = img
            sb7.place(x=788, y=244)


    def make_money(self):
        bgs = []
        for step in range(1, 37):
            lnk = 'load' + str(step) + '.png'
            bgs.append(lnk)

        def loading(i=1):
            if i < 34:
                img0 = bgs
                img7 = PhotoImage(file=img0[i])
                self.background.configure(image=img7)
                self.background.image = img7
                self.background.after(1, loading, i + 1)
            else:
                mkmon()

        loading()

        def mkmon():
            img4 = PhotoImage(file='makemon.png')
            self.background.configure(image=img4)
            self.background.image = img4
            print_wind = Entry(self.background, bd=0, font='Arial 20')
            print_wind.place(x=290, y=190, height=30, width=300)

            def print_digit(number):
                value = print_wind.get() + str(number)
                print_wind.delete(0, END)
                print_wind.insert(0, value)

            def delete_digit():
                value = print_wind.get()
                value = value[:len(value) - 1]
                print_wind.delete(0, END)
                print_wind.insert(0, value)

            def clear():
                value = ''
                print_wind.delete(0, END)
                print_wind.insert(0, value)

            def make():
                sum = int(print_wind.get())
                if sum <= Bank.balance:
                    Bank.balance -= sum
                    bgs = []
                    for step in range(1, 37):
                        lnk = 'load' + str(step) + '.png'
                        bgs.append(lnk)

                    def loading(i=1):
                        if i < 34:
                            img0 = bgs
                            img7 = PhotoImage(file=img0[i])
                            self.background.configure(image=img7)
                            self.background.image = img7
                            self.background.after(1, loading, i + 1)
                        else:
                            doing()

                    loading()

                    def doing(i=1):
                        bgs = []
                        for step in range(1, 7):
                            lnk = 'loaddone.png'
                            bgs.append(lnk)
                        if i < 6:
                            img5 = bgs
                            img6 = PhotoImage(file=img5[i])
                            self.background.configure(image=img6)
                            self.background.image = img6
                            self.background.after(1, doing, i + 1)
                        else:
                            print_wind.place_forget()
                            self.make_money()

                else:
                    Bank.balance = 0
                    value = ''
                    print_wind.delete(0, END)
                    print_wind.insert(0, value)

            def close():
                print_wind.place_forget()
                self.main_page()

            img = PhotoImage(file='B1.png')
            b1 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(1))
            self.b1 = img
            b1.place(x=354, y=396, height=30, width=30)

            img = PhotoImage(file='B2.png')
            b2 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(2))
            self.b2 = img
            b2.place(x=401, y=396, height=30, width=30)

            img = PhotoImage(file='B3.png')
            b3 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(3))
            self.b3 = img
            b3.place(x=447, y=396, height=30, width=30)

            img = PhotoImage(file='B4.png')
            b4 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(4))
            self.b4 = img
            b4.place(x=354, y=443, height=30, width=30)

            img = PhotoImage(file='B5.png')
            b5 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(5))
            self.b5 = img
            b5.place(x=401, y=443, height=30, width=30)

            img = PhotoImage(file='B6.png')
            b6 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(6))
            self.b6 = img
            b6.place(x=447, y=443, height=30, width=30)

            img = PhotoImage(file='B7.png')
            b7 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(7))
            self.b7 = img
            b7.place(x=354, y=490, height=30, width=30)

            img = PhotoImage(file='B8.png')
            b8 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(8))
            self.b8 = img
            b8.place(x=401, y=490, height=30, width=30)

            img = PhotoImage(file='B9.png')
            b9 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(9))
            self.b9 = img
            b9.place(x=447, y=490, height=30, width=30)

            img = PhotoImage(file='B0.png')
            b0 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(0))
            self.b0 = img
            b0.place(x=401, y=537, height=30, width=30)

            img = PhotoImage(file='CANCEL.png')
            bcancel = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                             command=lambda: delete_digit())
            self.bcancel = img
            bcancel.place(x=492, y=396)

            img = PhotoImage(file='ENTER.png')
            bent = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                          command=lambda: make())
            self.bent = img
            bent.place(x=492, y=490)

            img = PhotoImage(file='CLEAR.png')
            bcl = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: clear())
            self.bcl = img
            bcl.place(x=492, y=443)

            img = PhotoImage(file='SB.png')
            sb8 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: quit())
            self.sb8 = img
            sb8.place(x=788, y=293)

            sb4 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: close())
            self.sb4 = img
            sb4.place(x=55, y=293)

            sb1 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
            self.sb1 = img
            sb1.place(x=55, y=146)

            sb2 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb2 = img
            sb2.place(x=55, y=195)

            sb3 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb3 = img
            sb3.place(x=55, y=244)

            sb5 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
            self.sb5 = img
            sb5.place(x=788, y=146)

            sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb6 = img
            sb6.place(x=788, y=195)

            sb7 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb7 = img
            sb7.place(x=788, y=244)

    def show_user(self):
        img3 = PhotoImage(file='user.png')
        self.background.configure(image=img3)
        self.background.image = img3

        def close():
            user_info.place_forget()
            self.main_page()

        user_info = Label(self.background, bg='#F8F8F8', highlightthickness=0, text='Браер П.С.',
                             font='Arial 18')
        user_info.place(x=500, y=176)

        img = PhotoImage(file='SB.png')
        sb4 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: close())
        self.sb4 = img
        sb4.place(x=55, y=293)

        sb8 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: quit())
        self.sb8 = img
        sb8.place(x=788, y=293)

        sb1 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
        self.sb1 = img
        sb1.place(x=55, y=146)

        sb2 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb2 = img
        sb2.place(x=55, y=195)

        sb3 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb3 = img
        sb3.place(x=55, y=244)

        sb5 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
        self.sb5 = img
        sb5.place(x=788, y=146)

        sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb6 = img
        sb6.place(x=788, y=195)

        sb7 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb7 = img
        sb7.place(x=788, y=244)

        img = PhotoImage(file='ENTER.png')
        bent = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.bent = img
        bent.place(x=492, y=490)

    def show_info(self):
        img3 = PhotoImage(file='info.png')
        self.background.configure(image=img3)
        self.background.image = img3

        def close():
            user_info.place_forget()
            balance_info.place_forget()
            date_info.place_forget()
            self.main_page()

        user_info = Label(self.background, bg='#F8F8F8', highlightthickness=0, text='Браер П.С.',
                             font='Arial 14')
        user_info.place(x=500, y=150)

        balance_info = Label(self.background, bg='#F8F8F8', highlightthickness=0, text=str(Bank.balance) + ' руб.',
                             font='Arial 14')
        balance_info.place(x=500, y=185)

        date_info = Label(self.background, bg='#F8F8F8', highlightthickness=0, text=Bank.date,
                             font='Arial 14')
        date_info.place(x=500, y=215)

        img = PhotoImage(file='SB.png')
        sb4 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: close())
        self.sb4 = img
        sb4.place(x=55, y=293)

        sb8 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: quit())
        self.sb8 = img
        sb8.place(x=788, y=293)

        sb1 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
        self.sb1 = img
        sb1.place(x=55, y=146)

        sb2 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb2 = img
        sb2.place(x=55, y=195)

        sb3 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb3 = img
        sb3.place(x=55, y=244)

        sb5 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
        self.sb5 = img
        sb5.place(x=788, y=146)

        sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb6 = img
        sb6.place(x=788, y=195)

        sb7 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb7 = img
        sb7.place(x=788, y=244)

    def sms(self):
        bgs = []
        for step in range(1, 37):
            lnk = 'load' + str(step) + '.png'
            bgs.append(lnk)

        def loading(i=1):
            if i < 34:
                img0 = bgs
                img7 = PhotoImage(file=img0[i])
                self.background.configure(image=img7)
                self.background.image = img7
                self.background.after(1, loading, i + 1)
            else:
                if Bank.SMS == False:
                    img3 = PhotoImage(file='smsoff.png')
                    self.background.configure(image=img3)
                    self.background.image = img3
                elif Bank.SMS == True:
                    img3 = PhotoImage(file='smson.png')
                    self.background.configure(image=img3)
                    self.background.image = img3

        loading()
        if Bank.SMS == False:
            img3 = PhotoImage(file='smsoff.png')
            self.background.configure(image=img3)
            self.background.image = img3

            def turn():
                Bank.SMS = True
                self.sms()

            img = PhotoImage(file='SB.png')
            sb4 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: self.main_page())
            self.sb4 = img
            sb4.place(x=55, y=293)

            sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: turn())
            self.sb6 = img
            sb6.place(x=788, y=195)

            sb8 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: quit())
            self.sb8 = img
            sb8.place(x=788, y=293)

            sb1 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
            self.sb1 = img
            sb1.place(x=55, y=146)

            sb2 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb2 = img
            sb2.place(x=55, y=195)

            sb3 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb3 = img
            sb3.place(x=55, y=244)

            sb5 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
            self.sb5 = img
            sb5.place(x=788, y=146)

            sb7 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb7 = img
            sb7.place(x=788, y=244)

            img = PhotoImage(file='ENTER.png')
            bent = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.bent = img
            bent.place(x=492, y=490)

        elif Bank.SMS == True:
            img3 = PhotoImage(file='smson.png')
            self.background.configure(image=img3)
            self.background.image = img3

            def turn():
                Bank.SMS = False
                self.sms()

            img = PhotoImage(file='SB.png')
            sb4 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: self.main_page())
            self.sb4 = img
            sb4.place(x=55, y=293)

            sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: turn())
            self.sb6 = img
            sb6.place(x=788, y=195)

            sb8 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: quit())
            self.sb8 = img
            sb8.place(x=788, y=293)

            sb1 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
            self.sb1 = img
            sb1.place(x=55, y=146)

            sb2 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb2 = img
            sb2.place(x=55, y=195)

            sb3 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb3 = img
            sb3.place(x=55, y=244)

            sb5 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
            self.sb5 = img
            sb5.place(x=788, y=146)

            sb7 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.sb7 = img
            sb7.place(x=788, y=244)

            img = PhotoImage(file='ENTER.png')
            bent = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
            self.bent = img
            bent.place(x=492, y=490)

    def pin_checking(self):
        img2 = PhotoImage(file='pinwindow.png')
        self.background.configure(image=img2)
        self.background.image = img2
        print_wind = Entry(self.background, bd=0, show='*', font='Arial 30')
        print_wind.place(x=415, y=250, height=30, width=65)

        def print_digit(number):
            value = print_wind.get() + str(number)
            print_wind.delete(0, END)
            print_wind.insert(0, value)

        def delete_digit():
            value = print_wind.get()
            value = value[:len(value) - 1]
            print_wind.delete(0, END)
            print_wind.insert(0, value)

        def clear():
            value = ''
            print_wind.delete(0, END)
            print_wind.insert(0, value)

        def check_pin():
            pin = Bank.PIN
            value = print_wind.get()
            value = value[:4]
            if pin == value:
                print_wind.place_forget()
                self.new_pin()
            else:
                print_wind.place_forget()
                self.main_page()

        img = PhotoImage(file='B1.png')
        b1 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(1))
        self.b1 = img
        b1.place(x=354, y=396, height=30, width=30)

        img = PhotoImage(file='B2.png')
        b2 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(2))
        self.b2 = img
        b2.place(x=401, y=396, height=30, width=30)

        img = PhotoImage(file='B3.png')
        b3 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(3))
        self.b3 = img
        b3.place(x=447, y=396, height=30, width=30)

        img = PhotoImage(file='B4.png')
        b4 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(4))
        self.b4 = img
        b4.place(x=354, y=443, height=30, width=30)

        img = PhotoImage(file='B5.png')
        b5 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(5))
        self.b5 = img
        b5.place(x=401, y=443, height=30, width=30)

        img = PhotoImage(file='B6.png')
        b6 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(6))
        self.b6 = img
        b6.place(x=447, y=443, height=30, width=30)

        img = PhotoImage(file='B7.png')
        b7 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(9))
        self.b7 = img
        b7.place(x=354, y=490, height=30, width=30)

        img = PhotoImage(file='B8.png')
        b8 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(8))
        self.b8 = img
        b8.place(x=401, y=490, height=30, width=30)

        img = PhotoImage(file='B9.png')
        b9 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(9))
        self.b9 = img
        b9.place(x=447, y=490, height=30, width=30)

        img = PhotoImage(file='B0.png')
        b0 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(0))
        self.b0 = img
        b0.place(x=401, y=537, height=30, width=30)

        img = PhotoImage(file='CANCEL.png')
        bcancel = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: delete_digit())
        self.bcancel = img
        bcancel.place(x=492, y=396)

        img = PhotoImage(file='ENTER.png')
        bent = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                      command=lambda: check_pin())
        self.bent = img
        bent.place(x=492, y=490)

        img = PhotoImage(file='CLEAR.png')
        bcl = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: clear())
        self.bcl = img
        bcl.place(x=492, y=443)

        img = PhotoImage(file='SB.png')
        sb4 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: self.main_page())
        self.sb4 = img
        sb4.place(x=55, y=293)

        sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: turn())
        self.sb6 = img
        sb6.place(x=788, y=195)

        sb8 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: quit())
        self.sb8 = img
        sb8.place(x=788, y=293)

        sb1 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
        self.sb1 = img
        sb1.place(x=55, y=146)

        sb2 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb2 = img
        sb2.place(x=55, y=195)

        sb3 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb3 = img
        sb3.place(x=55, y=244)

        sb5 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
        self.sb5 = img
        sb5.place(x=788, y=146)

        sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb6 = img
        sb6.place(x=788, y=195)

        sb7 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb7 = img
        sb7.place(x=788, y=244)

    def new_pin(self):
        img2 = PhotoImage(file='newpin.png')
        self.background.configure(image=img2)
        self.background.image = img2
        print_wind = Entry(self.background, bd=0, font='Arial 20')
        print_wind.place(x=545, y=185, height=25, width=65)

        def print_digit(number):
            value = print_wind.get() + str(number)
            print_wind.delete(0, END)
            print_wind.insert(0, value)

        def delete_digit():
            value = print_wind.get()
            value = value[:len(value) - 1]
            print_wind.delete(0, END)
            print_wind.insert(0, value)

        def clear():
            value = ''
            print_wind.delete(0, END)
            print_wind.insert(0, value)

        def change_pin():
            value = print_wind.get()
            value = value[:4]
            print_wind.place_forget()
            Bank.PIN = value
            self.main_page()

        def bck():
            print_wind.place_forget()
            self.main_page()

        img = PhotoImage(file='B1.png')
        b1 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(1))
        self.b1 = img
        b1.place(x=354, y=396, height=30, width=30)

        img = PhotoImage(file='B2.png')
        b2 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(2))
        self.b2 = img
        b2.place(x=401, y=396, height=30, width=30)

        img = PhotoImage(file='B3.png')
        b3 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(3))
        self.b3 = img
        b3.place(x=447, y=396, height=30, width=30)

        img = PhotoImage(file='B4.png')
        b4 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(4))
        self.b4 = img
        b4.place(x=354, y=443, height=30, width=30)

        img = PhotoImage(file='B5.png')
        b5 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(5))
        self.b5 = img
        b5.place(x=401, y=443, height=30, width=30)

        img = PhotoImage(file='B6.png')
        b6 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(6))
        self.b6 = img
        b6.place(x=447, y=443, height=30, width=30)

        img = PhotoImage(file='B7.png')
        b7 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(9))
        self.b7 = img
        b7.place(x=354, y=490, height=30, width=30)

        img = PhotoImage(file='B8.png')
        b8 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(8))
        self.b8 = img
        b8.place(x=401, y=490, height=30, width=30)

        img = PhotoImage(file='B9.png')
        b9 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(9))
        self.b9 = img
        b9.place(x=447, y=490, height=30, width=30)

        img = PhotoImage(file='B0.png')
        b0 = Button(self.background, highlightthickness=0, bd=0, image=img, command=lambda: print_digit(0))
        self.b0 = img
        b0.place(x=401, y=537, height=30, width=30)

        img = PhotoImage(file='CANCEL.png')
        bcancel = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                         command=lambda: delete_digit())
        self.bcancel = img
        bcancel.place(x=492, y=396)

        img = PhotoImage(file='ENTER.png')
        bent = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                      command=lambda: change_pin())
        self.bent = img
        bent.place(x=492, y=490)

        img = PhotoImage(file='CLEAR.png')
        bcl = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: clear())
        self.bcl = img
        bcl.place(x=492, y=443)

        img = PhotoImage(file='SB.png')
        sb4 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img,
                     command=lambda: bck())
        self.sb4 = img
        sb4.place(x=55, y=293)

        sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb6 = img
        sb6.place(x=788, y=195)

        sb8 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb8 = img
        sb8.place(x=788, y=293)

        sb1 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
        self.sb1 = img
        sb1.place(x=55, y=146)

        sb2 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb2 = img
        sb2.place(x=55, y=195)

        sb3 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb3 = img
        sb3.place(x=55, y=244)

        sb5 = Button(self.background, highlightthickness=0, bd=0, height=30, width=54, image=img)
        self.sb5 = img
        sb5.place(x=788, y=146)

        sb6 = Button(self.background, highlightthickness=0, bd=0, height=30, width=55, image=img)
        self.sb6 = img
        sb6.place(x=788, y=195)


root = Tk()
tk = Bank(name=root)
root.title('Сбербанк')

tk.mainloop()
