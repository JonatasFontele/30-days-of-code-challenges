class Person:
    def __init__(self, initial_age):
        # Instance variable
        if initial_age >= 0:
            self.age = initial_age
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")

    def year_passes(self):
        self.age += 1

    def am_i_old(self):
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")


def main():
    t = int(input())
    for i in range(t):
        age = int(input())
        p = Person(age)
        p.am_i_old()
        for j in range(3):
            p.year_passes()
        p.am_i_old()
        print("")


if __name__ == "__main__":
    main()
