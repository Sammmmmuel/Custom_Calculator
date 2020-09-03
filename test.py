#Title to introduce 
print("Want to know how many secods are in how ever many days?")
#First question
print("Insert a number below !")
#asking the user to input the number of days they want answer 
time=input("days:")
#here i am turning the value received into an integer 
time=int(time)
#asking the user to try and guess how many seconds 
input("can you guess how many ?")
#there is a really small chance they will get it right so i just assumed and said they were wrong 
print("wrong!")
#here is where i use the value that i turned into and integer
#to multiply by 86400 because thats how many seconds there are in a day.
#and i put that and the days into an f string to give the answer to the user. 
print(f"there are {(int(time)* 86400)} secods in {time} days")