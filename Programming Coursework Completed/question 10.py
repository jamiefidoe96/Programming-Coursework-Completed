def sequences(n):
    sequences = []
    curSeq = []
    longSequence = 0
    for ind, val in enumerate(n):
        curSeq.append(val)
        if ind < len(n)-1 and val >= n[ind+1]:
            sequences.append(curSeq)
            longSequence = max(longSequence, len(curSeq))
            curSeq = []
    sequences.append(curSeq)
    longSequence = max(longSequence, len(curSeq))
    return [seq for seq in sequences if len(seq) == longSequence]

print(sequences([1,2,4,1,2,3,2,4,7,8,10,12,1,3,4,5,6,7]))
