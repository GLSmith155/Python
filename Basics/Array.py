 # Unlike c based languages, a for loop's variable is each value in an array of ints. Wheras in c it's 0,1,2,3.. and so on. 
 # nums[0] still works, but isn't how for loops are set. The first i is equal to nums[0] rather than being set to 0 like you would in Java/C++.

nums = [5,4,3,2,1]
    
    # Enumerate
for a, b in enumerate(nums):
    print("this is a: ", a)
    print("this is b: ", b)
    # a iterates through the range of nums (1 and on)   
    # b iterates through each value
    
print("Break") 

    # Normal For-loop
for i in nums:
    print("this is the value: ", i)
    
print("Break")

x = len(nums)
print("this is how many values are in the array nums: ", x)

print("Break")

for i in range(len(nums)):
    print("this is the index # of values in the array: ", i)
