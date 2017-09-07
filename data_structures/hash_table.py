"""
    In this quiz, you'll write your own hash table and hash function that uses string keys. 
    Your table will store strings in buckets by their first two letters, 
    according to the formula below:

    Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
    You can assume that the string will have at least two letters, 
    and the first two characters are uppercase letters (ASCII values from 65 to 90). 
    You can use the Python function ord() to get the ASCII value of a letter, 
    and chr() to get the letter associated with an ASCII value. 
"""


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value
