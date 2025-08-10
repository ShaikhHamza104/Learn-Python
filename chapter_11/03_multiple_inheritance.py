# creating ptt1 class for out of 20 marks 
class Ptt1:
    ptt1 = 0
    def get_marks_ptt1(self):
        self.ptt1 = int(input("Enter your ptt1 mark (Out of 20): "))

# creating ptt2 class for out of 20 marks
class Ptt2:
    ptt2 = 0
    def get_marks_ptt2(self):
        self.ptt2 = int(input("Enter your ptt2 mark (Out of 20): "))


# creating Microproject class for out of 10 marks
class Microproject:
    micro = 0
    def get_micro(self):
        self.micro = int(input("Enter your Microproject mark (Out of 10): "))

# creating Theory class for out of 10 marks
class Theory(Ptt1, Ptt2, Microproject):
    theory = 0

    def get_mark_theory(self):
        self.theory = int(input("Enter your Theory mark (Out of 70): "))
    
    def Calculate(self):
        ptt1 = self.ptt1
        ptt2 = self.ptt2
        micro = self.micro
        theory = self.theory

        # Calculate average of PTT marks and Micro marks normalized
        avg_of_ptt_micro = ((ptt1 + ptt2) / 40 * 30) + (micro / 10 * 20)

        # Calculate theory marks normalized to 50%
        avg_of_theory = (theory / 70) * 50

        # Final mark out of 100
        final_mark = avg_of_ptt_micro + avg_of_theory

        print(f"Your score is {final_mark:.2f}%")

# Create an instance of the Theory class and gather input
student = Theory()
student.get_marks_ptt1()
student.get_marks_ptt2()
student.get_micro()
student.get_mark_theory()
student.Calculate()