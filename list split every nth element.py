list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(list)
def slice(S, step):
    return[S[i::step] for i in range(step)]
print(slice(list,3))