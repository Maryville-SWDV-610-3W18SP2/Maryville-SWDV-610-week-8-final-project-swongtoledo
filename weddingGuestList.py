'''The problem that I wanted to solve happened quite recently when I was trying to plan for my wedding.
It was a small destination wedding and I had a guest list but I needed to limit the guest size of 14 people.
The restaurant that I planned where my reception would be, had a really nice cabana set up
overlooking the water, however the limit was for 14 people. 
So for this problem, I wanted to see every possible way I can sit my guests together and who I can
remove from the guest list to keep my limit to 14 people. In this scenario,
I used recursion to figure out multiple ways guests can sit next each other. '''




guest = ['Andy','Brandi','Jay','Sheri','Tony','Alicia','Ian','Miguel','Noreen','Carol','Lionel','Anthony','Nils','Terese','Naomi']


def combination(guest,tablesize):
    groups = combineguest(guest,tablesize)
    print (groups)
    
def combineguest(guest,tablesize,pos = 0, group=[],groups = []):

    if(len(group)) is tablesize:
       groups.append(group)
    
    elif pos < len(guest):

        #leave 
        combineguest(guest,tablesize,pos+1,group)
    
        #Keep
        new_group = list(group)
        new_group.append(guest[pos])
        combineguest(guest,tablesize,pos+1,new_group)
    return groups
    
    
    
    
c = combination(guest,14)

