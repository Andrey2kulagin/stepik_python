def merge(values):      # values - это список словарей
    out_dict = {}
    for i in values:
        for j in i:
            if out_dict.get(j) != None:
                out_dict[j].add(i[j])
            else:
                out_dict[j] = {i[j]}
    return out_dict



