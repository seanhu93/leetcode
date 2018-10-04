




# given a list of numbers from 1 to n, each number is only appeared once,
# except only one number is appeared twice, only one number is not shown 
# in the list,
# given the list, find the duplicated number, use O(1) space

def circle(nums):
    n = len(nums)
    if n < 2:
        return -1

    for x in range(len(nums)):
        if x + 1 == nums[x]:
            continue
        
        i = j = x
        while True:
            i = nums[i] - 1
            j = nums[nums[j] - 1] - 1
            if i == j:
                break

        if i == x:
            continue

        q = x
        while True:
            q = nums[q] - 1
            i = nums[i] - 1
            if q == i:
                return q + 1

def wrapper():

    import random
    # {length} {duplicated number}
    with open("test.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
       
        for line in lines:
            l = line.split(" ")
            n = int(l[0])
            x = int(l[1])


            nums = []
            if n == 1:
                nums = [1]
            if n > 1:
                nums = list(range(1, n+1))
                pick = x
                while pick == x:
                    pick = random.randint(1, n)
                nums[pick-1] = x
                random.shuffle(nums) 

            real = circle(nums)  
            print("list = {}, expected {}, real {}, passed: {}".format(nums, x, real, x == real))


if __name__ == '__main__':
    wrapper()

