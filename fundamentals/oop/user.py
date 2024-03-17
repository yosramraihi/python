class User:
    def __init__(self, first_name , last_name, email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0



    def display_info (self):
        print("==========================")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_reward_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("==========================")
    def enroll(self):
            self.is_reward_member=True
            self.gold_card_points=200




    def spend_points(self,amount):
            self.gold_card_points -= amount


user_1=User("jkhk","ahjazh","ddddddf",30)
user_1.display_info()
user_2=User("hjhj","hhjh","jjlk",80)
user_2.spend_points(50)
user_3=User("fjdj","fjdjds","jfkdj",34)
user_3.enroll()
user_3.spend_points(80)
user_2.display_info()
user_3.display_info()
