def freq(nums):
    mp = {}
    for i in set(nums):
        x=nums.count(i)
        try:
            mp[x].append(i)
        except:
            mp[x]=[i]
    ans=[]

    for i in sorted(mp):
        for j in sorted(mp[i]):
            ans.extend([j]*i)
    sol=[]
    for i in ans:
        if sol==[] or sol[-1]!=i:
            sol.append(i)
            
    return sol
s=input()
nums = input().split(" ")
num =[int(i) for i in nums]
print(*freq(num))
