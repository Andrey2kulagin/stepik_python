def mean(*args):
    cure_arr = []
    for i in args:
        if  type(i) is int or type(i) is float:
            cure_arr.append(i)
    if len(cure_arr)==0 or sum(cure_arr)==0:
        return 0
    return(sum(cure_arr)/len(cure_arr))
