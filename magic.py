from termcolor import colored, cprint

class Magic():
    def __init__(self):
        self.alphabet = {
            'a': 'az',
            'b': 'bey',
            'c': 'kei',
            'd': 'dah',
            'e': 'en',
            'f': 'fo',
            'g': 'gah',
            'h': 'hes',
            'i': 'in',
            'j': 'jen',
            'k': 'kei',
            'l': 'li',
            'm': 'mah',
            'n': 'ni',
            'o': 'ot',
            'p': 'pah',
            'q': 'qo',
            'r': 'rah',
            's': 'set',
            't': 'tag',
            'u': 'un',
            'v': 'vey',
            'w': 'wo',
            'x': 'nex',
            'y': 'yeh',
            'z': 'zet',
        }

    def translate(self, input):
        input = input.rstrip('\r\n')
        word = list(input)
        result = ''

        for i in range(len(word)):
            if(i == 0):
                result += colored(self.alphabet[word[i]].capitalize(), 'cyan')
            else:
                result += colored(self.alphabet[word[i]], 'yellow')
            if(i < len(word) - 1):
                result += '-'

        return result
