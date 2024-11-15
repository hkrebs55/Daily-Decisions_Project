from Locations import Locations
from Actions import Actions


class MyDay:

    def __init__(self):
        self.locationObject = Locations()
        self.actionObject = Actions()
        # time_of_day is set to the time the alarm is scheduled to go off
        self.time_of_day = 8

    # Before the day begins the user needs to get up
    # The time the user gets up depends on how many time they snooze the alarm
    def time_to_get_up(self):
        print("Your alarm is going off! It is " + str(self.time_of_day) + ". Do you snooze it for 5 minutes? \n"
              "Type 'Y' for yes or 'N' for no.")
        snooze_alarm = input()
        while snooze_alarm == "Y":
            self.time_of_day += .08
            print("Your alarm is going off! It is now " + str(self.time_of_day) +
                  ". Do you snooze it for another 5 minutes? \n"
                  "Type 'Y' for yes or 'N' for no.")
            snooze_alarm = input()
        print("Good morning. You are now awake and up.")

    # Once the user is up and no longer snoozing the alarm they need to decide what location to go
    # Depending on the location the user picks they will be prompted with which actions they can take
    def decisions_for_day(self):
        print("Now that you are up what are you going to do for the day. \n"
              "Remember that you need to be in bed before or at 24 hours. \n"
              "Within this time make sure you feed yourself by going to the kitchen, "
              "go to the restroom by going to the bathroom, "
              "feed the dog by going to the front room, and take the dog to the restroom by going outside.")

        # When time_of_day is at 24 or higher the user needs to go to bed
        while self.time_of_day < 24:
            print("It is currently " + str(self.time_of_day) + ". \n"
                  "Pick one of the below locations to go to by typing the corresponding number. \n"
                  "1. Bathroom \n"
                  "2. Bedroom \n"
                  "3. Front Room \n"
                  "4. Kitchen \n"
                  "5. Office \n"
                  "6. Outside")
            picked_location = input()
            if picked_location == "1":
                self.time_of_day += self.locationObject.bath()
            elif picked_location == "2":
                self.time_of_day += self.locationObject.bed()
            elif picked_location == "3":
                self.time_of_day += self.locationObject.front_room()
            elif picked_location == "4":
                self.time_of_day += self.locationObject.kitchen(self.time_of_day)
            elif picked_location == "5":
                self.time_of_day += self.locationObject.office()
            elif picked_location == "6":
                self.time_of_day += self.locationObject.outside()

        if self.time_of_day < 32:
            print("It is currently " + str(self.time_of_day) + ", which means it is time to go to bed. \n")
            self.time_of_day += self.actionObject.go_to_bed()


NewDay = MyDay()
NewDay.time_to_get_up()
NewDay.decisions_for_day()
