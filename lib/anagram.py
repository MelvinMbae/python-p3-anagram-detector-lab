# your code goes here!
class Anagram:
    def __init__(self, my_word):
        self.my_word = my_word
        
    def match(self, anagram_list):
        self.anagram_list = anagram_list
        return [word for word in anagram_list if self.is_an_anagram(word)]
    
    def is_an_anagram(self, other_word):
        return sorted(self.my_word) == sorted(other_word)
             
listen = Anagram("listen")
print(listen.match(["listen", "poison", "hello"]))