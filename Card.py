from word2number import w2n

class Card:
    
    def __init__(self,rank: str, suit: str):
        self.rank=rank
        self.suit=suit
        self.value=0
        self.value=self.assignValue()
        
    
    def assignValue(self):
        if(self.rank=="King" or self.rank=="king"):
            self.value=self.value+13
        elif(self.rank=="Queen" or self.rank=="queen"):
            self.value=self.value+12   
        elif(self.rank=="Jack" or self.rank=="jack"):
            self.value=self.value+11  
        else:
            self.value=self.value+w2n.word_to_num(self.rank)
        return(self.value)

    
