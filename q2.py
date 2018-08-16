my_List= [ ['Ali', 'Male'], ['Maha', 'Female'], ['Laith','Male'], ['Lamiaa', 'Female'], ['Zainab', 'Female'], ['Lena','Female'], ['Hanan', 'Female'] ]
name = input("Enter the name")
for i , j in my_List:
    if name in i:
     print(j)