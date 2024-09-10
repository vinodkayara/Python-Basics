def sum_xor_diff(N,A):
    sum_odd=0
    xor_even=0
    for i in range(N):
        if i%2==0:
            xor_even^=A[i]
        else:
            sum_odd+=A[i]
        return sum_odd - xor_even
N=int(input())
A=list(map(int,input().split()))
result=sum_xor_diff(N,A)
print(result)