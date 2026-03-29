# val = {(1, 2), (1, 2),(3, 4)}
# set = set(val)
# print(set)

# developers = {"Alice", "Bob", "Charlie"}
# admins = {"Alice", "David"}

# # both = developers.intersection(admins)
# # print (both)
# developers.intersection_update(admins)
# print (developers)

# required_packages = ["python3", "pip", "requests", "boto3", "pip"]
# print(required_packages)
# print("requests" in required_packages)
# print("ansible" in required_packages)



name = input("enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

hobbies = input('Type your 3 hobbies, use "," after every hobbie: ').split(",") #? users should type "gaming,footbal,food" => ["gaming", "football", "food"]
pupolar_hobiz = [
    "fotball",
    "bass",
    "meet",
    
]
for H in hobbies:
    H = H.strip()
    if H in pupolar_hobiz:
        print("nice")
    else: 
        print("basa")

print (pupolar_hobiz)

tuple_hubbies = tuple(hobbies)

if "music" in hobbies:
    print ("good")
else: 
    print ("shabat shalom")
    
    
    print ([name] [age] [city] [hobbies] )