class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        i=h
        count=0
        while count <=self.MAX:
            if self.arr[i] is None:
                return None
            elif self.arr[i][0]==key:
                return self.arr[i][1]
            i = (i+1)%self.MAX
            count+=1
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        i=h
        count=0
        while count <=self.MAX:
            if self.arr[i] == None or self.arr[i][0] == key:
                self.arr[i]=(key,val)
                break
            i = (i+1)%self.MAX
            count+=1
        else:
            print("Hash map is full")
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        i=h
        count=0
        while count <=self.MAX:
            if self.arr[i] == None or self.arr[i][0] == key:
                self.arr[i] = None
            i = (i+1)%self.MAX
            count+=1
h1 = HashTable()
h1['a']=0
#h1['k']=1
h1['c']=2
h1['d']=3
h1['e']=4
h1['f']=5
h1['g']=6
h1['h']=7
h1['i']=8
h1['j']=9
del h1['c']
print(h1.arr)
print(h1['k'])
