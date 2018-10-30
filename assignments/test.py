# variable = 0.0
# while variable != 0.3:
#     variable += 0.1
#     print(variable)
import pandas_datareader.data as web
# #
# # print(float(3)/5)
# #
# # elems = ['a', 'b', 'c', 'a', 'b', 'c']
# # for e in elems:
# #     print (e)
# #     elems.remove(e)
# symbol = '5_Industry_Portfolios'
#
# # elems_copy = elems[:]
# # for item in elems_copy:
# #     if not condition:
# #         elems.remove(item)
# #
# # def get_data(stock):
# #     # start = dt.datetime(2000,1,1)
# #     # end = dt.datetime(2017,12,31)
# #     # df= web.DataReader(stock,'google',start,end)
# #     df= web.DataReader(stock,'robinhood')
# #     return df
# #
# #
# # df= web.DataReader('APPL','quandl')
# # #
# # df = web.DataReader(symbol, 'famafrench', '2015-01-01', '2018-01-05')
# # # df/
# # print(df)
# from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
# symbols = get_nasdaq_symbols()
# print(symbols.ix['IBM'])

# Python Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 21

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")