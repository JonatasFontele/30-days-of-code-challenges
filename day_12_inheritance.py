class Person:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def print_person(self):
        print("Name:", self.last_name + ",", self.first_name)
        print("ID:", self.id_number)
        # print(f"O {self.__nome} está comendo")


class Student(Person):
    def __init__(self, first_name, last_name, id_number, scores):
        super().__init__(first_name, last_name, id_number)
        self.scores = scores

    def calculate(self):
        return sum(scores) / len(scores)

# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here


#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here


def main():
    first_name, last_name, id_num = input().split()
    num_scores = int(input())  # not needed for Python
    scores = list(map(int, input().split()))
    s = Student(first_name, last_name, id_num, scores)
    s.print_person()
    print("Grade:", s.calculate())


if __name__ == "__main__":
    main()
