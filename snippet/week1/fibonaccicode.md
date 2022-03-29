### <a href="https://alexd017.github.io/Tri3-IndivRepo/">Back</a>

### Code Snippet for fibonacci.py

    # Program to display the Fibonacci sequence up to n-th term
    n = int(input('How many terms? '))

    def fibonacci(n):
      a=0
      b=1
      fibList = [0]

      # check if the number of terms is valid
      if n <=0:
        print('Please enter a positive integer')
        fibonacci()
    
    # if there is only one term, return 
      elif n == 1:
        print(fibList)
        return

    # generate fibonacci sequence
      else:
        fibList.append(1)
        for i in range(2,n):
          c = a + b
          a = b
          b = c
          fibList.append(c)
      print(fibList)

    fibonacci(n)
