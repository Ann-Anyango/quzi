temprature=15
# boolen for if it's true or fale 
# conditions (if,if else, if elif  else,)
if temprature >30:
    print("it's  warm")
    
elif temprature >20:
    print("go to beach")
else:
     print ("the weatheris not well") 
print("done")
age =10
if age >=15:
    message="Child"
else:
    message="adults"
message="Child" if age >= 15 else "adults"       
print(message)
#logical operaters
#and ,or,not 
high=False
credit=True  
student=True
if not student:
    print("green")
# if high or credit:
    print("green")
else: 

    print("yellow")      

time = 19
 
if time == 9 :
   print("On time")
#  it will print coz it's right
if time > 9 and time <= 19:
   print("10 minutes late")
 
if time > 19 and time <= 39:
  print("30 minutes late")
 
if time > 39:
  print("Zero marks")
# loop condition
# for loop
# loop contains the Initialization,condition,incrimination
for i in range (10):
    # it counts the nmbers form the 0 to 9 butit does not include the number 10
    print (i)
    sum =0
    # it adds the sum of each i and gives out the out put
    for i in range(10):
        sum =sum+i
        print (sum)
        # this means that the for loop it used mostly in 
# 1. Print First 10 natural numbers using while loop
# i=1
# while i <=10:
#     print (i)
# i+=1
i = 1
while i <= 10:
    print(i)
    i += 1
    name=["Mercy","Nancy","Ann","Caro","Nicholas","Akinyi"]
first,second,third,*rest=name
print(first)
print(second)
print(*rest)
#sort()
number=[23,34,56,78,12,90]
number.sort()
print(number)
#
number.reverse()
print(number)
#
number.sort(reverse=True)
print(number)
myWork=[*range(30,40)]
print (myWork)
#deletes
del(number[0])
print(number)
#remove
number.remove(12)
print(number)
number2=set
def year_of_birth(name,age):
    year =2023-age
    print(f"Helo{name},you were born in{year}")
def my_country(country="Kenya"):
    print(f"Hello you are from{country}")
def hello(*names):
    for name in names :
        print(f"Hello {name}")
def sum (*nums):
    answer=0
    for num in nums:
     answer+=num

    
    return answer

 