for i in range(1, 101):
    print(i)

    if i%3 and i%5==0:
      print("fizzbuzz")
    elif  i%5==0:
      print("buzz")
    elif i%3==0:
      print("fizz")
