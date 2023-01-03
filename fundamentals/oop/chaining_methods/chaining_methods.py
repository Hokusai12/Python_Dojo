class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print("Membership Status: ", "Enrolled" if self.is_rewards_member else "Unenrolled")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member:
            print("User is already a member!")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Unfortunately, you don't have enough points to spend. Try and get some more!")
        else:
            self.gold_card_points -= amount
        return self

user3 = User("Kiki", "Ding", "kiki.ding@gmail.com", "2")
user2 = User("First", "Last", "first_last@gmail.com", 13)
user1 = User("H.H", "Holmes", "h.h.holmes@gmail.com", 32)

user1.enroll().spend_points(50)
user2.enroll().spend_points(80)

user1.display_info()
user2.display_info()
user3.display_info()


user1.enroll()
user3.spend_points(40)