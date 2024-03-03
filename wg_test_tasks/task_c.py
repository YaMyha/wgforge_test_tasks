def lis(nums, return_indexes=False):
    nums_length = len(nums)
    if nums_length < 2:
        return 1

    lis_length = -1

    subsequence = [float('inf')] * nums_length
    indexes = [float('inf')] * nums_length

    subsequence[0] = nums[0]
    indexes[0] = 0

    def ceil_index_func(subseq, start_left, start_right, key):
        left, right = start_left, start_right
        mid = ceil_index = 0
        ceil_index_found = False

        while left <= right and not ceil_index_found:
            mid = (left + right) // 2

            if subseq[mid] > key:
                right = mid - 1
            elif subseq[mid] == key:
                ceil_index = mid
                ceil_index_found = True
            elif mid + 1 <= right and subseq[mid + 1] >= key:
                subseq[mid + 1] = key
                ceil_index = mid + 1
                ceil_index_found = True
            else:
                left = mid + 1

        if not ceil_index_found:
            if mid == left:
                subseq[mid] = key
                ceil_index = mid
            else:
                subseq[mid + 1] = key
                ceil_index = mid + 1

        return ceil_index

    for i in range(1, len(nums)):
        indexes[i] = ceil_index_func(subsequence, 0, i, nums[i])

        if lis_length < indexes[i]:
            lis_length = indexes[i]
    if return_indexes:
        return lis_length + 1, indexes
    return lis_length + 1

def start():
    n = int(input())
    if n == 1:
        int(input())
        print("1 1")
    else:
        numbers = list(map(int, input().split()))
        result, indexes = lis(numbers, True)

        max_prem_length = -1
        division_indexes = [-1, 0]
        division_indexes.extend([j for j in range(1, n) if numbers[j - 1] > numbers[j]])
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
