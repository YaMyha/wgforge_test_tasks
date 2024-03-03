def lis(nums):
    if not nums:
        return 0

    n = len(nums)
    ans = [nums[0]]
    max_len_limit = max(nums) + 1 - min(nums)

    for i in range(1, n):
        if nums[i] > ans[-1]:
            ans.append(nums[i])
            temp_len = len(ans)
            if temp_len >= max_len_limit:
                return temp_len
        else:
            low = 0
            high = len(ans) - 1
            while low < high:
                mid = low + (high - low) // 2
                if ans[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid
            ans[low] = nums[i]
    return len(ans)


def start():
    n = int(input())
    if n == 1:
        int(input())
        print("1 1")
    else:
        numbers = list(map(int, input().split()))
        max_len_limit = max(numbers) - min(numbers) + 1
        result = lis(numbers)

        max_prem_length = -1
        division_indexes = [-1, 0]
        division_indexes.extend([j for j in range(1, n) if numbers[j - 1] > numbers[j]])

        if n >= 2 * max_len_limit:
            prem_max_len_limit = 2 * max_len_limit
            for index in division_indexes:
                if index == -1:
                    prem_length = 1 + lis(numbers[:-1])
                elif index == 0:
                    prem_length = 1 + lis(numbers[1:])
                else:
                    prem_length = lis(numbers[:index]) + lis(numbers[index:])
                if max_prem_length < prem_length:
                    max_prem_length = prem_length
                    if max_prem_length >= prem_max_len_limit:
                        break
        else:
            for index in division_indexes:
                if index == -1:
                    prem_length = 1 + lis(numbers[:-1])
                elif index == 0:
                    prem_length = 1 + lis(numbers[1:])
                else:
                    prem_length = lis(numbers[:index]) + lis(numbers[index:])
                if max_prem_length < prem_length:
                    max_prem_length = prem_length
        print(f"{result} {max_prem_length}")


start()
