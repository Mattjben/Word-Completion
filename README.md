# Word-Completion

The objective of this project is to implement three different dictionaries containing words and thier respective frequencies each contained within different data sturcture types (linked list , array , trie) and compare and compute the practical and theoretical time complexities of various operations. 

Each data structure was implemented so that it could perform: 
- **Construction**: Build a dictionary based on a given set of words and their respective frequencies 
- **Additon**: Add a word and its frequency to the dictionary 
- **Deletion**: Remove a specified word from the dictionary 
- **Autocomplete**: Display the top 3 words (highest frequency) with the same prefix of a given inputted prefix 

*FOR MORE DETAILED EXPLANATION OF EXPERIMENTAL SETUP PLEASE READ report.pdf*

## FILES: 

- Report.pdf: Report that details our experimental setup , results and disccussion for comparing the different data structures 
- dictionary_file_based.py: Code that reads in operation commands from file then executes those on the specified nearest neighbour data structure.  
-> USE:   `python3 dictionary_file_based.py datastructer(list/array/trie) Datafile inputcommands outputfile`   
- dictionary_test_script.py: Code that executes dictionary file based.py and tests your code on Linux servers.   
-> USE:  `python3 dictionary_test_script.py $PWD <approach> <data filename> <command filename1> <command filename2>`
- data generation: contains all input and data files used to test code and Generation.ipynb used to create those files  
- results: Contains code used to generate results table and results table itself 
- dictionary: contains all source code for dictionaries 


