index = n - 1
    while index > 0:
        if arr[index] < arr[index-1]:
            temp=arr[index]
            arr[index] = arr[index -1]
            print(" ".join(map(str,arr)))
            arr[index-1]=temp
        index = index -1
    print(" ".join(map(str,arr))
