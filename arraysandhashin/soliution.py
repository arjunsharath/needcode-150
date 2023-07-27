def containsDuplicate1(self, nums):
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
        return False

print(containsDuplicate1([4,3,2,1,2]))