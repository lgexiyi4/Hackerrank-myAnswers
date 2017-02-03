# More Exceptions
class Calculator:
    def power(self,n,p):
        self.n = n
        self.p = p
        if self.n<0 or self.p<0:
            e = 'n and p should be non-negative'
            return e
        else:
            return(n**p)

myCalculator = Calculator()
T = int(raw_input())
for i in xrange(T):
	n,p = map(int, raw_input().split())
	try:
		ans = myCalculator.power(n,p)
		print ans
	except Exception,e:
		print e