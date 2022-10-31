from sys import prefix
from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect as by



class ArrayDictionary(BaseDictionary):
    dictionary = []

    def __init__(self,dictionary=dictionary):
        self.dictionary = dictionary
        pass


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # words are allready in array format just need to sort values:
        #complexity: O(nlogn)
        dict = words_frequencies
        dict.sort(key=lambda x: x.word)
        self.dictionary = dict
        
        return self.dictionary

       


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        # Binary search algorithm
        # Complexity: O(log(n)) 

        dict = self.dictionary
        i = by.bisect_left(a=dict,x=word,key=lambda x: x.word)
    
        if i != len(dict) and dict[i].word == word:
            freq = dict[i].frequency
            return freq
        else:
            return 0
 
     

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # Binary search algorithm + insertion sort
        # Complexity: O(n)

        dict = self.dictionary
        find = self.search(word_frequency.word)
        if find == 0: 
            by.insort(dict,word_frequency,key=lambda x: x.word)
            return True
        else:
            return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # Binary search algorithm + bisect_left
        # Complexity: O(log(n))

        # find the position of 'word' in the list, if exists, will be at idx-1
        dict = self.dictionary
        find = self.search(word)
        if find == 0: 
            return False
        else:
            i = by.bisect_left(a=dict,x=word,key=lambda x: x.word)
            self.dictionary.pop(i)
            return True


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """

        # Complexity: O(Klog(n)) --> loops through binary search algorithm for each word with the prefix

        dict = self.dictionary
        prefix_len = len(prefix_word)
        dict_copy = dict.copy()
        wordfreq_list = []
        i=0
        while i ==0:
            w = by.bisect_left(a=dict_copy,x=prefix_word,key=lambda x: x.word)
            if w != len(dict_copy) and prefix_word in dict_copy[w].word[0:prefix_len]:
                wordfreq_list.append(dict_copy[w])
                del dict_copy[w]
            else:
                i =1
        wordfreq_list.sort(key=lambda x: x.frequency,reverse=True)
        if len(wordfreq_list) >= 3:
            wordfreq_list = wordfreq_list[0:3]
        

        return wordfreq_list