def counting_sort(A, k):
    """
    Counting sort in linear time. When k = O(n), the running time is O(n+k)
    :param A: The array to be sorted
    :param k: The maximum value of A
    :return: A sorted list
    """
    """
    e.g.: A = [2,5,3,0,2,3,0,3]
    C contains the number of elements equals to i
    C = [2, 0, 2, 3, 0, 1]
    C[0] = 2 means A has 2 elements = 0
    C[5] = 1 means A has 1 element = 5
    Time: O(k)+O(n)
    """

    C = [0] * (k+1)
    for i in A:
        C[i] += 1
    
    """
    C contains number of elements smaller or equal to i
    C = [2, 2, 4, 7, 7, 8]
    C[2] = 4 means A has 4 elements <= 2
    C[5] = 8 means A has 8 elements <= 5
    Time O(k)
    """
    for i in range(1, k+1):
        C[i] += C[i-1]
    
    """
    Start from the last element A[7] = 3.
    C[3] = 7 means there are 7 elements smaller or equal to 3 in A
    so B[7] = 3
    Update C[3] = C[3] - 1, now 6 elements are smaller or equal to 3.
    Time O(n)
    """
    n = len(A)
    B = [None] * n
    for i in range(n-1, 0-1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    
    return B    


if __name__=="__main__":
    l = [2,5,3,0,2,3,0,3]
    print counting_sort(l, 5)
    print counting_sort(l, 5) == sorted(l)