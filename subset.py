def subset(x):
    subset = []
    subset.append([])

    for i in x:
        for ss in range(0, len(subset)):
            temp = sorted(subset[ss] + [i])
            subset.append(temp)
    
    subset = sorted(subset)
    new_subset = []
    new_subset.append([])
    
    
    for ss in range(1, len(subset)):
        previous = subset[ss-1]
        if subset[ss] != previous:
            new_subset.append(subset[ss])


    return new_subset

print(subset([4,4,4,1,4]))