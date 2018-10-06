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

        # Constant parameters so I don't have to manually change everything
        label_row = 1
        boost_row = 6
        setback_row = 7
        ability_row = 5
        difficulty_row = 8
        proficiency_row = 4
        challenge_row = 9
        result_row = 2
        separator_row = 3

        decrement_column = 2
        increment_column = 4
        amount_column = 3
        dice_name_column = 1
        dice_symbol_separator1 = 5
        dice_symbol_column = 6
        dice_symbol_separator2 = 7
        final_result_column = 0
        final_result_image_column = 0
        despair_column = 8
        despair_separator = 9
        failure_column = 10
        failure_separator = 11
        threat_column = 12
        threat_separator = 13
        advantage_column = 14
        advantage_separator = 15
        success_column = 16
        success_separator = 17
        triumph_column = 18
        triumph_separator = 19


        progbar_row = 1
        progbar_column = 1

        roll_row = 1
        roll_column = 3

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

        self.boost_file = ImageTk.PhotoImage(Image.open('data/genesys/boost.png'))
        self.ability_file = ImageTk.PhotoImage(Image.open('data/genesys/ability.png'))
        self.proficiency_file = ImageTk.PhotoImage(Image.open('data/genesys/proficiency.png'))
        self.setback_file = ImageTk.PhotoImage(Image.open('data/genesys/setback.png'))
        self.difficulty_file = ImageTk.PhotoImage(Image.open('data/genesys/difficulty.png'))
        self.challenge_file = ImageTk.PhotoImage(Image.open('data/genesys/challenge.png'))

        self.proficiency_dice_advantage = tk.IntVar()
        self.proficiency_dice_advantage.set(0)
        self.proficiency_dice_success = tk.IntVar()
        self.proficiency_dice_success.set(0)
        self.proficiency_dice_triumph = tk.IntVar()
        self.proficiency_dice_triumph.set(0)
        self.ability_dice_advantage = tk.IntVar()
        self.ability_dice_advantage.set(0)
        self.ability_dice_success = tk.IntVar()
        self.ability_dice_success.set(0)
        self.boost_dice_advantage = tk.IntVar()
        self.boost_dice_advantage.set(0)
        self.boost_dice_success = tk.IntVar()
        self.boost_dice_success.set(0)
        self.setback_dice_threat = tk.IntVar()
        self.setback_dice_threat.set(0)
        self.setback_dice_failure = tk.IntVar()
        self.setback_dice_failure.set(0)
        self.difficulty_dice_threat = tk.IntVar()
        self.difficulty_dice_threat.set(0)
        self.difficulty_dice_failure = tk.IntVar()
        self.difficulty_dice_failure.set(0)
        self.challenge_dice_threat = tk.IntVar()
        self.challenge_dice_threat.set(0)
        self.challenge_dice_failure = tk.IntVar()
        self.challenge_dice_failure.set(0)
        self.challenge_dice_despair = tk.IntVar()
        self.challenge_dice_despair.set(0)

        # Load the labels for the dice
        self.blabel = tk.Label(self, text='    BOOST    ').grid(column=dice_name_column, row=boost_row)
        self.slabel = tk.Label(self, text='    SETBACK    ').grid(column=dice_name_column, row=setback_row)
        self.alabel = tk.Label(self, text='    ABILITY    ').grid(column=dice_name_column, row=ability_row)
        self.dlabel = tk.Label(self, text='    DIFFICULTY    ').grid(column=dice_name_column, row=difficulty_row)
        self.plabel = tk.Label(self, text='    PROFICIENCY    ').grid(column=dice_name_column, row=proficiency_row)
        self.clabel = tk.Label(self, text='    CHALLENGE    ').grid(column=dice_name_column, row=challenge_row)

        self.bdice_entry = tk.Label(self, textvariable=self.bdice)
        self.bdice_entry.grid(column=amount_column, row=boost_row)
        self.sdice_entry = tk.Label(self, textvariable=self.sdice)
        self.sdice_entry.grid(column=amount_column, row=setback_row)
        self.adice_entry = tk.Label(self, textvariable=self.adice)
        self.adice_entry.grid(column=amount_column, row=ability_row)
        self.ddice_entry = tk.Label(self, textvariable=self.ddice)
        self.ddice_entry.grid(column=amount_column, row=difficulty_row)
        self.pdice_entry = tk.Label(self, textvariable=self.pdice)
        self.pdice_entry.grid(column=amount_column, row=proficiency_row)
        self.cdice_entry = tk.Label(self, textvariable=self.cdice)
        self.cdice_entry.grid(column=amount_column, row=challenge_row)

        # Load the labels for the results, dice symbols and tracker bar
        self.triumph_label = tk.Label(self,textvariable=self.triumph_result).grid(column=triumph_column, row=result_row)
        self.success_label = tk.Label(self,textvariable=self.success_result).grid(column=success_column, row=result_row)
        self.advantage_label = tk.Label(self,textvariable=self.advantage_result).grid(column=advantage_column, row=result_row)
        self.threat_label = tk.Label(self,textvariable=self.threat_result).grid(column=threat_column, row=result_row)
        self.failure_label = tk.Label(self,textvariable=self.failure_result).grid(column=failure_column, row=result_row)
        self.despair_label = tk.Label(self,textvariable=self.despair_result).grid(column=despair_column, row=result_row)
        self.progressbar = ttk.Progressbar(self, length=100)
        self.progressbar.grid(column=progbar_column, row=progbar_row, rowspan=2)

        self.triumph_image = tk.Label(self, image=self.triumph_file).grid(column=triumph_column, row=label_row)
        self.success_image = tk.Label(self, image=self.success_file).grid(column=success_column, row=label_row)
        self.advantage_image = tk.Label(self, image=self.advantage_file).grid(column=advantage_column, row=label_row)
        self.threat_image = tk.Label(self, image=self.threat_file).grid(column=threat_column, row=label_row)
        self.failure_image = tk.Label(self, image=self.failure_file).grid(column=failure_column, row=label_row)
        self.despair_image = tk.Label(self, image=self.despair_file).grid(column=despair_column, row=label_row)

        self.boost_image = tk.Label(self, image=self.boost_file).grid(column=dice_symbol_column, row=boost_row)
        self.ability_image = tk.Label(self, image=self.ability_file).grid(column=dice_symbol_column, row=ability_row)
        self.proficiency_image = tk.Label(self, image=self.proficiency_file).grid(column=dice_symbol_column, row=proficiency_row)
        self.setback_image = tk.Label(self, image=self.setback_file).grid(column=dice_symbol_column, row=setback_row)
        self.difficulty_image = tk.Label(self, image=self.difficulty_file).grid(column=dice_symbol_column, row=difficulty_row)
        self.challenge_image = tk.Label(self, image=self.challenge_file).grid(column=dice_symbol_column, row=challenge_row)

        self.ui_label(proficiency_row, advantage_column, self.proficiency_dice_advantage, True)
        self.ui_label(proficiency_row, success_column, self.proficiency_dice_success, True)
        self.ui_label(proficiency_row, triumph_column, self.proficiency_dice_triumph, True)
        self.ui_label(ability_row, advantage_column, self.ability_dice_advantage, True)
        self.ui_label(ability_row, success_column, self.ability_dice_success, True)
        self.ui_label(boost_row, advantage_column, self.boost_dice_advantage, True)
        self.ui_label(boost_row, success_column, self.boost_dice_success, True)
        self.ui_label(setback_row, threat_column, self.setback_dice_threat, True)
        self.ui_label(setback_row, failure_column, self.setback_dice_failure, True)
        self.ui_label(difficulty_row, threat_column, self.difficulty_dice_threat, True)
        self.ui_label(difficulty_row, failure_column, self.difficulty_dice_failure, True)
        self.ui_label(challenge_row, threat_column, self.challenge_dice_threat, True)
        self.ui_label(challenge_row, failure_column, self.challenge_dice_failure, True)
        self.ui_label(challenge_row, despair_column, self.challenge_dice_despair, True)

        # Separators to make it easier to see
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=1, row=separator_row, columnspan=20, sticky='we')
        ttk.Separator(self, orient=tk.VERTICAL).grid(column=dice_symbol_separator1, row=1, rowspan=10, sticky='ns')
        ttk.Separator(self, orient=tk.VERTICAL).grid(column=dice_symbol_separator2, row=1, rowspan=10, sticky='ns')
        ttk.Separator(self, orient=tk.VERTICAL).grid(column=despair_separator, row=1, rowspan=10, sticky='ns')
        ttk.Separator(self, orient=tk.VERTICAL).grid(column=failure_separator, row=1, rowspan=10, sticky='ns')
        ttk.Separator(self, orient=tk.VERTICAL).grid(column=threat_separator, row=1, rowspan=10, sticky='ns')
        ttk.Separator(self, orient=tk.VERTICAL).grid(column=advantage_separator, row=1, rowspan=10, sticky='ns')
        ttk.Separator(self, orient=tk.VERTICAL).grid(column=success_separator, row=1, rowspan=10, sticky='ns')
        ttk.Separator(self, orient=tk.VERTICAL).grid(column=triumph_separator, row=1, rowspan=10, sticky='ns')

        # Bind the buttons to keys
        self.parent.bind('x', self.bdice_add)
        self.parent.bind('z', self.bdice_dec)

        self.parent.bind('r', self.sdice_add)
        self.parent.bind('e', self.sdice_dec)

        self.parent.bind('s', self.adice_add)
        self.parent.bind('a', self.adice_dec)

        self.parent.bind('f', self.ddice_add)
        self.parent.bind('d', self.ddice_dec)

        self.parent.bind('w', self.pdice_add)
        self.parent.bind('q', self.pdice_dec)

        self.parent.bind('v', self.cdice_add)
        self.parent.bind('c', self.cdice_dec)

        self.parent.bind('<BackSpace>', self.reset_pool)
        self.parent.bind('<space>', self.roll)

        self.bbutton_less = tk.Button(self, text='-', command=self.bdice_dec).grid(column=decrement_column, row=boost_row)
        self.bbutton_more = tk.Button(self, text='+', command=self.bdice_add).grid(column=increment_column, row=boost_row)
        self.sbutton_less = tk.Button(self, text='-', command=self.sdice_dec).grid(column=decrement_column, row=setback_row)
        self.sbutton_more = tk.Button(self, text='+', command=self.sdice_add).grid(column=increment_column, row=setback_row)
        self.abutton_less = tk.Button(self, text='-', command=self.adice_dec).grid(column=decrement_column, row=ability_row)
        self.abutton_more = tk.Button(self, text='+', command=self.adice_add).grid(column=increment_column, row=ability_row)
        self.dbutton_less = tk.Button(self, text='-', command=self.ddice_dec).grid(column=decrement_column, row=difficulty_row)
        self.dbutton_more = tk.Button(self, text='+', command=self.ddice_add).grid(column=increment_column, row=difficulty_row)
        self.pbutton_less = tk.Button(self, text='-', command=self.pdice_dec).grid(column=decrement_column, row=proficiency_row)
        self.pbutton_more = tk.Button(self, text='+', command=self.pdice_add).grid(column=increment_column, row=proficiency_row)
        self.cbutton_less = tk.Button(self, text='-', command=self.cdice_dec).grid(column=decrement_column, row=challenge_row)
        self.cbutton_more = tk.Button(self, text='+', command=self.cdice_add).grid(column=increment_column, row=challenge_row)
        self.rollbtn = tk.Button(self, text='Roll', command=self.roll).grid(column=roll_column, row=roll_row, rowspan=2)

    def roll(self, event=None):
        self.dicePool[0] = self.bdice.get()
        self.dicePool[1] = self.sdice.get()
        self.dicePool[2] = self.adice.get()
        self.dicePool[3] = self.ddice.get()
        self.dicePool[4] = self.pdice.get()
        self.dicePool[5] = self.cdice.get()
        self.Genesys.roll_dice(self.dicePool)

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
        if(self.Genesys.net_success > 0):
            self.success_result.set(self.Genesys.success)
        elif(self.Genesys.net_success < 0):
            self.failure_result.set(-self.Genesys.net_success)
        if(self.Genesys.net_advantage > 0):
            self.advantage_result.set(self.Genesys.net_advantage)
        elif(self.Genesys.net_advantage < 0):
            self.threat_result.set(-self.Genesys.net_advantage)

        self.show_pool_results()

        self.bar_progress()

    def reset_pool(self, event=None):
        self.bdice.set(0)
        self.sdice.set(0)
        self.adice.set(0)
        self.ddice.set(0)
        self.pdice.set(0)
        self.cdice.set(0)

    def show_pool_results(self):
        self.proficiency_dice_triumph.set(self.Genesys.proficiency_dice.triumph)
        self.proficiency_dice_success.set(self.Genesys.proficiency_dice.success)
        self.proficiency_dice_advantage.set(self.Genesys.proficiency_dice.advantage)
        self.ability_dice_success.set(self.Genesys.ability_dice.success)
        self.ability_dice_advantage.set(self.Genesys.ability_dice.advantage)
        self.boost_dice_success.set(self.Genesys.boost_dice.success)
        self.boost_dice_advantage.set(self.Genesys.boost_dice.advantage)
        self.setback_dice_failure.set(self.Genesys.setback_dice.failure)
        self.setback_dice_threat.set(self.Genesys.setback_dice.threat)
        self.difficulty_dice_failure.set(self.Genesys.difficulty_dice.failure)
        self.difficulty_dice_threat.set(self.Genesys.difficulty_dice.threat)
        self.challenge_dice_failure.set(self.Genesys.challenge_dice.failure)
        self.challenge_dice_threat.set(self.Genesys.challenge_dice.threat)
        self.challenge_dice_despair.set(self.Genesys.challenge_dice.despair)

    def bar_progress(self, event=None):
        self.progressbar.step(50)

    def ui_label(self, row, column, text, textvariable=False):
        if textvariable == False:
            tk.Label(self, text=text).grid(column=column, row=row)
        else:
            tk.Label(self, textvariable=text).grid(column=column, row=row)

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
