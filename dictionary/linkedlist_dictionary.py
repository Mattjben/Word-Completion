from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None
    
    def get_wordfreq(self):
        return self.word_frequency 

    def get_next(self):
        return self.next

    def set_wordfreq(self, value):
        self.word_frequency  = value

    def set_next(self, next):
        self.next = next

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        self.m_head= None
        self.m_length = 0
        
        


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """

        # Linear insertion 
        # complexity: O(n)

        for value in words_frequencies:
            new_node = ListNode(value)
            
            if not self.m_head:
                self.m_head = new_node
            else:
                new_node.set_next(self.m_head)
                self.m_head = new_node
            self.m_length+=1
            


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # Linear search
        # complexity: O(n)

        cur_node = self.m_head
        for i in range(self.m_length):
            if cur_node.get_wordfreq().word == word:
                return cur_node.get_wordfreq().frequency

            cur_node = cur_node.get_next()

        return 0

        

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # Linear search + insertion  
        # complexity: O(n)
        find = self.search(word_frequency.word)
        if find == 0: 
            new_node = ListNode(word_frequency)

            if not self.m_head:
                self.m_head = new_node
            else:
                new_node.set_next(self.m_head)
                self.m_head = new_node

            self.m_length+=1
            return True
        else:
            return False



    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        
        """
        # Linear search  
        # complexity: O(n)

        cur_node = self.m_head
        prev_node = None
        found = False
        if self.m_length == 0:
            return found
        # check if val is headnode 
        if cur_node.get_wordfreq().word==word:
            self.m_head = cur_node.get_next()
            self.m_length -=1
            found= True
            return found

        for i in range(self.m_length):
            if cur_node.get_wordfreq().word == word:
                prev_node.set_next(cur_node.get_next())
                self.m_length -=1
                found= True
                return found
            prev_node = cur_node
            cur_node = cur_node.get_next()

        return found
        
        


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # Linear search + insertion  
        # complexity: O(n)

        prefix_len = len(word)
        wordfreq_list = []
        freq_list = []
        cur_node = self.m_head
        # loops through entire array and continually saves the top three most frequent words 
        for i in range(self.m_length):
            if word in cur_node.get_wordfreq().word[0:prefix_len]:
                
                if len(freq_list) == 3:
                    if cur_node.get_wordfreq().frequency > min(freq_list):
                        i=freq_list.index(min(freq_list))
                        wordfreq_list[i] = cur_node.get_wordfreq()
                        freq_list[i]=cur_node.get_wordfreq().frequency
                else:
                    freq_list.append(cur_node.get_wordfreq().frequency)
                    wordfreq_list.append(cur_node.get_wordfreq())
            cur_node = cur_node.get_next()
        wordfreq_list.sort(key=lambda x: x.frequency,reverse=True)
    
        return wordfreq_list



