#Fiseha's' game
print("score counter machine" )
print("Name of game:" " " "Fisho game")
name = str.capitalize(input("Your nickname \n"))
while True:
    round1 = int(input("round_1 score \n"))
    round2 = int(input("round_2 score \n"))
    round3 = int(input("round_3 score \n"))

    if round1 == round2 == round3:
        print("Insert three different numbers, please!")
        continue  # Restart the loop to get new inputs
    else:
        break  # Exit the loop if the numbers are different

total_round = round1 + round2 + round3
final_result = total_round / 3
print(final_result)
count = 0
if final_result > round1:
      count +=1
if final_result > round2:
      count +=1
if final_result > round3:
      count +=1
if count >=2:
      print( "congratulations 👏" " "+ name + " " "you are the winner 🏆")
      print("keep up" " "+ name)
else:
      print("It's is okay" " " +name + " " "you are lost😞" " " + "Try again. \n")
      print("come solid in the next tournament!")