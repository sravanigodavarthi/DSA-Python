# Better address scheme is to always have a prime number(0 - 6)
# increases the randomness of how key value pair distributed through the hash table

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hashvalue(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash+ord(letter)*23) % len(self.data_map)
        return my_hash
    
    def print(self):
        for index,item in enumerate(self.data_map):
            print(f"{index}:{item}") 
    
    def set(self,key,value):
        index = self.__hashvalue(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])
    
    def get(self,key):
        index = self.__hashvalue(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if key ==  item[0]:
                    return item[1]
            return None
    
    def key(self):
        my_list = []
        for item in self.data_map:
            if item is not None:
                for items in item:
                    my_list.append(items[0])
        return my_list
        
my_hashtable =  HashTable()
my_hashtable.set('firstname','sravani')
my_hashtable.set('lastname','samudrala')
my_hashtable.set('middlename','venkata lakshmi')
# print(my_hashtable.get('firstname'))
# my_hashtable.print()
print(my_hashtable.key())