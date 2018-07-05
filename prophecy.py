'''
import random as r
import nltk
from nltk.parse.generate import generate, demo_grammar
from nltk import CFG

class Adventure():
    def __init__(self):
        with open('data/idea.ni', 'r') as file:
            content = file.read().rstrip('\r\n')
        tokens = nltk.word_tokenize(content)
        text = nltk.Text(tokens)
        print(tokens)
        self.grammar = CFG.fromstring(text)
        self.ideas = list(generate(self.grammar, depth=20))

    def generate(self):
        return self.ideas[r.randint(0, len(self.ideas) - 1)]
'''
import nltk
import numpy
import random as r

class Prophecy():
    def __init__(self):
        self.reject = ['to', 'a', 'of', 'the', 'and', 'are', 'is', 'but', ',', 'they', 'it', 'has', 'that', 'as']
        with open('data/idea.ni', 'r') as file:
            content = file.readlines()#nltk.corpus.gutenberg.words('data/idea.ni')
        self.TEXT = []
        for i in content:
            i = i.rstrip('\r\n')
            for word in i.split(' '):
                character = False
                character_append = ''
                temp = list(word)
                if(len(temp) > 0):
                    current = temp[len(temp) - 1]
                    if(current == ","):
                        character_append = ','
                        character = True
                    elif(current == ';'):
                        character_append = ';'
                        character= True
                    elif(current == ':'):
                        character_append = ':'
                        character= True

                word = word.lower()
                if character == True:
                    self.TEXT.append(character_append)
                else:
                    self.TEXT.append(word.strip("'").strip(',').strip('?').strip('!').strip('.').strip(';'))
        # NLTK shortcuts :)
        self.bigrams = nltk.bigrams(self.TEXT)
        self.cfd = nltk.ConditionalFreqDist(self.bigrams)
        self.cfd_list = list(self.cfd.keys())

    def check(self, input):
        if input in self.reject:
            return ''
        return input

    def generate(self):
        # pick a random word from the corpus to start with
        word = r.choice(self.TEXT)
        result = ''
        # generate 15 more words
        iter = r.randint(25,30)
        for i in range(iter):
            if i != 0:
                space = ' '
            else:
                space = ''
            if word == ',':
                space = ''
            if(i == iter - 1):
                word = self.check(word)
            result += space + word
            #print(self.cfd[word].keys())
            if word in self.cfd:
                #placeholder = 1
                #print(self.cfd.keys())
                word = self.cfd[word].keys()
                word = list(word)
                word = word[r.randint(0, len(word) - 1)]
            else:
                break
        result += "."
        return result.capitalize()

    def test(self):
        return self.cfd.keys()
