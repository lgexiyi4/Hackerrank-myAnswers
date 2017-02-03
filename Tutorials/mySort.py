# mySort: bubble sort
class mySort:
    def bubbleSort(self,a,n): # list 'a' with length 'n'
        self.a = a
        self.n = n
        self.swapnum = 0
        for i in range(n):
            for j in range(n-1-i):
                if(self.a[j]>self.a[j+1]):
                    self.swap(j,j+1)
                    self.swapnum += 1
            if self.swapnum==0:
                break
    def swap(self,p,q):
        temp = self.a[p]
        self.a[p] = self.a[q]
        self.a[q] = temp
    

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
aBubble = mySort()
aBubble.bubbleSort(a,n)
print("Array is sorted in "+repr(aBubble.swapnum)+" swaps.")
print("First Element: "+repr(aBubble.a[0]))
print("Last Element: "+repr(aBubble.a.pop()))