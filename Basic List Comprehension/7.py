# identify duplicates in a tuple 

sample_tuple=(1,2,3,2,1,4)      # sample tuple
no_dup=set(sample_tuple)        # removing duplicates 

for i in no_dup:
    if sample_tuple.count(i)>1:
        print(i)

print("Robin Roy\n22BRS1114")