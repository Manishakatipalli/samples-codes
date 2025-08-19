
'''Currency Converter  
Write a program to convert an amount of money from one currency to another 
using fixed exchange rates. The user inputs the amount and selects the currencies 
for conversion'''

while True:
    s=input('do you want convert yes/no:')
    if(s=='no'):
      print("Goodbye!")
      break
    elif(s=='yes'):
        n = float(input("Enter the amount: "))
        print(n)
    else:
        print("Invalid input! Please enter a number.")
        continue
    s=input("enter source currency usd/inr/cad:").strip().lower()
    print(s)
    t=input("enter target currency usd/inr/cad:").strip().lower()
    print(t)
    if s == t:
        print(f"{n} {s} = {n:.2f} {t}")
    elif s=="usd" and t=="inr":
        print(f"{n} usd=={n*87.01:.2f}inr")
    elif s=="usd"and t=="cad":
        print(f"{n} usd={n*1.39:.2f}cad")
    elif s=="inr"and t=="usd":
        print(f"{n} inr=={n*0.01:.2f}usd")
    elif s=="inr"and t=="cad":
        print(f"{n} inr={n*0.015:.2f}cad")
    elif s=="cad" and t=="inr":
        print(f"{n} cad=={n*62.77:.2f}inr")
    elif s=="cad" and t=="usd":
        print(f"{n} cad=={n*62.77:.2f}usd")
    else:
        print("Invalid currency")
    
   

