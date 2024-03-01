from projectq import * # import functions from the file projectq


def word_comparator(filename, word_list:list):
    '''
    The function takes a file, that need to be saved in the project environment. It opens it and processes its content.
    For every word in the word_list it builds a semantic vector.Then computes the cosine similarity between every 
    couple of vectors. Finally it prints the couples with the highest similarity.
    
    :param filename: It is the name of the file we want to process. To not use the path of the file,
    said file should be stored within the same project/environment of the .py file we are calling it in.
    :param word_list: List of words we want to build the vectors and compute similairty for.
    :return: It prints the cuples of worsd, whose similairty has the highest values.
    '''
    text= read_reference_text("ref-sentences.txt") # opens the file and processes it
                                                   # text as an object is a list of lists of strings
    temp_dict = {word: make_word_vector(word, text) for word in word_list} # for every words in word_list;
                                                                           # makes semantic vectors,
                                                                           # store semantic vectors as values in a dictionary, 
                                                                           # whose keys are the corresponding words the vectors describe
    sim_comparison = []  # initialises an empty list
    for i in range(len(word_list)):  # loops over the range of the length of the word list, so all the words in the list
        min_distance = 0.0  # Initialises a float representing the maximum closeness between two words, given the context
        for j in range(len(word_list)):  # Second loop over the word_list, because the similarity is calculated between 2 words
            if j == i:  # if the 2 loops run into the same word, do not compute the cosine similarity;
                        # it iterates 2 times over the same fixed list, if the iterators i and j (integers) are in the same position
                        # the function would take 2 words that are equal, the cosine similarity would be 1
                pass
            else:
                similarity = sim_word_vec(temp_dict[word_list[i]], temp_dict[word_list[j]])  # apply the function built for the cosine similairty
                                                                                      # on the vectors (of the words i and j)  we selected
                if similarity > min_distance:  # if the new similarity computed is greater than the minimum distance
                    min_distance = similarity  # updates the minimum distance object, meanimg words with closer semantic meaning have been found
                    compared_element_position = j  # need to update the second word position
        print(word_list[i], "/", word_list[compared_element_position],"->", min_distance) # print the couples of words which are closest in semanting meaning
                                                                                          # and their corresponding distance





def main():
     filename= "ref-sentences.txt"

     word_list_tt= ["canada", "disaster", "flood", "car", "road", "train", "rail", "germany", "switzerland",
                   "technology", "industry", "conflict"]
     word_list = ["spain", "anchovy", "france", "internet", "china", "mexico", "fish", "industry", "agriculture",
                   "fishery", "tuna", "transport", "italy", "web", "communication", "labour", "cod"]
     print(word_comparator(filename, word_list))

if __name__ == "__main__":
    main()

