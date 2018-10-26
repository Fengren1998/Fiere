import random as r
from termcolor import colored, cprint

with open('data/settlement_names.ni', 'r') as file:
    NAMES = file.readlines()
for i in NAMES:
    i = i.rstrip('\r\n')

class Mdict():
    def __init__(self):
        self.d = {}
    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)
    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]
    def get_suffix(self,prefix):
        l = self[prefix]
        return r.choice(l)

class MName():
    """
    A name from a Markov chain
    """
    def __init__(self, chainlen = 2):
        """
        Building the dictionary
        """
        if(chainlen > 10 or chainlen < 1):
            print ("Chain length must be between 1 and 10, inclusive")
            sys.exit(0)

        self.mcd = Mdict()
        oldnames = []
        self.chainlen = chainlen

        for l in NAMES:
            l = l.strip()
            oldnames.append(l)
            s = " " * chainlen + l
            for n in range(0,len(l)):
                self.mcd.add_key(s[n:n+chainlen], s[n+chainlen])
            self.mcd.add_key(s[len(l):len(l)+chainlen], "\n")

    def New(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 9:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()

class Cell():
    def __init__(self, upper, string1=None, string2=None, string3=None):
        self.upper = upper
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3

class EventCell():
    def __init__(self, upper, name, description):
        self.upper = upper
        self.name = name
        self.description = description

class TOADCell():
    def __init__(self, upper, description):
        self.upper = upper
        self.description = description

class Mythic():
    def __init__(self):
        self.events_table = [
            EventCell(7, 'Remote Event', 'Something important has happened that bears on the adventure, but the player characters were not present when the event occurred, they only learn about it remotely.'),
            EventCell(28, 'NPC Action', 'An existing non-player character makes a surprise action.'),
            EventCell(35, 'Introduce a New NPC', 'A brand new face is involved in the adventure.'),
            EventCell(45, 'Move Toward a Thread', 'Threads are the goals that player characters are going after.'),
            EventCell(52, 'Move Away from a Thread', 'This random event will make a thread harder.'),
            EventCell(55, 'Close a Thread', 'The random event is so important it actually closes an open thread.'),
            EventCell(67, 'PC Negative', 'Something bad happens to a player character, or non-player character. Interchangeable with NPC Negative.'),
            EventCell(75, 'PC Positive', 'Something good happens to a player character, or non-player character. Interchangeable with NPC Positive.'),
            EventCell(83, 'Ambiguous Event', 'All of the random events previously mentioned have a direct impact on the adventure and the player characters.'),
            EventCell(92, 'NPC Negative', 'Something bad happens to a player character, or non-player character. Interchangeable with PC Negative.'),
            EventCell(100, 'NPC Positive', 'Something good happens to a player character, or non-player character. Interchangeable with PC Positive.'),
        ]

        self.details_table = [
            Cell(4, colored('It induces anger.', 'cyan'), 'The answer is something that causes anger in the PC most directly involved with the Question. The degree of anger is up to you, whatever seems most appropriate, ranging from discovering that an ally is actually working for an enemy to being upset that the barrista failed to put whipped cream on your caramel macchiato.'),
            Cell(5, colored('It induces sadness.', 'cyan'), 'The answer is something that causes sadness in the Player Character most directly involved with the Question. As with anger and the other emotions, “sadness” can be interpreted widely, from the grief of discovering a dear friend has died to losing an object they wanted'),
            Cell(6, colored('It induces fear.', 'cyan'), 'The answer is something that causes fear in the PC most directly involved. This may be the most easily 12interpreted emotion in the table as many things can cause fear, from an opponent drawing their weapon and attacking to hearing a dread knocking sound in the dead of night.'),
            Cell(7, colored('It disfavors a thread.', 'cyan'), 'The answer to your Question will be the most obvious result that works against that Thread goal. The goal may become harder to achieve or there may be a delay of some sort. i.e. if the goal is to move to a location, then the character(s) may be attacked and end up running away and getting lost, delaying the journey.'),
            Cell(8, colored('It disfavors a player character.', 'cyan'), 'This Disfavors the character in the most obvious way. i.e. if the character is weak to fire then the object in question will have fire attacks/traps etc.'),
            Cell(9, colored('It focuses on an NPC.', 'cyan'), 'The answer to this Question centers around an NPC on the NPC List. If there is more than one then randomly determine which one. It doesn’t necessarily mean that anything directly happens to that NPC, or that the NPC is even directly involved in the answer to the Question, it just means that the answer has something to do with that NPC.'),
            Cell(10, colored('It favors an NPC.', 'cyan'), 'The answer to this Question pertains to a randomly determined NPC on the Character List in a favorable way. “Favors” can be something that directly aids that NPC to the result being alike to the NPC. i.e. "What does the demon coming at me look like?" can be answered with a demon that is easy to kill with a particular tool owned by the character or some form of knowledge that may help in killing the demon.'),
            Cell(11, colored('It focuses on a player character.', 'cyan'), 'The answer to this Question centers around a player character. If there is more than one then randomly determine which one. It doesn’t necessarily mean that anything directly happens to that character, or that the character is even directly involved in the answer to the Question, it just means that the answer has something to do with that character.'),
            Cell(12, colored('It disfavors an NPC', 'cyan'), 'This Disfavors the NPC in the most obvious way. i.e. if the character is weak to fire then the object in question will have fire attacks/traps etc.'),
            Cell(13, colored('It focuses on a thread.', 'cyan'), 'The answer to this Question centers around a thread on the thread List. If there is more than one then randomly determine which one. It doesn’t necessarily mean that anything directly happens to the thread, or that the thread is even directly involved in the answer to the Question, it just means that the answer has something to do with the thread. Since threads are the goals that the PCs are pursuing, the Focus Thread result will often be a piece of information about the thread or a reminder of the thread.'),
            Cell(14, colored('It favors a player character.', 'cyan'), 'The answer to this Question pertains to a player character in a favorable way. “Favors” can be something that directly aids that character to the result being alike to the character. i.e. "What does the demon coming at me look like?" can be answered with a demon that is easy to kill with a particular tool owned by the character or some form of knowledge that may help in killing the demon.'),
            Cell(15, colored('It favors a thread.', 'cyan'), 'The answer to this Question will likely result in the PCs taking a step closer to completing the Thread in question, if not give them the opportunity to achieve it right then. Or, it may simply have something in common with the Thread.'),
            Cell(16, colored('It induces courage.', 'cyan'), 'This is another emotion result, the flip side to Fear. As with the other emotions, this one pertains to the PC most directly related to the Question being asked. The result should be something that bolsters the PC’s courage, such as the sudden appearance of an ally army or the discovery of a useful weapon.'),
            Cell(17, colored('It induces happiness.', 'cyan'), 'The answer to this Detail Check makes the PC most directly related to the Question happy in some way. This is the opposite of the Sad result. As with the other emotions, Happiness can range widely from discovering that a friend thought dead is still alive to getting your hands on a beer after a long, tiring journey.'),
            Cell(18, colored('It induces calm.', 'cyan'), 'The answer to this Question makes the PC most directly involved with the Question calm in some way. This is the opposite of the Anger result. “Calm” can be anything that produces peace or lessens a currently tense situation. As with the other emotions, the affects can range widely. Maybe a storm that is rocking a ship they’re traveling in ends, or a monster they thought would attack stands down.'),
        ]

        self.statistic = [
            Cell(2, 'It is much weaker than expected. (-75%)'),
            Cell(4, 'It is weaker than expected. (-50%)'),
            Cell(6, 'It is slightly weaker than expected. (-10%)'),
            Cell(11, 'It is as strong as expected. (+0%)'),
            Cell(14, 'It is slightly stronger than expected. (+10%)'),
            Cell(16, 'It is stronger than expected. (+50%)'),
            Cell(18, 'It is much stronger than expected. (+100%)'),
            Cell(20, 'It is as strong as you. (+0%)'),
            Cell(22, 'It is slightly stronger compared to you. (+10%)'),
            Cell(24, 'It is stronger compared to you. (+50%)'),
            Cell(26, 'It is much stronger compared to you. (+100%)'),
        ]

        self.action_1 = []
        with open('data/action_1.ni', 'r') as file:
            content = file.readlines()
        for i in content:
            self.action_1.append(i.split(' ')[1].rstrip('\r\n'))

        self.action_2 = []
        with open('data/action_2.ni', 'r') as file:
            content = file.readlines()
        for i in content:
            self.action_2.append(i.split(' ')[1].rstrip('\r\n'))

        self.description_1 = []
        with open('data/description_1.ni', 'r') as file:
            content = file.readlines()
        for i in content:
            self.description_1.append(i.split(' ')[1].rstrip('\r\n'))

        self.description_2 = []
        with open('data/description_2.ni', 'r') as file:
            content = file.readlines()
        for i in content:
            self.description_2.append(i.split(' ')[1].rstrip('\r\n'))

        self.action = []
        with open('data/eventaction.ni', 'r') as file:
            content = file.readlines()
        for i in content:
            self.action.append(i.split(' ')[1].rstrip('\r\n'))

        self.subject = []
        with open('data/eventsubject.ni', 'r') as file:
            content = file.readlines()
        for i in content:
            product = ''
            temp = i.split(' ')
            temp.pop(0)
            for j in temp:
                product += j.rstrip('\r\n').capitalize() + ' '
            self.subject.append(product)

    def calculate(self, rank, chaos=None):
        roll1 = self.rollsim(1, 10)
        roll2 = self.rollsim(1, 10)
        total = roll1 + roll2

        # For exceptional results
        roll1 = self.rollsim(1, 10)
        roll2 = self.rollsim(1, 10)
        total2 = roll1 + roll2

        # For Chaos
        isChaos = False

        # Calculate the likelihood
        if(rank == 1):
            total -= 8
        elif(rank == 2):
            total -= 6
        elif(rank == 3):
            total -= 4
        elif(rank == 4):
            total -= 2
        elif(rank == 6):
            total += 2
        elif(rank == 7):
            total += 4
        elif(rank == 8):
            total += 6
        elif(rank == 9):
            total += 8

        # Add the Chaos Factor
        if(chaos is not None):
            if(chaos == '+'):
                total += 2
            elif(chaos == '-'):
                total -= 2
            isChaos = True

        # For exceptionals and events
        digits = str(total2)
        if(len(digits) > 1):
            digit1 = int(digits[0])
            digit2 = int(digits[1])

        # Return the answer
        if(total < 11):
            if(len(digits) > 1):
                if(isChaos == True):
                    if(digits[0] == digits[1]):
                        return 'Exceptionally no. Roll for an event or detail.'
                    elif(digit1 % 2 == 1 and digit2 % 2 == 1):
                        return 'Exceptionally no.'
                    elif(digit1 % 2 == 0 and digit2 % 2 == 0):
                        return 'No. Roll for an event or detail.'
            return 'No.'
        elif (total >= 11):
            if(len(digits) > 1):
                if(isChaos == True):
                    if(digits[0] == digits[1]):
                        return 'Exceptionally yes. Roll for an event or detail.'
                    elif(digit1 % 2 == 1 and digit2 % 2 == 1):
                        return 'Exceptionally yes.'
                    elif(digit1 % 2 == 0 and digit2 % 2 == 0):
                        return 'Yes. Roll for an event or detail.'
            return 'Yes.'

    def detail(self, chaos=None):
        roll = self.rollsim(2, 20)
        # Handle the chaos argument
        if(chaos is not None):
            if(chaos == '+'):
                roll += 2
            elif(chaos == '-'):
                roll -= 2

        # Iterate over the array then return
        for i in self.details_table:
            if(roll <= i.upper):
                return i.string1, i.string2
            elif(roll >= 18):
                return self.details_table[-1].string1, self.details_table[-1].string2
        return None

    def action_gen(self):
        result = ''
        result += self.action_1[r.randint(0, len(self.action_1) - 1)]
        result += ' '
        result += self.action_2[r.randint(0, len(self.action_2) - 1)]
        return result

    def description_gen(self):
        result = ''
        result += self.description_1[r.randint(0, len(self.description_1) - 1)]
        result += ' '
        result += self.description_2[r.randint(0, len(self.description_2) - 1)]
        return result

    def strength_determine(self, modifier=None, modifier2=None):
        roll = r.randint(2,20)

        # Handle the modifier argument
        if(modifier is not None):
            if(modifier == 'important'):
                roll += 2
            elif(modifier == 'weak'):
                roll -= 2
            elif(modifier == 'strong'):
                roll += 2
            elif(modifier == 'prime'):
                roll += 4

        if(modifier2 is not None):
            if(modifier2 == 'important'):
                roll += 2
            elif(modifier2 == 'weak'):
                roll -= 2
            elif(modifier2 == 'strong'):
                roll += 2
            elif(modifier2 == 'prime'):
                roll += 4

        # Iterate over the array then return
        for i in self.statistic:
            if(roll <= i.upper):
                return i.string1
            elif(roll >= 26):
                return self.statistic[-1].string1
        return None

    def generate(self):
        event = ''
        event_desc = ''
        roll = r.randint(1,100)
        for i in self.events_table:
            if(roll <= i.upper):
                event = i.name
                event_desc = i.description
                break

        meaning = ''
        roll = r.randint(1, 100)
        meaning += self.action[roll - 1] + ' '
        roll = r.randint(1, 100)
        meaning += self.subject[roll - 1]

        return event, event_desc, meaning

    def rollsim(self, lower, upper):
        roll = 0
        for x in range(lower + upper):
            roll = r.randint(lower, upper)

        return roll

class Dungeon():
    def __init__(self):
        self.dungeon_exotic = ['Among the branches of a tree', 'Around a geyser',
            'Behind a waterfall', 'Buried in an avalanche', 'Buried in a sandstorm',
            'Buried in volcanic ash', 'Structure sunken in a swamp', 'Structure at the bottom of a sinkhole',
            'Floating on the sea', 'In a meteorite', 'On a demiplane or in a pocket dimension',
            'In an area devastated by a magical catastrophe', 'On a cloud', 'In the feywild',
            'In the Shadowfell', 'On an island in an underground sea', 'In a volcano',
            'On the back of a gargantuan living creature', 'Sealed inside a magical dome of force',
        ]
        self.dungeon_location = [TOADCell(4, 'A building in a city'), TOADCell(8, 'Catacombs or sewers beneath a city'),
            TOADCell(12, 'Beneath a farmhouse'), TOADCell(16, 'Beneath a graveyard'),
            TOADCell(22, 'Beneath a ruined castle'), TOADCell(26, 'Beneath a ruined city'),
            TOADCell(30, 'Beneath a temple'), TOADCell(34, 'In a chasm'),
            TOADCell(38, 'In a cliff face'), TOADCell(42, 'In a desert'),
            TOADCell(46, 'In a forest'), TOADCell(50, 'In a glacier'),
            TOADCell(54, 'In a gorge'), TOADCell(58, 'In a jungle'),
            TOADCell(62, 'In a mountain pass'), TOADCell(66, 'In a swamp'),
            TOADCell(70, 'Beneath or on top of a mesa'), TOADCell(74, 'In sea caves'),
            TOADCell(78, 'In several connected mesas'), TOADCell(82, 'On a mountain peak'),
            TOADCell(86, 'On a promontory'), TOADCell(90, 'On an island'),
            TOADCell(95, 'Underwater'), TOADCell(100, self.exotic())
        ]
        self.dungeon_purpose = [
            TOADCell(1, '{}. This dungeon is built to eliminate any creature that dares to enter it. A death trap might guard the treasure of an insane wizard, or it might be designed to lure adventurers to their demise for some nefarious purpose, such as to feed souls to a lich\'s phylactery.'.format(colored('Death Trap', 'cyan'))),
            TOADCell(5, '{}. A lair is a place where monsters live. Typical lairs include ruins and caves.'.format(colored('Lair', 'cyan'))),
            TOADCell(6, '{}. A maze is intended to deceive or confuse those who enter it. Some mazes are elaborate obstacles that protect treasure, while others are gauntlets for prisoners banished there to be hunted and devoured by the monsters within.'.format(colored('Maze', 'cyan'))),
            TOADCell(9, '{}. An abandoned mine can quickly become infested with monsters, while miners who delve too deep can break through into the Underdark.'.format(colored('Mine', 'cyan'))),
            TOADCell(10, '{}. Dungeons built around planar portals are often transformed by the planar energy seeping out through those portals.'.format(colored('Planar Gate', 'cyan'))),
            TOADCell(14, '{}. A stronghold dungeon provides a secure base of operations for villains and monsters. It is usually ruled by a powerful individual, such as a wizard, vampire, or dragon, and it is larger and more complex than a simple lair.'.format(colored('Stronghold', 'cyan'))),
            TOADCell(17, '{}. This dungeon is consecrated to a deity or other planar entity. The entity\'s worshippers control the dungeon and conduct their rites there.'.format(colored('Temple or Shrine', 'cyan'))),
            TOADCell(19, '{}. Tombs are magnets for treasure hunters, as well as monsters that hunger for the bones of the dead.'.format(colored('Tomb', 'cyan'))),
            TOADCell(20, '{}. Built to protect powerful magic items and great material wealth, treasure vault dungeons are heavily guarded by monsters and traps.'.format(colored('Treasure Vault', 'cyan'))),
        ]

    def exotic(self):
        roll = r.randint(0, len(self.dungeon_exotic) - 1)
        result = self.dungeon_exotic[roll]
        return result

    def generate(self):
        location = ''
        purpose = ''

        roll = r.randint(1,100)
        for i in self.dungeon_location:
            if(roll <= i.upper):
                location = i.description
                break

        roll = r.randint(1,20)
        for i in self.dungeon_purpose:
            if(roll <= i.upper):
                purpose = i.description
                break

        return location, purpose

class Settlement():
    def __init__(self):
        self.ruler_status = []
        with open('data/settlement_ruler_status.ni', 'r') as file:
            content = file.readlines()
        for i in content:
            self.ruler_status.append(i.rstrip('\r\n'))

        self.traits = []
        with open('data/settlement_traits.ni', 'r') as file:
            content = file.readlines()
        for i in content:
            self.traits.append(i.rstrip('\r\n'))

        self.known_for = []
        with open('data/settlement_known_for.ni', 'r') as file:
            content = file.readlines()
        for i in content:
            self.known_for.append(i.rstrip('\r\n'))

        self.calamity = []
        with open('data/settlement_calamity.ni', 'r') as file:
            content = file.readlines()
        for i in content:
            self.calamity.append(i.rstrip('\r\n'))

    def generate(self):
        name = MName().New()
        ruler_status = self.ruler_status[r.randint(0, len(self.ruler_status) - 1)]
        temp = ruler_status
        first = list(temp.lower())

        if (first[0] == "a" or first[0] == "i" or first[0] == "u" or first[0] == "e" or first[0] == "o"):
            start = "an"
        else:
            start = "a"

        result = 'The village/town/city named {4} is governed by {5} {0}, known for its {1} and {2}. It is in a state of calamity due to {3}.'.format(
            colored(ruler_status, 'cyan'),
            colored(self.traits[r.randint(0, len(self.traits) - 1)], 'green'),
            colored(self.known_for[r.randint(0, len(self.known_for) - 1)], 'green'),
            colored(self.calamity[r.randint(0, len(self.calamity) - 1)], 'yellow'),
            colored(name, 'magenta'),
            start
        )
        return result

class Oracle():
    def __init__(self):
        self.pay_price = [
            TOADCell(2, 'Roll again and apply that result but make it worse. If you roll this result yet again, think of something dreadful that changes the course of the adventure.'),
            TOADCell(5, 'A person or community you trusted loses faith in you, or acts against you.'),
            TOADCell(9, 'A person or community you care about is exposed to danger.'),
            TOADCell(16, 'You are separated from something or someone.'),
            TOADCell(23, 'Your action has an unintended effect.'),
            TOADCell(32, 'Something of value is lost or destroyed.'),
            TOADCell(41, 'The current situation worsens.'),
            TOADCell(50, 'A new danger or foe is revealed.'),
            TOADCell(59, 'It puts you at disadvantage.'),
            TOADCell(68, 'It is tiring or harmful.'),
            TOADCell(76, 'A surprising development complicates your quest.'),
            TOADCell(85, 'It is disheartening, upsetting or frightening.'),
            TOADCell(90, 'It wastes resources.'),
            TOADCell(94, 'It forces you to act against your best intentions.'),
            TOADCell(98, 'A companion or ally is put in harm’s way, or you are, if alone.'),
            TOADCell(100, 'Roll twice. Both results occur. If they are the same result, make it worse.')
        ]
        self.twist = [
            'It was all a diversion.', 'A dark secret is revealed.',
            'A trap is sprung.', 'An assumption is revealed to be false.',
            'A secret alliance is revealed.', 'Your actions benefit an enemy.',
            'Someone returns unexpectedly.', 'A more dangerous foe is revealed.',
            'You and an enemy share a common goal.', 'A true identity is revealed.',
            'You are betrayed by someone who was trusted.', 'You are too late.',
            'The true enemy is revealed.', 'The enemy gains new allies.',
            'A new danger appears.', 'Someone or something goes missing.',
            'The truth of a relationship is revealed.',
            'Two seemingly unrelated situations are shown to be connected.',
            'Unexpected powers or abilities are revealed.',
            'Roll twice. (Use the command two times)'
        ]
        self.goals = [
            TOADCell(3,'Obtain an object.'),
            TOADCell(6,'Make an agreement.'),
            TOADCell(9,'Build a relationship.'),
            TOADCell(12,'Undermine a relationship.'),
            TOADCell(15,'Seek a truth.'),
            TOADCell(18,'Pay a debt.'),
            TOADCell(21,'Refute a falsehood.'),
            TOADCell(24,'Harm a rival.'),
            TOADCell(27,'Cure an ill.'),
            TOADCell(30,'Find a person.'),
            TOADCell(33,'Find a home.'),
            TOADCell(36,'Seize power.'),
            TOADCell(39,'Restore a relationship.'),
            TOADCell(42,'Create an item.'),
            TOADCell(45,'Travel to a place.'),
            TOADCell(48,'Secure provisions.'),
            TOADCell(51,'Rebel against power.'),
            TOADCell(54,'Collect a debt.'),
            TOADCell(57,'Protect a secret.'),
            TOADCell(60,'Spread faith.'),
            TOADCell(63,'Enrich themselves.'),
            TOADCell(66,'Protect a person.'),
            TOADCell(69,'Protect the status quo.'),
            TOADCell(72,'Advance status.'),
            TOADCell(75,'Defend a place.'),
            TOADCell(78,'Avenge a wrong.'),
            TOADCell(81,'Fulfill a duty.'),
            TOADCell(84,'Gain knowledge.'),
            TOADCell(87,'Prove worthless.'),
            TOADCell(90,'Find redemption.'),
            TOADCell(92,'Escape from something.'),
            TOADCell(95,'Resolve a dispute.'),
            TOADCell(100,'Roll two more times.'),
        ]

    def price(self):
        roll = r.randint(1, 100)
        result = None
        for i in self.pay_price:
            if(roll <= i.upper):
                result = i.description
                break
        return result

    def plot_twist(self):
        roll = r.randint(0, len(self.twist) - 1)
        return self.twist[roll]

    def get_goal(self):
        roll = r.randint(1,100)
        result = None
        for i in self.goals:
            if(roll <= i.upper):
                result = i.description
                break
        return result
