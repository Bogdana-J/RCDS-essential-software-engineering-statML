def pivot_sort(arr):
    """
    Sorts a list in ascending order using the pivot sort (similar to quicksort) algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new list with the elements sorted in ascending order.

    Example:
        >>> pivot_sort([34, 7, 23, 32, 5, 62])
        [5, 7, 23, 32, 34, 62]
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return pivot_sort(less_than_pivot) + [pivot] + pivot_sort(greater_than_pivot)

# Example usage
if __name__ == "__main__":
    sample_list = [34, 7, 23, 32, 5, 62]
    sorted_list = pivot_sort(sample_list)
    print("Sorted list:", sorted_list)