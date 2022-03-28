def lcm(num1, num2): # imperative
  if (num1 > num2):
    max = num1
  else:
    max = num2
  while (True):
      if (max % num1 == 0 and max % num2 == 0):
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
			print("The LCM of 12 and 30 is ", lcm(12,30))
		elif num == 'o':
			lcmoop = LCM(12,30)
			print("The LCM of 12 and 30 is ", lcmoop())
	except:
		print("that was not an option u old swine")


if __name__ == "__main__":
    run() 