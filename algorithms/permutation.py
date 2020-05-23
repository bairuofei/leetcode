def permutation(nums,depth,n,used,curr,ans):
    if depth==n:
        ans.append(curr[:])
        return
    
    for i in range(0,len(nums)):
        if used[i]:
            continue
        used[i]=True
        curr.append(nums[i])
        permutation(nums,depth+1,n,used,curr,ans)
        curr.pop()
        used[i]=False

if __name__=="__main__":
    nums=[1,2,3]
    n=2
    used=[False]*3
    ans=[]
    permutation(nums,0,n,used,[],ans)
    print(ans)
