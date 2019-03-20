#############################
#### FUNCTION EXERCISES #####
#############################

###############
## Problem 1 ##
###############

# Given the string:


# ใช้ indexing เพื่อ print out ให้ได้ผลดังต่อไปนี้:
# 'd'
def main():
    s = 'django'
    print(s[0])
# 'o'
    print(s[-1])
# 'djan'
    print(s[:4])
# 'jan'
    print(s[1:4])
# 'go'
    print(s[4:])
# Bonus: ลองใช้ index จากท้าย


###############
## Problem 2 ##
###############

# Given this nested list:
l = [3, 7, [1, 4, 'hello']]

# จงแก้ค่า hello เป็น goodbye

l[2][2] = 'goodbye'
print(l[2][2])

###############
## Problem 3 ##
###############

# จง print out ค่า hello ออกมาจาก dicitionry ด้านล่าง:

d1 = {'simple_key': 'hello'}
print('d1 = '+d1['simple_key'])

d2 = {'k1': {'k2': 'hello'}}
print('d2 = '+d2['k1']['k2'])

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print('d3 = '+d3['k1'][0]['nest_key'][1][0])
main()

#####################
## -- PROBLEM 4 -- ##
#####################

# เขียนฟังก์ชั่นที่รับ list ของเลข integer โดยจะ return True ถ้ามี list ของเลข 1, 2, 3 อยู่ใน list ที่รับเข้ามา

# For example:


def arrayCheck(nums):
    for index in range(len(nums)-2):
        if nums[index] == 1 and nums[index+1] == 2 and nums[index+2] == 3:
            return True
        else:
            return False
print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))

   #####################
   ## -- PROBLEM 5 -- ##
   #####################

   # เขียนฟังก์ชั่นที่รับ string เข้ามา แล้ว return string ที่แสดงตัวอักษร ตัว-เว้น-ตัว จาก string ที่รับเข้ามา

   # For example:

   # stringBits('Hello') → 'Hlo'
   # stringBits('Hi') → 'H'
   # stringBits('Heeololeo') → 'Hello'

def stringBits(str):
    for x in str:
      print(x, end='')


print(stringBits('A'))
    #####################
    ## -- PROBLEM 6 -- ##
    #####################

    # จง return จำนวนเลขคู่ใน list ที่ส่งเข้ามาในฟังก์ชั่น
    #
    # Examples:
    #
    # count_evens([2, 1, 2, 3, 4]) → 3
    # count_evens([2, 2, 0]) → 3
    # count_evens([1, 3, 5]) → 0

    # def count_evens(nums):
    # CODE GOES HERE
