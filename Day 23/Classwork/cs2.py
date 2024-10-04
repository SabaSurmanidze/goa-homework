list = [8,4,2,6]
list.remove(2)
print((len(list))+list.count(6))

# answer = 4 ლისტიდან ამოიშალა ციფრი 2 შემდეგ ლენს ანუ ციფრების
#  რაოდენობას დაემატა 1 რადგან 6 იყო მხოლოდ ერთი და 3 დაემატა ერთი და გამოვიდა 4

nums = [2,4,8,9,5]
nums.insert(1,3)
nums.remove(9)
nums.insert(0,nums.count(8))
print(nums[3])
# answer = 4 ცვლადში ჩაემდატა
#  პირველ ადგილას ციფრი 3 შემდეგ წაიშალა 9 და დათვალა რამდენი 
# იყო 8 ცვლადში და გადაიტანა 0 ადგილას შემდეგ დაპრინტა მესამე ციფრი და მესამე იყო 4


queue = ["john","amy","bob","adam"]
user = str(input("enter your name:"))
queue.append(user)
print(queue)


