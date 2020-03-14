# k = int(input())
# nums = list(input())
import time

start = time.time()
count = 0
choose = input('Как решить программу?\n'
               '1. Рекурсивно.\n'
               '2. Итеративно\n')


def SearchBin_Rec(k, nums, count):
    if len(nums) == 1 and k == nums[0]:      # If there is only one element remain and it coincide with required number.
        print("Program running time: " + str(time.time() - start))
        return count + 1
    elif len(nums) == 1 and k != nums[0]:    # If it dont coincide with required number.
        print("Program running time: " + str(time.time() - start))
        return None
    if k >= nums[len(nums) // 2]:            # Right side if the number is greater than the number in the middle.
        count += int(len(nums) / 2)          # Plus len of left part, if k in right part.
        return SearchBin_Rec(k, nums[int((len(nums)) / 2):len(nums) + 1], count)
    elif k < int(nums[int(len(nums) / 2)]):  # Left side if the number is greater than the number in the middle.
        return SearchBin_Rec(k, nums[:int(len(nums) / 2)], count)


def SearchBin_Iterative(k, nums, count):
    while len(nums) > 1:
        if k >= nums[len(nums) // 2]:     # Right side if the number is greater than the number in the middle.
            nums = nums[len(nums) // 2:]  # Plus len of left part, if k in right part.
            count += int(len(nums) / 2)
        else:                             # Left side if the number is greater than the number in the middle.
            nums = nums[:len(nums) // 2]
    if nums[0] == k:                       # If there is only one element remain and it coincide with required number.
        print("Program running time: " + str(time.time() - start))
        print(k)
    else:                                  # If it dont coincide with required number.
        print('None')
        print("Program running time: " + str(time.time() - start))


if choose == '1':
    print(SearchBin_Rec(100,
                        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                         27, 28, 29, 30, 31, 32, 33,
                         34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
                         58, 59, 60, 61, 62, 63,
                         64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87,
                         88, 89, 90, 91, 92, 93,
                         94, 95, 96, 97, 98, 99, 100], count))
elif choose == '2':
    SearchBin_Iterative(100,
                        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                         27, 28, 29, 30, 31, 32, 33,
                         34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
                         58, 59, 60, 61, 62, 63,
                         64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87,
                         88, 89, 90, 91, 92, 93,
                         94, 95, 96, 97, 98, 99, 100], count)