"""
The program is trying to translate a sentence captured as user input.
We first read in the text file textese.txt.
Then from the text file, we create a list of strings from each lines in the text file
Then, we create a dictionary from the lists.
Once the text file has been read into memory, we close the file. 

We then define a function for translating which involves splitting the users input(sentence) 
into an array of strings ("Enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

Once we have the array of strings representing the user's input sentence, we 
loop through each words, fine the key matching word and returns back the value tied to the word
in our dictionary.

After each word is translated, we then
Print out the translated sentence to the user.
"""


