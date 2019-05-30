from random import randint
class HashMaker:

    def __init__(self):
        self.hash_value = '0'

    def create_hash(self):
        self.hash_value = hash(randint(100000000,999999999))

    def get_hash(self):
        return self.hash_value