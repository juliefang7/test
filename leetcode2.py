'''convert Roman numbers to integars
INPUT: roman numbers
OUTPUT: the corresponsing integar
'''
def romanToInt(s):
    i = 0
    mynum = 0
    mydic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if mydic[s[len(s)-2]] >= mydic[s[len(s)-1]]and len(s) > 1:
        mynum += mydic[s[len(s)-1]]
		#to add the last number
    if len(s) == 1 :
        mynum += mydic[s]
			#if the number is made out of one character
    while i < len(s)-1:
        i += 1
        if mydic[s[i-1]] < mydic[s[i]]:
			#to check if number after is greater
            mynum +=  mydic[s[i]]-mydic[s[i-1]]
            i+=1 #add i one so that the program checks for next pair of letters'''
					
        else:
            mynum += mydic[s[i-1]]
					

    return mynum 