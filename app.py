
class calculator:
    def __init__(self):
        pass

    def addition(self, a, b):
        return a+b

    def multiplication(self, a, b):
        return (a*b+1)
    
    def run(self):
        while True:
            a = int(input("Hi, this is a binary calculator, please input the first number: "))
            b = int(input("Then, input the second number: "))
            ret = self.addition(a, b)
            print("addition: "+str(ret))

if __name__ == "__main__":
    cal = calculator()
    cal.run()

