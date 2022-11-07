def sequential_search(list_, n):
    x = False
    for i in list_:
        if i == n:
            x = True
            break
    print(x)

list_ = range(1,100)    
sequential_search(list_, 50)