import random
class Main:
    
    #====================GuessNumber function====================
    def GuessNumber(self, number):
        a = 0
        b = int(number)
        guess = random.randint(a, b)
        while True:
            response = input(f"Is {guess} your number? (Enter '1' if too low, 'h' if too high, 'c' if correct): ")
            if response == 'c' :
                print(f"Welldone! The computer guessed your number {guess} correctly!")
                break
            elif response == '1':
                a = guess + 1
            elif response == 'h':
                b = guess - 1
            guess = random.randint(a, b)
        pass
        # end def

#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        number = input("Enter a range for guessed number: ")
        print("OUTPUT")
        self.GuessNumber(number)
        print("FINISH")
main = Main()
main.main()
