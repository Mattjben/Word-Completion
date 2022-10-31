from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
        self.root = None
        pass

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        
        #Complexity: O(nL) , where L is the length of each word 

        # set node 
        self.root = TrieNode()
        current_node = self.root
        # iterate through word_frequency list:
        
        for wordfreq in words_frequencies:
            word = wordfreq.word
            for char in word:
                if char in current_node.children.keys():
                    current_node = current_node.children[char]
                else:
                    new_node = TrieNode(letter=char)
                    current_node.children[char] = new_node
                    current_node = new_node
            current_node.is_last = True
            current_node.frequency = wordfreq.frequency
            current_node = self.root
        



    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        #Complexity: O(L) , where L is the length of word being searched 
        current_node= self.root
        count = 1
        for letter in word: 
            if letter in current_node.children.keys():
                current_node = current_node.children[letter]
                
                if count == len(word):
                    
                    if current_node.is_last == True:
                        
                        return current_node.frequency
                    else:
                        return False
            else:
                return False
            count+=1

      


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        #Complexity: O(L) , where L is the length of word being searched 
        current_node = self.root
        # iterate through word_frequency list:
        
        word = word_frequency.word
        for char in word:
            if char in current_node.children.keys():
                current_node = current_node.children[char]
            else:
                new_node = TrieNode(letter=char)
                current_node.children[char] = new_node
                current_node = new_node
        if current_node.is_last == True:
            return False
        else:
            current_node.is_last = True
            current_node.frequency = word_frequency.frequency
            return True
        
            

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        #Complexity: O(L) , where L is the length of word being searched 
        current_node = self.root
        last_child_node = None
        last_letter = word[0]
        count =1
        for letter in word: 

            if letter in current_node.children.keys():
                
 
                if len(current_node.children) > 1 or current_node.is_last==True:
                    last_child_node = current_node
                    
                    last_letter = letter

                current_node = current_node.children[letter]
                
                if count == len(word):
                    if current_node.is_last == False:
                        return False
                    else:
                        if len(current_node.children) > 0:
                            current_node.is_last = False
                            current_node.frequency = None
                        else:
                            if last_child_node:
                                del last_child_node.children[last_letter]
                elif current_node.is_last==True:
                    last_child_node = current_node

                    last_letter = letter
            else:
                return False
            count+=1
        return True



    def depth_first(self,current_node,current_word,word_freqs):
        """Recursive depth-first search algorithm for autocompletion 
        @return: a lits of all word frequencies with the specified prefix 
        """
        
        if current_node.is_last:
                wf = WordFrequency(current_word,current_node.frequency)
                word_freqs.append(wf)
    
        for child in current_node.children.keys():
            self.depth_first(current_node.children[child],current_word+ child,word_freqs)
        

        return word_freqs

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        #Complexity: Θ(V), where V is the number of nodes after the prefix 
        # finds node with specified prefix and runs recursive depth first search on all its children 
        current_node = self.root
        current_word =""
        for letter in word: 
            
            if letter in current_node.children.keys():
                current_node = current_node.children[letter]
                current_word+= letter
                
            else:
                return []
        #sorts the words with the prefix and displays the top 3
        word_freqs= self.depth_first(current_node,current_word,[])
        word_freqs.sort(key=lambda x: x.frequency,reverse=True)
        if len(word_freqs) <3:
            return word_freqs
        else:
            
            return word_freqs[0:3]
    
    

        

