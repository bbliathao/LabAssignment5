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

"""
main() :
    set sentence = input()
    set dictionary = create_dictionary()
    translate(sentence, dictionary)

translate(sentence, dictionary):

    words = for each of the words in the sentence
    for each words, translate the word
    print translated sentence to user

create_dictionary():
    read in textese.txt
    create list = each line from file 
    close the file
    create a dict off of the list
    return the dict

main()
"""

def main() 
    sentence = "enjoy the excellent band tonight"
    dictionary = create_dictionary()

def create_dictionary(txt_file) :
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]   
    infile.close()
    return dict ([word.split(",")for word in words])

    for word in words: 
        [k,v] = word. split(",") 
        translation[k] = v
    
    return translation

def translate(sentence, dictionaru)
    print("From translate", sentence)
    words = sentence.split()
    for word in words:
        print(dictionary.get(word,word)," , end="")

main()
