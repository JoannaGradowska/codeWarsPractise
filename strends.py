# Complete the solution so that it returns
# true if the first argument(string) passed
# in ends with the 2nd argument (also a string).
def solution(string, ending):
    if ending == '':
        return True
    if string[len(ending) - 1:] == ending:

        return True
    else:
        return False
