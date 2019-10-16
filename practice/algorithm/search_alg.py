def binary_search(nums,niddle):
    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low+high)//2
        if niddle == nums[mid]:
            return mid
        elif niddle < nums[mid]:
            high = mid-1
        else:
            low = mid+1
    else:
        return None

#print(binary_search([1,3,4,6,9,12],6))