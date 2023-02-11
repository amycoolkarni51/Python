#Write a program for bubble sort using python for the list a=[12, 5, 7, 18, 11, 6, 12, 4, 17, 1]  
def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    n=len(list1)
    for i in range(n):  
        for j in range(n-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  
  
a=[12, 5, 7, 18, 11, 6, 12, 4, 17, 1]  
print("The sorted list is: ", bubble_sort(a))  