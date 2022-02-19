def get_abs_diff(list_length,list):
    abs_diffs=[]
    for i in range(list_length):
        for j in range(list_length):
            if i==j:
                continue
            abs_diffs.append(abs(list[i]-list[j]))
    return min(abs_diffs)

if __name__=="__main__":
    list_length=int(input())
    list=input().split()
    list = [int(i) for i in list]
    print(get_abs_diff(list_length,list))
