### Code Snippet for LCM
    def lcm(num1, num2):  # imperative
        if (num1 > num2):
            max = num1
        else:
            max = num2
        while True:
            if max % num1 == 0 and max % num2 == 0:
                break
            max = max + 1
        return max
    class LCM:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2
      def __call__(self):
          if self.num1 > self.num2:
              max = self.num1
          else:
              max = self.num2
          while (True):
              if (max % self.num1 == 0 and max % self.num2 == 0):
                  break
              max = max + 1
          return max
    def run():
        num = input("imperative(i) or OOP(o)")
        try:
            if num == 'i':
                print("The LCM of 9 and 6 is ", lcm(9, 6))
            elif num == 'o':
                lcmoop = LCM(9, 6)
                print("The LCM of 9 and 6 is ", lcmoop())
        except:
            print("Error! Please select imperative or OOP!")
    if __name__ == "__main__":
        run()
