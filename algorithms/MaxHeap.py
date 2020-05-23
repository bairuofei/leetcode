class MaxHeap:
    def __init__(self,nums=[]):
        super().__init__()
        self.array=nums
        self.heapify()

    def append(self,num):
        self.array.append(num)
        new_index=len(self.array)
        while new_index!=0 and new_index!=1:
            parent=new_index//2-1
            if self.array[new_index-1]>self.array[parent]:
                swap=self.array[parent]
                self.array[parent]=self.array[new_index-1]
                self.array[new_index-1]=swap
            new_index=parent+1

    def pop(self):
        arr_len=len(self.array)
        if arr_len!=0:
            maximum=self.array[0]
            self.array[0]=self.array[-1]
            self.array=self.array[:-1]
            self.__heap_check(self.array)
            return maximum
        else:
            return None
            
    def __heap_check(self,sort_array,root=0):
        arr_len=len(sort_array)
        left_child=root*2+1
        right_child=root*2+2
        while left_child<arr_len or right_child<arr_len:
            if right_child<arr_len:
                if sort_array[root]<sort_array[left_child] or\
                    sort_array[root]<sort_array[right_child]:
                    if sort_array[left_child]>=sort_array[right_child]:
                        swap=sort_array[left_child]
                        sort_array[left_child]=sort_array[root]
                        sort_array[root]=swap
                        root=left_child
                    else:
                        swap=sort_array[right_child]
                        sort_array[right_child]=sort_array[root]
                        sort_array[root]=swap
                        root=right_child
                    left_child=root*2+1
                    right_child=root*2+2
                else: break
            else:
                if sort_array[root]<sort_array[left_child]:
                    swap=sort_array[left_child]
                    sort_array[left_child]=sort_array[root]
                    sort_array[root]=swap
                break

    def heapify(self):
        num_index=len(self.array)//2-1
        while num_index!=-1: 
            self.__heap_check(self.array,root=num_index)
            num_index-=1
        return self.array
    
    def heap_sort(self):
        result=[]
        for i in range(len(self.array)):
            result.append(self.pop())
        return result

if __name__=="__main__":
    nums=[1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    heap_ex=MaxHeap(nums)
    heap_num=heap_ex.heap_sort()
    print(heap_num)



