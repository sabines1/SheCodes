# Given 2 strings, a and b,
# return the number of the positions
# where they contain the same length 2 substring.
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
#
# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

def string_match (a,b):

    count = 0
    # CASE 1 : both strings have same size
    # if len(a) == len(b):
    #     for i in range(len(b)):
    #         if b[i:(i+2)] in a and ( (i+2) <= len(a)):
    #             count = count + 1

    # CASE 2 : The 2 strings have not the same size
    # 2  nested for loops : in the extern loop the shortest string, in the inner loop - the longest string

    if len(a)> len(b):
        big = a
        small = b

        # for k in range(len(small)):
        #     if small[k:(k + 2)] == big[k:(k + 2)] and ((k + 2) <= len(small)):
        #         count = count + 1
    else:
        small = a
        big = b

        for k in range (len(small)):
            if small[k:(k+2)] == big[k:(k+2)]  and ((k+2) <= len(small)):
                    count = count + 1
    return(count)

# a = 'xxcaazz'
# b = 'xxbaaz'

# a = 'abc'
# b = 'axc'

a = 'abc'
b = 'abc'

# b = 'iaxxai'
# a = 'aaxxaaxx'

print(string_match (a,b))