""" /*****Bubble sort algoriths***/
A bubble sort compares pairs of adjacent elements and swaps those elements if they are not in order. It is commonly implemented in Python to sort lists of unsorted numbers. Bubble sorts are a standard computer science algorithm. By using a bubble sort, you can sort data in either ascending or descending order

"""

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
nums=[5,3,8,6,7,2]
sort(nums)
print(nums)
