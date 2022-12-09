a=int(input("Enter The 1st Side of the Traingle: "))
b=int(input("Enter The 2st Side of the Traingle: "))
c=int(input("Enter The 3st Side of the Traingle: "))
if(a==b==c):
    print("The Traingle is Equilateral Traingle.")
elif(a!=b!=c):
    print("The Traingle is Scalane Traingle.")
else:
    print("The Traingle is Isoceles Traingle.")
