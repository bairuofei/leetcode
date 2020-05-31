def two_way_merge(list1,list2):
    len1=len(list1)
    len2=len(list2)
    index1,index2=0,0 # tuple unpacking
    return_list=[]
    while index1<len1 and index2<len2:
        if list1[index1]<=list2[index2]:
            return_list.append(list1[index1])
            index1+=1
        else:
            return_list.append(list2[index2])
            index2+=1
    if index1==len1 and len2!=0:
        return_list.extend(list2[index2:])
    elif index2==len2 and len1!=0:
        return_list.extend(list1[index1:])
    return return_list

def merge_sort(nums):
    low=0
    high=len(nums)-1
    if low<high:
        mid=(low+high)//2
        nums1=merge_sort(nums[:mid+1])
        nums2=merge_sort(nums[mid+1:])
        sorted_nums=two_way_merge(nums1,nums2)
        return sorted_nums
    else:
        return nums

a=[2,1,4,6,3,9,7]
b=merge_sort(a)
print(b)
