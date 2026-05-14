#str= "Codingal"
#for i in str:
 #   print(i)


#for i in range(1, 10):
 #   print(i)

#i=1
#while (i < 6):
 #print(i)
 #i=i+1

# for i in range(1, 5):
#     for j in range(i):
#         print("*", end=" ")
#     print()
        

num = int(input("Enter a number: "))

if num > 1:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is NOT a Prime Number")

else:
    print(num, "is NOT a Prime Number")


