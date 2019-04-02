#Markov Model Second Order Sentence Generator
#By Lachlan Page
import random

def markov_generate():
    file_string = ""
    with open("data/idea.ni", 'r') as content_file:
        file_string = content_file.read()

    file_string = file_string.split()

    #full stop in dictionary to handle end cases
    chain = {}
    chain['.'] = ' '

    #More efficient algorith. O(n)
    for i in range(0, len(file_string)):
        key = file_string[i]
        if key not in chain:
            chain[key] = []
            if(i + 1 < len(file_string)):
                chain[key].append(file_string[i+1])
            else:
                chain[key].append('.')
        else:
            #already exists in chain
            if(i+1 < len(file_string)):
                chain[key].append(file_string[i+1])
            else:
                chain[key].append('.')

    #Prediction
    #print(len(chain.keys()))
    #Can move to dedicated function or something...
    WORD_LENGTH = 20
    start_word = random.choice(list(chain.keys()))
    final_word_list = []
    final_word_list.append(start_word)
    for i in range(WORD_LENGTH):
        current_word = final_word_list[i]
        next_word = random.choice(chain[current_word])
        final_word_list.append(next_word)

    #Formatting python list to a string for output
    result = ''
    for word in final_word_list:
        result+= str(word) + " "
    return result

def markov_generate_2():
    file_string = ""
    with open("text.txt", 'r') as content_file:
        file_string = content_file.read()

    #Fixing formatting for sampletext, this can be removed for other text sources
    file_string = file_string.lower()
    file_string = file_string.replace("!" , " ")
    file_string = file_string.replace("." , " ")
    file_string = file_string.replace("," , " ")
    file_string = file_string.replace("@" , " ")
    file_string = file_string.replace("&amp;", " ")
    file_string = file_string.replace("?", " ")
    file_string = file_string.replace("-", " ")
    file_string = file_string.split()

    #full stop in dictionary to handle end cases
    chain = {}
    chain['.'] = ' '

    #More efficient algorith. O(n)
    for i in range(0, len(file_string)):
        if(i + 1 < len(file_string)):
            key = (file_string[i], file_string[i+1])
            if key not in chain:
                chain[key] = []
                if(i+2 < len(file_string)):
                    chain[key].append(file_string[i+2])
                else:
                    chain[key].append('.')
            else:
                #already exists in chain
                if(i+2 < len(file_string)):
                    chain[key].append(file_string[i+2])
                else:
                    chain[key].append('.')

    #prediction
    WORD_LENGTH = 20
    start_word = random.choice(tuple(chain.keys()))
    final_word_list = []
    current_tuple = start_word

    for i in range(WORD_LENGTH):
        current_word = current_tuple
        next_word = random.choice(chain[current_word])
        current_tuple = (current_word[1], next_word)
        if i == 0:
            temp = list(next_word)
            temp[0] = temp[0].upper()
            next_word = ''
            for j in temp:
                next_word += j
        final_word_list.append(next_word)

    result = ''
    for word in final_word_list:
        result+= str(word) + " "
    return result
