 import random
def Generate_password(length):
    lower_case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    digits=['0','1','2','3','4','5','6','7','8','9']
    special_characters=['!','@','#','$','%','^','&','*','(',')']
    password_variable=lower_case+upper_case+digits+special_characters
    password=''.join(random.choice(password_variable)for _ in range(length))
    return password
password=Generate_password(12)
print("password ",password)
