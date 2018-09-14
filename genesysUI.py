from genesys import GenesysDiceRoller
import tkinter as tk
from tkinter import ttk

class GenesysUI(tk.Frame):
    def __init__(self, parent=None):
        self.dicePool = [0, 0, 0, 0, 0, 0]
        self.Genesys = GenesysDiceRoller()
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.parent = parent

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
        self.result = tk.StringVar()

        self.blabel = tk.Label(self, text='Boost').grid(column=1, row=1)
        self.slabel = tk.Label(self, text='Setback').grid(column=1, row=2)
        self.alabel = tk.Label(self, text='Ability').grid(column=1, row=3)
        self.dlabel = tk.Label(self, text='Difficulty').grid(column=1, row=4)
        self.plabel = tk.Label(self, text='Proficiency').grid(column=1, row=5)
        self.clabel = tk.Label(self, text='Challenge').grid(column=1, row=6)

        self.bdice_entry = tk.Label(self, textvariable=self.bdice)
        self.bdice_entry.grid(column=3, row=1)
        self.sdice_entry = tk.Label(self, textvariable=self.sdice)
        self.sdice_entry.grid(column=3, row=2)
        self.adice_entry = tk.Label(self, textvariable=self.adice)
        self.adice_entry.grid(column=3, row=3)
        self.ddice_entry = tk.Label(self, textvariable=self.ddice)
        self.ddice_entry.grid(column=3, row=4)
        self.pdice_entry = tk.Label(self, textvariable=self.pdice)
        self.pdice_entry.grid(column=3, row=5)
        self.cdice_entry = tk.Label(self, textvariable=self.cdice)
        self.cdice_entry.grid(column=3, row=6)

        self.resultlabel = tk.Label(self, textvariable=self.result).grid(column=1, row=8)

        self.parent.bind('q', self.bdice_add)
        self.parent.bind('a', self.bdice_dec)

        self.parent.bind('w', self.sdice_add)
        self.parent.bind('s', self.sdice_dec)

        self.parent.bind('e', self.adice_add)
        self.parent.bind('d', self.adice_dec)

        self.parent.bind('r', self.ddice_add)
        self.parent.bind('f', self.ddice_dec)

        self.parent.bind('x', self.pdice_add)
        self.parent.bind('z', self.pdice_dec)

        self.parent.bind('v', self.cdice_add)
        self.parent.bind('c', self.cdice_dec)

        self.parent.bind('<BackSpace>', self.reset_pool)
        self.parent.bind('<space>', self.roll)

        self.bbutton_less = tk.Button(self, text='-', command=self.bdice_dec).grid(column=2, row=1)
        self.bbutton_more = tk.Button(self, text='+', command=self.bdice_add).grid(column=4, row=1)
        self.sbutton_less = tk.Button(self, text='-', command=self.sdice_dec).grid(column=2, row=2)
        self.sbutton_more = tk.Button(self, text='+', command=self.sdice_add).grid(column=4, row=2)
        self.abutton_less = tk.Button(self, text='-', command=self.adice_dec).grid(column=2, row=3)
        self.abutton_more = tk.Button(self, text='+', command=self.adice_add).grid(column=4, row=3)
        self.dbutton_less = tk.Button(self, text='-', command=self.ddice_dec).grid(column=2, row=4)
        self.dbutton_more = tk.Button(self, text='+', command=self.ddice_add).grid(column=4, row=4)
        self.pbutton_less = tk.Button(self, text='-', command=self.pdice_dec).grid(column=2, row=5)
        self.pbutton_more = tk.Button(self, text='+', command=self.pdice_add).grid(column=4, row=5)
        self.cbutton_less = tk.Button(self, text='-', command=self.cdice_dec).grid(column=2, row=6)
        self.cbutton_more = tk.Button(self, text='+', command=self.cdice_add).grid(column=4, row=6)
        self.rollbtn = tk.Button(self, text='Roll', command=self.roll).grid(column=4, row=7)

    def roll(self, event=None):
        self.dicePool[0] = self.bdice.get()
        self.dicePool[1] = self.sdice.get()
        self.dicePool[2] = self.adice.get()
        self.dicePool[3] = self.ddice.get()
        self.dicePool[4] = self.pdice.get()
        self.dicePool[5] = self.cdice.get()
        self.Genesys.rollDice(self.dicePool)

        result = ''
        if(self.Genesys.triumph > 0):
            result += '{0}TP, '.format(self.Genesys.triumph)
        if(self.Genesys.despair > 0):
            result += '{0}DR, '.format(self.Genesys.despair)
        if(self.Genesys.netSuccess > 0):
            result += '{0}X, '.format(self.Genesys.netSuccess)
        elif(self.Genesys.netSuccess < 0):
            result += '{0}F, '.format(-self.Genesys.netSuccess)
        if(self.Genesys.netAdvantage > 0):
            result += '{0}A'.format(self.Genesys.netAdvantage)
        elif(self.Genesys.netAdvantage < 0):
            result += '{0}T'.format(-self.Genesys.netAdvantage)

        if(result == ''):
            result += 'None.'
        self.result.set(result)

    def reset_pool(self, event=None):
        self.bdice.set(0)
        self.sdice.set(0)
        self.adice.set(0)
        self.ddice.set(0)
        self.pdice.set(0)
        self.cdice.set(0)

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
