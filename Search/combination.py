def combination(nums,depth,n,start_i,curr,ans):
    if depth==n:
        ans.append(curr[:])
        return
    
    for i,num in enumerate(nums[start_i:]):
        curr.append(num)
        combination(nums,depth+1,n,start_i+i+1,curr,ans)
        curr.pop()

if __name__=="__main__":
    nums=[1,2,3]
    n=2
    ans=[]
    combination(nums,0,n,0,[],ans)
    print(ans)