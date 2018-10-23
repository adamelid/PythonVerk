def make_sublists(a_list):
    sublist = []
    sublist.append()
    for stak in range(1,len(a_list)+1):
        sublist.append(stak)
        for undirStak in range(stak, len(a_list)+1):
            sublist.append()
        
# Main program starts here

# This should be the last statement in your main program/function 
print(sorted(sub_lists))
