def partition(nums,low,high):
    if low==high:
        return low
    else:
        i,j=low,high
        mid=i+(j-i)//2
        while i<j:
            while i<high and nums[i]<=nums[mid]:
                i+=1
            while j>low and nums[j]>=nums[mid]:
                j-=1
            if i<j:
                swap1=nums[i]
                nums[i]=nums[j]
                nums[j]=swap1
        if j>mid:
            swap2=nums[mid]
            nums[mid]=nums[j]
            nums[j]=swap2
            return j
        return mid

def quick_sort(nums,low,high):
    if low<high:
        pos=partition(nums,low,high)
        quick_sort(nums,low,pos)
        quick_sort(nums,pos+1,high)

nums=[1,6,7,9,12,3,5]
quick_sort(nums,0,len(nums)-1)
print(nums)
    
