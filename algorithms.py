def linear_search(S, x):
    for i in range(len(S)):  # keep going through array until x found
        if S[i] == x:  # return True if value x in the array is found
            return True
    return False  # value x not in array


def binary_search(S, x):
    # merge.merge_sort(S) #sort the list before starting binary search

    start = 0  # index at beginning of array
    end = len(S) - 1  # index at end of array

    while S[start] < S[end]:
        mid = (start + end) // 2
        if S[mid] == x:  # return True if value x in the array is found
            return True
        elif S[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return False  # value x not in array


# sorts a list in O(nlogn) time
def merge_sort(S):
    # if list is long enough to be sorted
    if len(S) > 1:
        left = S[:len(S) // 2]
        right = S[len(S) // 2:]

        # recursive call
        merge_sort(left)
        merge_sort(right)

        i = 0  # index of left array
        j = 0  # index of right array
        k = 0  # index of merged array

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                S[k] = left[i]
                i += 1
            else:
                S[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            S[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            S[k] = right[j]
            j += 1
            k += 1
