from genesys import GenesysDiceRoller
import tkinter as tk
from tkinter import ttk
from random import randint
from PIL import ImageTk, Image

class GenesysUI(tk.Frame):
    def __init__(self, parent=None):
        self.dicePool = [0, 0, 0, 0, 0, 0]
        self.Genesys = GenesysDiceRoller()
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.parent = parent

        # Load all variables
        self.bdice = tk.IntVar()
        self.bdice.set(0)
        self.sdice = tk.IntVar()
        self.sdice.set(0)
        self.adice = tk.IntVar()
        self.adice.set(0)
        self.ddice = tk.IntVar()
        self.ddice.set(0)
        self.pdice = tk.IntVar()
        self.pdice.set(0)
        self.cdice = tk.IntVar()
        self.cdice.set(0)
        self.triumph_result = tk.IntVar()
        self.triumph_result.set(0)
        self.success_result = tk.IntVar()
        self.success_result.set(0)
        self.advantage_result = tk.IntVar()
        self.advantage_result.set(0)
        self.threat_result = tk.IntVar()
        self.threat_result.set(0)
        self.failure_result = tk.IntVar()
        self.failure_result.set(0)
        self.despair_result = tk.IntVar()
        self.despair_result.set(0)
        self.triumph_file = ImageTk.PhotoImage(Image.open('data/genesys/triumph.png'))
        self.success_file = ImageTk.PhotoImage(Image.open('data/genesys/success.png'))
        self.advantage_file = ImageTk.PhotoImage(Image.open('data/genesys/advantage.png'))
        self.threat_file = ImageTk.PhotoImage(Image.open('data/genesys/threat.png'))
        self.failure_file = ImageTk.PhotoImage(Image.open('data/genesys/failure.png'))
        self.despair_file = ImageTk.PhotoImage(Image.open('data/genesys/despair.png'))

        # Load the labels for the dice
        self.blabel = tk.Label(self, text='    BOOST    ').grid(column=3, row=1)
        self.slabel = tk.Label(self, text='    SETBACK    ').grid(column=3, row=2)
        self.alabel = tk.Label(self, text='    ABILITY    ').grid(column=3, row=3)
        self.dlabel = tk.Label(self, text='    DIFFICULTY    ').grid(column=3, row=4)
        self.plabel = tk.Label(self, text='    PROFICIENCY    ').grid(column=3, row=5)
        self.clabel = tk.Label(self, text='    CHALLENGE    ').grid(column=3, row=6)

        self.bdice_entry = tk.Label(self, textvariable=self.bdice)
        self.bdice_entry.grid(column=5, row=1)
        self.sdice_entry = tk.Label(self, textvariable=self.sdice)
        self.sdice_entry.grid(column=5, row=2)
        self.adice_entry = tk.Label(self, textvariable=self.adice)
        self.adice_entry.grid(column=5, row=3)
        self.ddice_entry = tk.Label(self, textvariable=self.ddice)
        self.ddice_entry.grid(column=5, row=4)
        self.pdice_entry = tk.Label(self, textvariable=self.pdice)
        self.pdice_entry.grid(column=5, row=5)
        self.cdice_entry = tk.Label(self, textvariable=self.cdice)
        self.cdice_entry.grid(column=5, row=6)

        # Load the labels for the results, dice symbols and tracker bar
        self.triumph_label = tk.Label(self,textvariable=self.triumph_result).grid(column=2, row=1)
        self.success_label = tk.Label(self,textvariable=self.success_result).grid(column=2, row=2)
        self.advantage_label = tk.Label(self,textvariable=self.advantage_result).grid(column=2, row=3)
        self.threat_label = tk.Label(self,textvariable=self.threat_result).grid(column=2, row=4)
        self.failure_label = tk.Label(self,textvariable=self.failure_result).grid(column=2, row=5)
        self.despair_label = tk.Label(self,textvariable=self.despair_result).grid(column=2, row=6)
        self.progressbar = ttk.Progressbar(self, length=50)
        self.progressbar.grid(column=3, row=8)

        self.triumph_image = tk.Label(self, image=self.triumph_file).grid(column=1, row=1)
        self.success_image = tk.Label(self, image=self.success_file).grid(column=1, row=2)
        self.advantage_image = tk.Label(self, image=self.advantage_file).grid(column=1, row=3)
        self.threat_image = tk.Label(self, image=self.threat_file).grid(column=1, row=4)
        self.failure_image = tk.Label(self, image=self.failure_file).grid(column=1, row=5)
        self.despair_image = tk.Label(self, image=self.despair_file).grid(column=1, row=6)

        # Bind the buttons to keys
        self.parent.bind('x', self.bdice_add)
        self.parent.bind('z', self.bdice_dec)

        self.parent.bind('v', self.sdice_add)
        self.parent.bind('c', self.sdice_dec)

        self.parent.bind('s', self.adice_add)
        self.parent.bind('a', self.adice_dec)

        self.parent.bind('f', self.ddice_add)
        self.parent.bind('d', self.ddice_dec)

        self.parent.bind('w', self.pdice_add)
        self.parent.bind('q', self.pdice_dec)

        self.parent.bind('r', self.cdice_add)
        self.parent.bind('e', self.cdice_dec)

        self.parent.bind('<BackSpace>', self.reset_pool)
        self.parent.bind('<space>', self.roll)

        self.bbutton_less = tk.Button(self, text='-', command=self.bdice_dec).grid(column=4, row=1)
        self.bbutton_more = tk.Button(self, text='+', command=self.bdice_add).grid(column=6, row=1)
        self.sbutton_less = tk.Button(self, text='-', command=self.sdice_dec).grid(column=4, row=2)
        self.sbutton_more = tk.Button(self, text='+', command=self.sdice_add).grid(column=6, row=2)
        self.abutton_less = tk.Button(self, text='-', command=self.adice_dec).grid(column=4, row=3)
        self.abutton_more = tk.Button(self, text='+', command=self.adice_add).grid(column=6, row=3)
        self.dbutton_less = tk.Button(self, text='-', command=self.ddice_dec).grid(column=4, row=4)
        self.dbutton_more = tk.Button(self, text='+', command=self.ddice_add).grid(column=6, row=4)
        self.pbutton_less = tk.Button(self, text='-', command=self.pdice_dec).grid(column=4, row=5)
        self.pbutton_more = tk.Button(self, text='+', command=self.pdice_add).grid(column=6, row=5)
        self.cbutton_less = tk.Button(self, text='-', command=self.cdice_dec).grid(column=4, row=6)
        self.cbutton_more = tk.Button(self, text='+', command=self.cdice_add).grid(column=6, row=6)
        self.rollbtn = tk.Button(self, text='Roll', command=self.roll).grid(column=6, row=8)

    def roll(self, event=None):
        self.dicePool[0] = self.bdice.get()
        self.dicePool[1] = self.sdice.get()
        self.dicePool[2] = self.adice.get()
        self.dicePool[3] = self.ddice.get()
        self.dicePool[4] = self.pdice.get()
        self.dicePool[5] = self.cdice.get()
        self.Genesys.rollDice(self.dicePool)

        self.triumph_result.set(0)
        self.success_result.set(0)
        self.advantage_result.set(0)
        self.threat_result.set(0)
        self.failure_result.set(0)
        self.despair_result.set(0)

        if(self.Genesys.triumph > 0):
            self.triumph_result.set(self.Genesys.triumph)
        if(self.Genesys.despair > 0):
            self.despair_result.set(self.Genesys.despair)
        if(self.Genesys.netSuccess > 0):
            self.success_result.set(self.Genesys.success)
        elif(self.Genesys.netSuccess < 0):
            self.failure_result.set(-self.Genesys.netSuccess)
        if(self.Genesys.netAdvantage > 0):
            self.advantage_result.set(self.Genesys.netAdvantage)
        elif(self.Genesys.netAdvantage < 0):
            self.threat_result.set(-self.Genesys.netAdvantage)

        self.bar_progress()

    def reset_pool(self, event=None):
        self.bdice.set(0)
        self.sdice.set(0)
        self.adice.set(0)
        self.ddice.set(0)
        self.pdice.set(0)
        self.cdice.set(0)

    def bar_progress(self, event=None):
        self.progressbar.step(50)

    def bdice_add(self, event=None):
        result = self.bdice.get() + 1
        self.bdice.set(result)

    def bdice_dec(self, event=None):
        if(self.bdice.get() > 0):
            result = self.bdice.get() - 1
            self.bdice.set(result)

    def sdice_add(self, event=None):
        result = self.sdice.get() + 1
        self.sdice.set(result)

    def sdice_dec(self, event=None):
        if(self.sdice.get() > 0):
            result = self.sdice.get() - 1
            self.sdice.set(result)

    def adice_add(self, event=None):
        result = self.adice.get() + 1
        self.adice.set(result)

    def adice_dec(self, event=None):
        if(self.adice.get() > 0):
            result = self.adice.get() - 1
            self.adice.set(result)

    def ddice_add(self, event=None):
        result = self.ddice.get() + 1
        self.ddice.set(result)

    def ddice_dec(self, event=None):
        if(self.ddice.get() > 0):
            result = self.ddice.get() - 1
            self.ddice.set(result)

    def pdice_add(self, event=None):
        result = self.pdice.get() + 1
        self.pdice.set(result)

    def pdice_dec(self, event=None):
        if(self.pdice.get() > 0):
            result = self.pdice.get() - 1
            self.pdice.set(result)

    def cdice_add(self, event=None):
        result = self.cdice.get() + 1
        self.cdice.set(result)

    def cdice_dec(self, event=None):
        if(self.cdice.get() > 0):
            result = self.cdice.get() - 1
            self.cdice.set(result)



if __name__ == "__main__":
    root = tk.Tk()
    root.title('Genesys Dice Roller')
    GenesysUI(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
