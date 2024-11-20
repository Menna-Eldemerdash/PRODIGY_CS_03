# import re
# def check_password(password):
#     strength=0
#     feedback=[]

#     if len(password)>=8:     
#         strength+=1
#     else:
#         feedback.append("Password is too short, it should be at least 8 characters long.")

#     if re.search(r"[A-Z]",password):         
#         strength +=1
#     else:
#         feedback.append("Password should contain at least one uppercase letter.")

#     if re.search(r"[a-z]",password):
#         strength +=1
#     else:
#         feedback.append("Password should contain at least one lowercase letter.")

#     if re.search(r"[0-9]",password):
#         strength +=1
#     else:
#         feedback.append("Password should contain at least one number.")

#     if re.search(r"[^A-Za-z0-9]",password):
#         strength+=1
#     else:
#         feedback.append("Password should contain at least one special character (@, #, $).")
    
        
#     return strength,feedback
# while True:
#     password = input("Enter your Password: ")
#     strength, feedback = check_password(password)
    
#     if strength == 5:
#         print("Password is very strong")
#         break
#     elif strength >= 3:
#         print("Password is moderate. Try to make it stronger.")
#     else:
#         print("Password is very weak. You should improve it.")
    
#     print("Password strength:", strength)
#     for msg in feedback:
#         print(msg)
#     print("\nPlease try again.\n")  
def pp(*nums):
    result=nums[0]
    for num in nums:
        if num<result:
            result=num
    return result
pp(2,3,4,5,6,8)

