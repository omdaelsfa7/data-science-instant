class rev():
    def setter(self,string  ):
        self.string = string 
    def revers_str(self):
        self.string = self.string.split(" ")
        self.string.reverse()
        self.string = " ".join(self.string) 
        return self.string  
rev1 = rev 
rev1.setter("omda","omda")    
print(rev1.revers_str)        