def countSwaps(a):
    # Write your code here
    numSwaps =0
    swapp=False
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
             temp=a[j];
             a[j]=a[j+1]
             a[j+1]=temp
             swapp=True
             numSwaps=numSwaps+1
        if not swapp:
            break
    lastElement =a[len(a)-1]
    firstElement=a[0]
    print("Array is sorted in "+str(numSwaps) +" swaps.")
    print("First Element: "+str(firstElement)  )
    print("Last Element: "+str(lastElement) )
