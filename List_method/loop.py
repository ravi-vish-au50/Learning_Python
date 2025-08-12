fruits = ["Apple", "Banana", "Cherry", "Date", ]

# for x in fruits :
#     print (x)

for x in fruits:
    print(x)
    if x == "Cherry":
         break
    
    for x in fruits:
         print(x)
         if x == "cherry" :
             continue 
    print(x)



    # While loop

    num =0
    while  num <11:
         print(num)
         num+=1
    num = 1
    while num < 6:
              print(num)
              if num == 9:
                   break
              num +=1
              

    num = 0
    while num < 20:       
     num += 1
    if num == 15:
       continue
print(num)
             
            #   t