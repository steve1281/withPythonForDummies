__author__ = 'steve1281'

def find_missing(ip):
    """
    list of n integers ... range 1 to n+1
    no duplicates
    what is the quickest way to find the missing integer?

    Assume: lowest int will be 1.
            No duplicates.
            Only one missing
    """

    n = len(ip)
    print(ip)
    a = []

    # init  - two greater than the input list
    #         there is one missing and we need to ignore 0
    for i in range(n+2):
        a.append(-1)

    # scan
    for i in range(n):
        a[ip[i]] = 1

    # locate missing integers
    for i in range(1,n+1):
        if (a[i] == -1):
            print('missing entry', i)

    return

find_missing([1,2,3,4,6,5,7,8])


