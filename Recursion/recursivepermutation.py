def splitter(l):
    if len(l) == 1:
        return [l]
    else:
        l2=[]
        for i in range(len(l)):
            first_letter=l[i]
            without_first_letter = l[:i] + l[i+1:]
            
            for j in splitter(without_first_letter):
                l2.append([first_letter] + j)
        return l2
    
print(splitter([1,2,3,4]))