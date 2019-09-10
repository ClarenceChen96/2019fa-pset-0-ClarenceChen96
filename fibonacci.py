#!/usr/bin/env python3

def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    return int(str(some_int)[-8:])


def optimized_fibonacci(f):
    #covering edge cases when f = 0 or 1
    if (f==0):
        return 0
    elif(f==1):
        return 1
    else:
        #initializing the first elements
        a=0
        b=1
        #loop to calculate the next element
        for i in range(f-1):
            a,b=b,a+b
        return b


class SummableSequence(object):
    def __init__(self, *initial):
        # initialize instance variable as below
        self.backup = initial



    def __call__(self, i):
        #re-initialize the list
        self.init=[]
        for x in range(len(self.backup)):
            self.init.append(self.backup[x])
        #covering the edge cases where i<n
        if (i < len(self.init)):
            return (self.init[i])
        else:
            #loop to get result
            for j in range(i + 1 - len(self.init)):
                temp = 0
                for m in range(len(self.init)):
                    temp += self.init[m]
                for m in range(len(self.init) - 1):
                    self.init[m] = self.init[m + 1]
                self.init[len(self.init) - 1] = temp
            return self.init[len(self.init) - 1]






if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))

