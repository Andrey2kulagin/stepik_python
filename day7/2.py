def build_query_string(my_dict):
    out_str = ""
    
    for i in sorted(my_dict):
        out_str+=(str(i)+'='+str(my_dict[i])+'&')
    return out_str[:-1]
