#! /usr/bin/env python3
#coding: utf-8

from tkinter import *
from tkinter import ttk
from libs.SimxConf import *
from libs.Iocp import *
import os


class Fenetre():
    def __init__(self):

        self.dataDict = -1
        

        self.fen = Tk()
        self.fen.minsize(900,600)
        self.fen.title("Aircraft Data Controler")
        self.alti = StringVar()
        self.alti.set("00000")
        self.speed = StringVar()
        self.speed.set("000")
        self.crs_nav1 = StringVar()
        self.crs_nav1.set("000")
        self.crs_nav2 = StringVar()
        self.crs_nav2.set("000")
        self.obs_nav1 =StringVar()
        self.obs_nav2 = StringVar()
        self.nav1_dec = StringVar()
        self.nav1_dec.set("111")
        self.nav1_inc = StringVar()
        self.nav1_inc.set("10")
        self.nav2_dec = StringVar()
        self.nav2_dec.set("111")
        self.nav2_inc = StringVar()
        self.nav2_inc.set("10")
        self.adf_freq = StringVar()
        self.adf_freq.set("200")
        self.dst_adf = StringVar()
        self.dst_adf.set("000")
        self.crs_adf = StringVar()
        self.crs_adf.set("000")



        self.widgets()

        
        # conf file for ip port and xplane var
        dirName = os.path.dirname(__file__)
        conFile = os.path.join(dirName,"simx.conf")
        self.conf = SimxConf(conFile)

        if self.conf.get() == -1:
            print("Unable to read the file")
            exit(-1)

        self.adr_ip.set(self.conf.getIp())
        self.adr_port.set(self.conf.getPort())

        print(self.adr_ip.get())

        self.iocp = Iocp()
        
        
    def widgets(self):

        # top of window
        frame1 = Frame(self.fen, relief="groove")
        frame1.pack(fill='x',padx=5, pady=10)

            # left side
        frame2 = Frame(frame1, borderwidth=2, relief="sunken")
        frame2.pack(side="left")

        lab_ip = Label(frame2)
        lab_ip.config(text="IP Server: ")
        lab_ip.pack(side="left",padx=3)

        
        self.adr_ip = StringVar()
        self.ent_ip = Entry(frame2, width=14, textvariable= self.adr_ip)
        self.ent_ip.pack(side="left", padx=3)

        lab_port = Label(frame2)
        lab_port.config(text="Port: ")
        lab_port.pack(side="left",padx=3)

        self.adr_port = StringVar()
        self.ent_port = Entry(frame2, width=5, textvariable=self.adr_port)
        self.ent_port.pack(side="left", padx=3)


            # right side
        frame3 = Frame(frame1, borderwidth=2, relief="sunken")
        frame3.pack(side="right")

        self.but_connect = Button(frame3, command= self.connect)
        self.but_connect.configure(text="Connect")
        self.but_connect.pack(side="left",padx=10)

        but_disco = Button(frame3, command = self.disconnect)
        but_disco.configure(text="Disconnect")
        but_disco.pack(side="left", padx=10)





        #heart of window
        frame4 = Frame(self.fen)
        frame4.pack(expand=1, fill="both")

        # tabs
        tab = ttk.Notebook(frame4)
        tab.pack(expand=1, fill="both")



            #tab sys
        tab1= ttk.Frame(tab, padding=(5,5,5,5),borderwidth=3, relief="sunken")
        tab1.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), weight=1)
        tab1.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), weight=1)


        Label(tab1, text="Battery").grid(column=0, row=1, sticky='w')
        self.bat_on = Button(tab1, text="ON", relief="raised", command= self.but_on_fn)
        self.bat_on.grid(column=2, row=1,padx=2)
        self.bat_off = Button(tab1, text="OFF", relief="raised", command=self.but_off_fn)
        self.bat_off.grid(column=3, row=1,padx=2)
        Label(tab1,text="Generator 1").grid(column=0, row=2, sticky='w')
        self.gen1_on = Button(tab1, text="ON", relief="raised",command=self.gen1_on_but)
        self.gen1_on.grid(column=2,row=2)
        self.gen1_off = Button(tab1, text="OFF", relief="raised",command=self.gen1_off_but)
        self.gen1_off.grid(column=3,row=2)
        Label(tab1, text="Generator 2").grid(column=0, row=3, sticky='w')
        self.gen2_on = Button(tab1, text="ON", relief="raised",command=self.gen2_on_but)
        self.gen2_on.grid(column=2,row=3)
        self.gen2_off = Button(tab1, text="OFF", relief="raised",command=self.gen2_off_but)
        self.gen2_off.grid(column=3,row=3)
        Label(tab1, text="Inverter 1").grid(column=0, row=4, sticky='w')
        self.inv1_on = Button(tab1, text="ON", relief="raised",command=self.inv1_on_but)
        self.inv1_on.grid(column=2,row=4)
        self.inv1_off = Button(tab1, text="OFF",  relief="raised",command=self.inv1_off_but)
        self.inv1_off.grid(column=3,row=4)
        Label(tab1, text="Inverter 2").grid(column=0, row=5, sticky='w')
        self.inv2_on = Button(tab1, text="ON", relief="raised",command=self.inv2_on_but)
        self.inv2_on.grid(column=2,row=5)
        self.inv2_off = Button(tab1, text="OFF",  relief="raised",command=self.inv2_off_but)
        self.inv2_off.grid(column=3,row=5)
        Label(tab1,text="HUD").grid(column=0,row=6,sticky="w")
        self.hud_on = Button(tab1,text="ON",relief="raised",command=self.hud_on_but)
        self.hud_on.grid(column=2,row=6)
        self.hud_off = Button(tab1,text="OFF",relief="raised",command=self.hud_off_but)
        self.hud_off.grid(column=3,row=6)
        Label(tab1,text="Pitot").grid(column=0,row=7,sticky="w")
        self.pitot_on = Button(tab1,text="ON",relief="raised",command=self.pitot_on_but)
        self.pitot_on.grid(column=2,row=7)
        self.pitot_off = Button(tab1,text="OFF",relief="raised",command=self.pitot_off_but)
        self.pitot_off.grid(column=3,row=7)
        Label(tab1,text="Hydrau").grid(column=0,row=8,sticky="w")
        self.hydrau_on = Button(tab1,text="ON",relief="raised",command=self.hydrau_on_but)
        self.hydrau_on.grid(column=2,row=8)
        self.hydrau_off = Button(tab1,text="OFF",relief="raised",command=self.hydrau_off_but)
        self.hydrau_off.grid(column=3,row=8)

        

        ttk.Separator(tab1, orient="vertical").grid(column=6, row=0,rowspan=20, padx=10, sticky="ns")




            #tab instru
        tab2= ttk.Frame(tab, padding=(5,5,5,5),borderwidth=3, relief="sunken")
        tab2.columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
        tab2.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        Label(tab2, text="Altitude  Ft: ").grid(column=0, row=1, sticky='w')
        self.lab_alti = Label(tab2,text="00 000", textvariable=self.alti)
        self.lab_alti.grid(column=1, row=1)
        Label(tab2, text="Speed  Kt: ").grid(column=0, row=2, sticky='w')
        self.lab_speed = Label(tab2,text="000",textvariable=self.speed)
        self.lab_speed.grid(column=1, row=2)

            #tab radios
        tab3= ttk.Frame(tab, padding=(5,5,5,5),borderwidth=3, relief="sunken")
        tab3.columnconfigure((1,10), weight=1)
        tab3.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        Label(tab3,text="Nav 1: ").grid(column=0, row=1,sticky='w')
        self.nav1_pwr = Button(tab3,text="PWR",command=self.nav1_but_pwr)
        self.nav1_pwr.grid(column=2,row=1,padx=5)
        Label(tab3,text="Freq:").grid(column=3,row=1,padx=10)
        nav1_freq_dec = Spinbox(tab3,from_=108, to=117,width=3,textvariable=self.nav1_dec)
        nav1_freq_dec.grid(column=4,row=1)
        nav1_freq_inc = Spinbox(tab3,from_=00,to=95,increment=5,width=2,textvariable=self.nav1_inc)
        nav1_freq_inc.grid(column=5,row=1)
        self.nav1_set = Button(tab3,text="Set",command=self.nav1_but_set)
        self.nav1_set.grid(column=6,row=1,padx=10)
        nav1_obs = Spinbox(tab3,from_=1,to=360,width=3,textvariable=self.obs_nav1)
        nav1_obs.grid(column=8,row=1)
        self.nav1_obs_set = Button(tab3,text="Obs set",command=self.nav1_but_obs)
        self.nav1_obs_set.grid(column=9,row=1,padx=5)
        nav1_crs = Label(tab3,bd=4,width=3,relief="ridge",textvariable=self.crs_nav1)
        nav1_crs.grid(column=11,row=1)
        nav1_lab_crs = Label(tab3,text="Course")
        nav1_lab_crs.grid(column=12, row=1,padx=5)

        Label(tab3,text="Nav 2: ").grid(column=0, row=2,sticky='w')
        self.nav2_pwr = Button(tab3,text="PWR",command=self.nav2_but_pwr)
        self.nav2_pwr.grid(column=2,row=2,padx=5)
        Label(tab3,text="Freq:").grid(column=3,row=2,padx=10)
        nav2_freq_dec = Spinbox(tab3,from_=108, to=117,width=3,textvariable=self.nav2_dec)
        nav2_freq_dec.grid(column=4,row=2)
        nav2_freq_inc = Spinbox(tab3,from_=00,to=95,increment=5,width=2,textvariable=self.nav2_inc)
        nav2_freq_inc.grid(column=5,row=2)
        self.nav2_set = Button(tab3,text="Set",command=self.nav2_but_set)
        self.nav2_set.grid(column=6,row=2,padx=10)
        nav2_obs = Spinbox(tab3,from_=1,to=360,width=3,textvariable=self.obs_nav2)
        nav2_obs.grid(column=8,row=2)
        self.nav2_obs_set = Button(tab3,text="Obs set",command=self.nav2_but_obs)
        self.nav2_obs_set.grid(column=9,row=2,padx=5)
        nav2_crs = Label(tab3,bd=4,width=3,relief="ridge",textvariable=self.crs_nav2)
        nav2_crs.grid(column=11,row=2)
        nav2_lab_crs = Label(tab3,text="Course")
        nav2_lab_crs.grid(column=12, row=2,padx=5)

        Label(tab3,text="Adf: ").grid(column=0,row=3,sticky='w')
        self.adf_pwr = Button(tab3,text="PWR",command=self.adf_but_pwr)
        self.adf_pwr.grid(column=2,row=3,padx=5)
        Label(tab3,text="Freq;").grid(column=3,row=3,padx=10)
        adf_freq_spin = Spinbox(tab3,from_=200, to=450,width=3,textvariable=self.adf_freq)
        adf_freq_spin.grid(column=4,row=3)
        self.adf_set = Button(tab3,text="SET",command=self.adf_but_set)
        self.adf_set.grid(column=5,row=3,padx=10)
        adf_dst = Label(tab3,bd=4,width=3,relief="ridge",textvariable = self.dst_adf)
        adf_dst.grid(column=7,row=3)
        Label(tab3,text="Nm Dst").grid(column=8,row=3)
        adf_crs = Label(tab3,bd=4,width=3,relief="ridge",textvariable = self.crs_adf)
        adf_crs.grid(column=11,row=3)
        Label(tab3,text="Course").grid(column=12,row=3,padx=5)

        





        tab.add(tab1,text="Systems")
        tab.add(tab2, text="Instruments")
        tab.add(tab3, text="Radios")

        
    def connect(self):
        print("connection)")
        self.but_connect.configure(bg="RED", state="disabled")
        if self.iocp.connect(self.adr_ip.get(), int(self.adr_port.get())) == -1:
            self.but_connect.configure(bg="RED", state="active")
            return
        self.but_connect.configure(bg="GREEN")
        self.dataDict = self.iocp.register(self.conf.getVar())
        print("Registered ",self.dataDict)
       
        
    def disconnect(self):
        print("disconnect")
        self.iocp.close()
        self.but_connect.configure(bg="WHITE", state="active")

    def run(self):

        self.fen.after(1000,self.update)
        self.fen.mainloop()


    def update(self):
        ''' update datas from server'''
        data = self.iocp.recvData()
        if data == -1:
            self.fen.after(1000,self.update)
            return
        for i in data.keys():
            self.dataDict[i] = data[i]
        
        
        if self.dataDict == -1:
            self.fen.after(1000,self.update)
            return
        
        
        print("From server: " + str(data))

        # colors channge for systems tab
        try:
            if self.dataDict["10"] == '1':
                self.bat_on.config(bg="GREEN")
                self.bat_off.config(bg="WHITE")
            else:
                self.bat_on.config(bg="WHITE")
                self.bat_off.config(bg="RED")

            if self.dataDict["11"] == '1':
                self.gen1_on.config(bg="GREEN")
                self.gen1_off.config(bg="WHITE")
            else:
                self.gen1_on.config(bg="WHITE")
                self.gen1_off.config(bg="RED")

            if self.dataDict["12"] == '1':
                self.gen2_on.config(bg="GREEN")
                self.gen2_off.config(bg="WHITE")
            else:
                self.gen2_on.config(bg="WHITE")
                self.gen2_off.config(bg="RED")

            if self.dataDict["13"] == '1':
                self.inv1_on.config(bg="GREEN")
                self.inv1_off.config(bg="WHITE")
            else:
                self.inv1_on.config(bg="WHITE")
                self.inv1_off.config(bg="RED")

            if self.dataDict["14"] == '1':
                self.inv2_on.config(bg="GREEN")
                self.inv2_off.config(bg="WHITE")
            else:
                self.inv2_on.config(bg="WHITE")
                self.inv2_off.config(bg="RED")
            
            if self.dataDict["15"] == '1':
                self.hud_on.config(bg="GREEN")
                self.hud_off.config(bg="WHITE")
            else:
                self.hud_on.config(bg="WHITE")
                self.hud_off.config(bg="RED")
                
            if self.dataDict["17"] == '1':
                self.pitot_on.config(bg="GREEN")
                self.pitot_off.config(bg="WHITE")
            else:
                self.pitot_on.config(bg="WHITE")
                self.pitot_off.config(bg="RED")

            if self.dataDict["118"] == '1':
                self.hydrau_on.config(bg="GREEN")
                self.hydrau_off.config(bg="WHITE")
            else:
                self.hud_on.config(bg="WHITE")
                self.hud_off.config(bg="RED")

            # instruments
            self.alti.set(str(int(int(self.dataDict["510"])/10000)))
            self.speed.set(str(int(int(self.dataDict["500"])/10000)))



            # radios
            #self.nav1_dec.set(self.dataDict["602"])
            #self.nav1_inc.set(self.dataDict["603"])
            #self.nav2_dec.set(self.dataDict["604"])
            #self.nav2_inc.set(self.dataDict["605"])
            self.crs_nav1.set(str(int(int(self.dataDict["608"])/10000)))
            self.crs_nav2.set(str(int(int(self.dataDict["609"])/10000)))
            self.crs_adf.set(str(int(int(self.dataDict["612"])/10000)))
            self.dst_adf.set(str(int(int(self.dataDict["613"])/10000)))
            if self.dataDict["600"] == '1':
                self.nav1_pwr.config(bg="GREEN")
            else:
                self.nav1_pwr.config(bg="WHITE")

            if self.dataDict["601"] == '1':
                self.nav2_pwr.config(bg="GREEN")
            else:
                self.nav2_pwr.config(bg="WHITE")

            if self.dataDict["610"] == "1":
                self.adf_pwr.config(bg="GREEN")
            else:
                self.adf_pwr.config(bg="WHITE")
        except:
            print("problem with a var, is it declared in both side ?")


        self.fen.after(1000,self.update)


    # buttons fonction for tab 1
    def but_on_fn(self):
        print("######## send 1")
        self.iocp.sendData("10","1")
        return

    def but_off_fn(self):
        print("######## send 2")
        self.iocp.sendData("10","0")
        return

    def gen1_on_but(self):
        print("gen1 on")
        self.iocp.sendData("11","1")

    def gen1_off_but(self):
        print("gen1 off")
        self.iocp.sendData("11","0")

    def gen2_on_but(self):
        print("gen2 on")
        self.iocp.sendData("12","1")

    def gen2_off_but(self):
        print("gen2 off")
        self.iocp.sendData("12","0")

    def inv1_on_but(self):
        print("inv1 on")
        self.iocp.sendData("13","1")

    def inv1_off_but(self):
        print("inv1 off")
        self.iocp.sendData("13","0")

    def inv2_on_but(self):
        print("inv2 on")
        self.iocp.sendData("14","1")

    def inv2_off_but(self):
        print("inv2 off")
        self.iocp.sendData("14","0")
    
    def hud_on_but(self):
        print("hud on")
        self.iocp.sendData("15","1")

    def hud_off_but(self):
        print("hud off")
        self.iocp.sendData("15","0")

    def pitot_on_but(self):
        print("pitot on")
        self.iocp.sendData("17","1")

    def pitot_off_but(self):
        print("pitot off")
        self.iocp.sendData("17","0")

    def hydrau_on_but(self):
        print("hydrau on")
        self.iocp.sendData("118","1")

    def hydrau_off_but(self):
        print("hydrau off")
        self.iocp.sendData("118","0")


    # buttons fonctuon for tab 3 radios
    def nav1_but_pwr(self):
        print("nav1 pwr")
        try:
            if self.dataDict["600"] == "1":
                self.iocp.sendData("600","0")
            else:
                self.iocp.sendData("600","1")
        except:
            print("Unable to send nav1 pwr")
            

    def nav1_but_set(self):
        print("freq set")
        self.iocp.sendData("602",self.nav1_dec.get())
        self.iocp.sendData("603",self.nav1_inc.get())

    def nav1_but_obs(self):
        print("obs set")
        self.iocp.sendData("606",str(int(self.obs_nav1.get())*10000))

    def nav2_but_pwr(self):
        print("nav2 pwr")

        try:
            if self.dataDict["601"] == "1":
                self.iocp.sendData("601","0")
            else:
                self.iocp.sendData("601","1")
        except:
            print("Unable to send nav2 pwr")

    def nav2_but_set(self):
        print("freq set")
        self.iocp.sendData("603",self.nav2_dec.get())
        self.iocp.sendData("603",self.nav2_inc.get())

    def nav2_but_obs(self):
        print("obs set")
        self.iocp.sendData("607",str(int(self.obs_nav2.get())*10000))

    def adf_but_pwr(self):
        print("Adf pwr")
        try:
            if self.dataDict["610"] == "2":
                self.iocp.sendData("610","0")
            else:
                self.iocp.sendData("610","2")
        except:
            pass

    def adf_but_set(self):
        print("adf freq set !")
        self.iocp.sendData("611",self.adf_freq.get())










def main():
    print("hello world")
    app = Fenetre()
    app.run()






if __name__ ==  "__main__":
    main()