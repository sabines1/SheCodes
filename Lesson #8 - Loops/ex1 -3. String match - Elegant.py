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

    if len(a)> len(b):
        big = a
        small = b

        for k in range(len(small)):
            if small[k:(k + 2)] == big[k:(k + 2)] and ((k + 2) <= len(small)):
                count = count + 1
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

# a = 'abc'
# b = 'abc'

b = 'iaxxai'
a = 'aaxxaaxx'

print(string_match (a,b))