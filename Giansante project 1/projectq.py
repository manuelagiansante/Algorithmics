
import re # to use the split method on the text we import
import math # to use the methods needs in the scalar products and cosine similarity computations
from stopwords import * # import stop words content

def read_reference_text(filename: str) -> list[list[str]]:
    '''
    The function opens the txt file, and processes it line by line. 
    Returning a list of the lines in it, after having separated words and having lowered the case of them.
    Resource: Assignment PDF.
    
    :param filename: It is the name of the file we want to process. To not use the path of the file,
    said file should be stored within the same project/environment of the .py file we are calling it in.
    :return: The function returns a list of the sentences, which themselves are lists of the words in them.
    These words have been cleaned from punctuation and turned into lower case.
    '''
    f=open(filename,encoding="utf8") #filename is string containing the file name;
                                     # encoding utf-8 is how to interpret the text file;
                                     # it means that unicode charcater can be transformed into a string of binary code
                                     # the function open reads the file line by line
    txt=[] # initilise an empty list where we will store our sentences
    for x in f: # for every line x in the file we opened
        content =re.split("[ ,;:\’\"\?!\n]+", x) # split words by these characters
                                                 # initialise object content where we store separated characters
        lower=list(map(lambda x:x.lower(), content)) # method map applies to lower methode to all elements in content
                                                     # initialise lower object where separated and transformed strings are stored
        txt.append(lower) # add to list txt every list of strings we processed
    f.close() #close the .txt file we used
    return txt # return list of lists of strings



def make_word_vector(w: str, txt: list[list[str]]) -> dict[str, int]:
    '''
    The function takes a word w and for it builds a semantic vector. The semantic vector is a dictionary
    with its keys as all the words that are within the same sentece as w, and the corresponding values
    are the frequency with which they appear in th esame sentence as w.
    This dictionary does not include the most common words, that are listed in the stop words list.
    Resource: Assignment PDF and dictionary slides and material covered in class.
    
    :param w: It is a string, the word the function builds the semantic vector for.
    :param txt: The list of lists we generated in the previous function. This is where the function
    looks for the context in which our string w appears.
    :return: A dictionary with all the words that appear in the same sentence with w,and the frequency they do that with.
    '''
    words_of_context=[] # initialise an empty list we will build our dictionary from
    for sentences in txt: # loop over every sentence within the list txt
            for words_strings in sentences: #access the strings in the sentences
                if w in sentences: # is the word are considering in a sentence
                    words_of_context.append(words_strings) # then we add all the words in that sentence to the empty list

    semantic_vector={} # initialise empty dictionary
    for word in words_of_context: # iterate over every string in the words_of_context list
            if word not in stopwords and len(word)>=3 and word!=w: # the word to be used as a key needs to be not in the stop words list;
                                                                   # longer than 3 characters, and not the word we are building the semantic vector around
                if word in semantic_vector: # we start adding the eligible words to the dictionary
                    semantic_vector[word]= semantic_vector[word]+1 # the value is the frequency so if the word appears multiple times we add 1
                else:
                    semantic_vector[word]=1 # if the word is not in the dictionary already we add it in with value (frequency) 1
    return semantic_vector # return our semantic vector


def sim_word_vec(v1: dict[str, int], v2: dict[str, int]) -> float:
    '''
    The function takes 2 sematic vectors of two different words and computes their cosine similarity.
    Resource: Dictionary slides, material done in class.

    :param v1: Semantic dictionary of word 1.
    :param v2: Semantic dictionary of word 2.
    :return: It returns a float value, which expresses how similar the 2 words are in terms of the context they appear in.
    '''
    sp = 0.0 # scalar product at the numerator as a float starting from 0
    sp_1 = 0.0 # scalar product of dictionary 1 at the denominator starting from 0.0
    sp_2 = 0.0 # scalar product of dictionary 2 at the denominator starting from 0.0
    for word in v1: # iterating over every word in the dictionary for word 1
        sp += v1[word] * v2.get(word, 0)  # scalar product of frequencies of words that are in both vectors, otherwise multiply by 0
        sp_1 += v1[word] * v1.get(word, 0) # scalar product of words in vector 1
    for word in v2: # for ecvery words in vector 2
        sp_2 += v2[word] * v2.get(word, 0) # compute scalar product of words in vector 2
    return sp / (math.sqrt(sp_1 * sp_2)) # return the cosine similarity






def main():
    '''
    The main in this case recalled all the function we wrote with the needed arguments to check whether the functions we built worked.

    :return: It prints out the results for each function, up to necessity.
    '''
    #filename= "ref-sentences.txt"
    #print(read_reference_text(filename))
    '''w=['spain', 'anchovy','france','internet','china','mexico', 'fish',
       'industry','agricolture','fisher','tuna','transport', 'italy', 'web', 'communication', 'labour',
       'fish', 'cod']'''
    #w = "spain"
    #print(make_word_vector(w,txt))

    #v1 = make_word_vector('spain', txt)  # why do i have to specify
    #v2 = make_word_vector('anchovy', txt)
    #print(sim_word_vec(v1,v2))
if __name__ == "__main__":
    main()