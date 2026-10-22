###Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.  

amount=int(input("Enter amount:"))
n500=amount//500
amount=amount%500
n200=amount//200
amount=amount%200
n100=amount//100
amount=amount%100
n50=amount//50
amount=amount%50
n20=amount//20
amount=amount%20
n10=amount//10
amount=amount%10
n5=amount//5
amount=amount%5
n2=amount//2
amount=amount%2
n1=amount//1
amount=amount%1
print("Notes of 500:", n500)
print("Notes of 200:", n200)
print("Notes of 100:", n100)
print("Notes of 50:", n50)
print("Notes of 20:", n20)
print("Notes of 10:", n10)
print("Notes of 5:", n5)
print("Notes of 2:", n2)
print("Notes of 1:", n1)
total_notes=n500+n200+n100+n50+n20+n10+n5+n2+n1
print("Minimum number of notes:", total_notes)