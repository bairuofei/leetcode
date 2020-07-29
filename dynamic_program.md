# Notes for Dynamic Programming

## 62 Unique Paths
- 思路一，使用组合数求解所有的可能
- 思路二，使用动态规划

## 53 最大子序和

dp求解最大子序和问题

dp[0]=0

- 如果dp[i]的含义是终点为num[i]的子序的最大和，则状态转移方程为：

dp[i]=max(dp[i-1]+num[i],num[i])  注意这种情况下最后还要对所有的dp[i]取最大值

- 如果含义是到num[i]为止，所见到的最大子序和，则状态转移方程为：

dp[i]=max(dp[i-1],num[i],dp[i-1]+num[i])