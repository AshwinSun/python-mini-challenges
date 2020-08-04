# --------------
#Code starts here
def palindrome(num):
    numstr=str(num) #convert to string
    for i in range(num+1,1000000000): 
        if (str(i)==str(i)[::-1]): #compare the string to its reversal
            return i

print(palindrome(121))


# --------------
#Code starts here
def a_scramble(str_1,str_2):
    res=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            res=False
            break
        str_1=str_1.replace(i,'',1)
    return(res)    



a_scramble('Tom Marvolo Riddle','Voldemort')



# --------------
#Code starts here
def check_fib(num):
    n1=0
    n2=1
    n3=0
    while(n3<num):
        n3=n1+n2
        n1=n2
        n2=n3

    if(n3==num):
        return True
    else:
        return False
    

check_fib(987)






# --------------
#Code starts here
#Code starts here

#Function to compress string
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)
compress("abbs")    

#Code ends here


# --------------
#Code starts here

#Function to check existence of k distinct characters in string
def k_distinct(string,k):
    s_list=(set(string.lower()))
    return len(s_list)>=k

k_distinct("banana",4)

#Code ends here


