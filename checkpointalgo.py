#!/usr/bin/env python
# coding: utf-8

# In[1]:


#quest 1
def binary_search(A, l, h, k):
    if h >= l:
        mid = int(l + (h - l)/2)
        print(mid)
        if A[mid] == k:
            return 'k is found'
        elif A[mid] > k:
            return binary_search(A, l, mid-1, k)
        else:
            return binary_search(A, mid+1, h, k)
    else:
        return 'k is not found'
A=[1,2,3,5,8]
k=5;l=0; h=len(A)-1;
binary_search(A,l,h,k) 


# In[ ]:


#quest 3
def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    return nlist

nlist = [29,13,22,37,52,49,46,71,56]
bubbleSort(nlist)


# In[6]:


#quest 4:
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1
    return(myList)
myList=([29,13,22,37,52,49,46,71,56])
mergeSort(myList)


# In[ ]:


#quest 5
def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
array=[29,13,22,37,52,49,46,71,56]
quick_sort=[array,0,len(array)-1]
    


# In[ ]:





# In[ ]:




