
def two_sum(nums, target):

    if len(nums) < 2:
        return False
    
    nums.sort()

    i = 0
    j = len(nums)-1
    while i < j:
        if nums[i] + nums[j] == target:
            return True
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return False 

def wrapper():
    
    with open("test.txt", "r") as f:
        lines = f.readlines()

        print(lines)
        for line in lines:
            line = line.strip()

            problem = line.strip().split(" ")

            expected = problem[0] == "True"
            target = int(problem[1])
            n = int(problem[2])

            nums = []
            if n is not 0:
                nums = [int(x) for x in problem[3:]]

            real = two_sum(nums, target)       
            print("list = {}, target = {}, expected {}, real {}, passed: {}".format(nums, target, expected, real, expected == real))


if __name__ == '__main__':

    wrapper()

