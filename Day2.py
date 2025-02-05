from collections import defaultdict


def count_special_subarrays(A, N):
    prefixXOR = 0
    prefixSum = 0
    count = 0
    diff_count = defaultdict(int)


    diff_count[0] = 1

    for i in range(N):
        prefixXOR ^= A[i]
        prefixSum += A[i]

        diff = prefixXOR - prefixSum
        count += diff_count[diff]

        diff_count[diff] += 1

    return count



T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(count_special_subarrays(A, N))
