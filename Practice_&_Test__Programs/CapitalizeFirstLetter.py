def solve(s):
    arr = list(s)
    arr[0] = arr[0].upper()
    for i in range(0, len(arr)):
        if arr[i] == ' ':
            arr[i+1] = arr[i+1].upper()
    print(''.join(arr))
solve('aditya saxena')

