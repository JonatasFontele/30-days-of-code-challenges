class Person:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def print_person(self):
        # print("Name:", self.last_name + ",", self.first_name)
        # print("ID:", self.id_number)
        print(f"Name: {self.last_name}, {self.first_name}")
        print(f"ID: {self.id_number}")


class Student(Person):
    def __init__(self, first_name, last_name, id_number, scores):
        super().__init__(first_name, last_name, id_number)
        self.scores = scores

    def calculate(self):
        a = sum(self.scores) / len(self.scores)
        if 90 <= a <= 100:
            return "O"
        elif 80 <= a < 90:
            return "E"
        elif 70 <= a < 80:
            return "A"
        elif 55 <= a < 70:
            return "P"
        elif 40 <= a < 55:
            return "D"
        elif a < 40:
            return "T"


def main():
    first_name, last_name, id_num = input().split()
    num_scores = int(input())  # not needed for Python
    scores = list(map(int, input().split()))
    s = Student(first_name, last_name, id_num, scores)
    s.print_person()
    print("Grade:", s.calculate())


if __name__ == "__main__":
    main()
