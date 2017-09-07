<table style="width:100%">
  <tr>
    <th><a href="/just-learn-this">Home</a></th>
    <th><a href="/just-learn-this/data_structures/data_structure_menu.html">Data Structures</a></th>
  </tr>
</table>

```python

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


"""
    Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
    You can assume that the string will have at least two letters, 
    and the first two characters are uppercase letters (ASCII values from 65 to 90). 
    You can use the Python function ord() to get the ASCII value of a letter, 
    and chr() to get the letter associated with an ASCII value. 
"""

```