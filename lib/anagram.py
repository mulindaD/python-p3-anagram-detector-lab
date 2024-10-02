# your code goes here!

class Anagram:
    def __init__(self, word="word"):
        self._word = word

    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, word):
        if type(word) is str:
            self._word = word
        else:
            print("Please enter a valid word!")

    def match(self, list_of_anagrams):
        anagrams = []

        for word in list_of_anagrams:
            if sorted([char for char in self._word]) == sorted([char for char in word]):
                anagrams.append(word)
            
        return anagrams
        
        


    