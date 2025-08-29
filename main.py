class Student:
    def __init__(self, ism, baxo):
        self.ism = ism
        self.baxo = baxo

    def ortabaho(self):
        return sum(self.baxo) / len(self.baxo)

class Teacher:
    def __init__(self, ism, fan):
        self.ism = ism
        self.fan = fan

    def talaba_baxosi(self, oquvci):
        print(f"{oquvci.ism} ortacha bahosi:", oquvci.ortabaho())
        
talaba1 = Student("vali", [5, 4, 5])
ustoz = Teacher("ali", "informatika")
ustoz.talaba_baxosi(talaba1)
