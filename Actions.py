class Actions:

    # These are the actions that can be taken in each location you go to
    # The actions are pulled into the Locations class to be used

    # Actions used for bath location

    def restroom_break(self):
        print("Use the restroom. Make sure you wash you hands when you are done.")
        return .08

    def routine_morning(self):
        print("Put in your contacts. Brush your hair. Brush your teeth. Take your allergy medication.")
        return .08

    def routine_night(self):
        print("Brush your teeth. Take out contacts. Put on night facial cream.")
        return .08

    def take_shower(self):
        print("Time to get clean. Hop in the shower.")
        return .5

    # Actions used for bed location

    def get_dressed(self):
        print("Put on clothes.")
        return .08

    def go_to_bed(self):
        print("Have you done your bathroom night routine yet? \n"
              "Type 'Y' for yes or 'N' for no.")
        get_ready_for_bed = input()
        if get_ready_for_bed == "N":
            print("You will need to go to the bathroom and perform your night time routine.")
            self.routine_night()
        print("Great you are already ready for bed.")
        print("Don't forget to set your alarm for tomorrow. Goodnight. Sweet dreams!")
        return 24

    def take_nap(self):
        print("How long of a nap would you like to take? 30 minutes or 1 hour? \n"
              "Type '30' for 30 minutes or '1' for 1 hour.")
        nap_time_amount = input()
        print("Have a nice nap.")
        if nap_time_amount == 30:
            return .5
        else:
            return 1

    # Actions used for front_room location

    def feed_dog(self):
        print("Fill up the dogs bowl with food and place it on their food mat.")
        return .08

    def get_on_phone(self):
        print("Turn on your phone to read the news and browse Pinterest.")
        return .5

    def play_games(self):
        print("Turn on the Switch and play a game")
        return 1

    def watch_tv(self):
        print("Turn on the TV and find something to watch.")
        return 1

    # Actions used for kitchen location

    def do_dishes(self):
        print(
            "Put the clean dishes away. Once all dishes are put away rinse off dirty dishes and put them in the dishwasher. Remember to run the dishwasher when done putting dishes in it.")
        return .5

    def grocery_shopping(self):
        print("You need to leave the house to get groceries. Go to the bedroom to put on going out clothes.")
        self.get_dressed()
        print("Grab your keys, wallet, and phone before leaving the house. Head to the store.")
        return 1.5

    def make_food(self, time_of_day):
        if time_of_day < 10:
            print("Make yourself some breakfast and coffee.")
            return .25
        elif time_of_day < 12:
            print("Make yourself a snack. It is too late for breakfast, but too early for lunch.")
            return .25
        elif time_of_day < 14:
            print("Make yourself some lunch.")
            return .25
        elif time_of_day < 17:
            print("Make yourself a snack. It is too late for lunch, but too early for dinner.")
            return .25
        elif time_of_day < 20:
            print("Make yourself some dinner.")
            return .25
        else:
            print("Make yourself a snack. It is too late for dinner.")
            return .25

    # Actions used for office location

    def browse_internet(self):
        print("Turn on your computer, open Chrome and browse your favorite web pages.")
        return .5

    def crafts(self):
        print("Grab some craft and get creative!")
        return 1

    def school(self):
        print("Do some school work. It's time to learn a lot.")
        return 1

    def work(self):
        print("Turn on your computer and login to your work accounts.")
        hours_worked = 2
        need_break = False
        while need_break == False:
            print("You have spent 2 hours working to you need a break? \n"
                  "Type 'Y' if a break is needed or 'N' if you can keep working")
            break_needed = input()
            if break_needed == "N":
                print("Keep on working.")
                hours_worked += 2
            else:
                need_break = True

        return hours_worked

    # Actions used for out location

    def take_dog_out(self):
        print(
            "Put outside shoes on. If it is below 50 degrees fahrenheit put a jacket on. Put a leash on your dog. Take the dog outside to go to potty. \n"
            "When done and back inside, take leash off dog, jacket off if you ahd one on, and take off shoes.")
        return .25
