from random import sample
nums = sample(range(100), 8)
print("nums:", nums)


def binary_search(nums, niddle):
    '''
    二分查找，适用于有序序列
    '''
    if len(nums) == 0:
        return -1

    low, high = 0, len(nums) - 1

    while low + 1 < high:
        mid = low + (high - low) // 2
        if niddle == nums[mid]:
            high = mid
        elif niddle < nums[mid]:
            high = mid
        else:
            low = mid
    if nums[low] == niddle:
        return low
    if nums[high] == niddle:
        return high
    return -1


print('BS: ', binary_search([1, 3, 4, 6, 9, 12], 6))

####----------sort algorithms-----------


def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print("bs:", bubble_sort(nums))

####--------------------------------------####


def quick_sort1(nums):
    if len(nums) < 2:
        return nums  #基线条件：为空或只包含一个元素的数组是“有序”的
    else:
        pivot = nums[0]  #递归条件
        less = [i for i in nums[1:] if i <= pivot]
        #-由所有小于基准值的元素组成的子数组
        greater = [i for i in nums[1:] if i > pivot]
        #由所有大于基准值的元素组成的子数组

    return quick_sort1(less) + [pivot] + quick_sort1(greater)


print("qs:", quick_sort1(nums))


####--------------------------------------####
def quicksort(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        quicksort(lst, lo, p)
        quicksort(lst, p + 1, hi)
    return


def partition(lst, lo, hi):
    pivot = lst[hi - 1]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[hi - 1] < lst[i + 1]:
        lst[i + 1], lst[hi - 1] = lst[hi - 1], lst[i + 1]
    return i + 1


####--------------------------------------####
def InsertSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(1, n):
        j = i
        target = lst[i]  #每次循环的一个待插入的数
        while j > 0 and target < lst[j - 1]:  #比较、后移，给target腾位置
            lst[j] = lst[j - 1]
            j = j - 1
        lst[j] = target  #把target插到空位
    return lst


print("is:", InsertSort(nums))


####--------------------------------------####
def ShellSort(lst):
    def shellinsert(arr, d):
        n = len(arr)
        for i in range(d, n):
            j = i - d
            temp = arr[i]  #记录要出入的数
            while (j >= 0 and arr[j] > temp):  #从后向前，找打比其小的数的位置
                arr[j + d] = arr[j]  #向后挪动
                j -= d
            if j != i - d:
                arr[j + d] = temp

    n = len(lst)
    if n <= 1:
        return lst
    d = n // 2
    while d >= 1:
        shellinsert(lst, d)
        d = d // 2
    return lst


print("ss:", ShellSort(nums))


####--------------------------------------####
def HeapSort(lst):
    def heapadjust(arr, start, end):  #将以start为根节点的堆调整为大顶堆
        temp = arr[start]
        son = 2 * start + 1
        while son <= end:
            if son < end and arr[son] < arr[son + 1]:  #找出左右孩子节点较大的
                son += 1
            if temp >= arr[son]:  #判断是否为大顶堆
                break
            arr[start] = arr[son]  #子节点上移
            start = son  #继续向下比较
            son = 2 * son + 1
        arr[start] = temp  #将原堆顶插入正确位置


#######

    n = len(lst)
    if n <= 1:
        return lst
    #建立大顶堆
    root = n // 2 - 1  #最后一个非叶节点（完全二叉树中）
    while (root >= 0):
        heapadjust(lst, root, n - 1)
        root -= 1
    #掐掉堆顶后调整堆
    i = n - 1
    while (i >= 0):
        (lst[0], lst[i]) = (lst[i], lst[0])  #将大顶堆堆顶数放到最后
        heapadjust(lst, 0, i - 1)  #调整剩余数组成的堆
        i -= 1
    return lst
print("hs:", HeapSort(nums))


####--------------------------------------####
def MergeSort(lst):
    #合并左右子序列函数
    def merge(arr, left, mid, right):
        temp = []  #中间数组
        i = left  #左段子序列起始
        j = mid + 1  #右段子序列起始
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        for i in range(left, right + 1):  #  !注意这里，不能直接arr=temp,他俩大小都不一定一样
            arr[i] = temp[i - left]

    #递归调用归并排序
    def mSort(arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        mSort(arr, left, mid)
        mSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

    n = len(lst)
    if n <= 1:
        return lst
    mSort(lst, 0, n - 1)
    return lst


print("ms:", MergeSort(nums))

####--------------------------------------####
