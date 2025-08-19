import random 
while True:
  computer=random.choice(('r', 'p', 's'))
  print("Computer chose:", computer)
  me=input("enter Rock as r, Paper as p, Scissors as s:").lower()
  print("you chose:",me)
  if computer==me:
    print("Its a tie")
  elif(computer == "r" and me == "p") or (computer == "p" and me == "s") or (computer == "s" and me == "r"):
    print("you win")
  else:
    print("you lose")
    n=(input(" do you want to continue y/n")) 
    if n=='y':
      print("Computer chose:", computer) 
    else: 
        print("Thanks for playing!")
        break
