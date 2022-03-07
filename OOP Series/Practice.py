from email import charset


class Critter :
    '''A base class for all critter properties'''
    count = 0

    def __init__(self,chat) :
        self.sound = chat
        Critter.count += 1

    def talk(self) :
        return self.sound


polly = Critter('Squawk, squawk!')
print('\nNumber of Critters:', Critter.count)
print('Polly says:', polly.talk())

harry = Critter('Tweet, tweet!')
print('\nNumber of Critters:', Critter.count)
print('Harry says:', harry.talk())


class Bird :
    '''A base class for defining all bird properties'''
    count = 0
    def __init__(self, chat) :
        self.sound = chat
        Critter.count += 1
    
    def talk(self):
        return self.sound


chick = Bird('Cheep, cheep!')
chick.age = '1 week'

print('\nChick says:', chick.talk())
print('Chick Age:', chick.age)

chick.age = '2 weeks'
print('Chick Now:', chick.age)

setattr(chick, 'age', '3 weeks')
