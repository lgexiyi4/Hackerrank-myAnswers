# Exceptions - String to Integer
S = raw_input().strip()
try:
    S = int(S)
    print S
except:
    print 'Bad String'
