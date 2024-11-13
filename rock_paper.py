import random
options = ["rock","paper","scissor"]
user = 0
robot =0
while (user<5) and (robot<5) :
    print("Lets play a game Rock Paper Scissor!!")
    try:
        user_choice = input("Please type your choice ")
        compute = options[random.randrange(0,3)]
        if (user_choice == "rock" and compute == "paper") or (user_choice == "paper" and compute == "scissor") or (user_choice == "scissor" and compute == "rock"):
            robot+=1
            print(f"Robot wins Score {user} : {robot} \n" )
        elif (compute == "rock" and user_choice == "paper") or (compute == "paper" and user_choice == "scissor") or (compute == "scissor" and user_choice == "rock"):
            user+=1
            print(f"You win Score :{user} : {robot} \n" )
        else:
            print(f"Draw!! score{user} : {robot} \n" )
    except Exception as f:
        print("Please select a valid option ",f )
        
if user> robot:
    print("YOU WINN")
else:
    print("YOU LOSE :(")