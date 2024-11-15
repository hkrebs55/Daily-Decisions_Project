from Actions import Actions


class Locations:

    def __init__(self):
        self.actionObject = Actions()

    def bath(self):
        time_spent = 0

        print("You are in the bathroom. Pick one of the below actions to perform by typing the corresponding number. \n"
              "1. Go to Restroom \n"
              "2. Morning Routine \n"
              "3. Night Routine \n"
              "4. Take a Shower \n"
              "5. None of these, go to another room")
        action_to_take = input()
        if action_to_take == "1":
            time_spent += self.actionObject.restroom_break()
        elif action_to_take == "2":
            time_spent += self.actionObject.routine_morning()
        elif action_to_take == "3":
            time_spent += self.actionObject.routine_night()
        elif action_to_take == "4":
            time_spent += self.actionObject.take_shower()
        elif action_to_take == "5":
            return

        return time_spent

    def bed(self):
        time_spent = 0

        print("You are in the bedroom. Pick one of the below actions to perform by typing the corresponding number. \n"
              "1. Get Dressed \n"
              "2. Take a Nap \n"
              "3. Go to bed for the night \n"
              "4. None of these, go to another room")
        action_to_take = input()
        if action_to_take == "1":
            time_spent += self.actionObject.get_dressed()
        elif action_to_take == "2":
            time_spent += self.actionObject.take_nap()
        elif action_to_take == "3":
            time_spent += self.actionObject.go_to_bed()
        elif action_to_take == "4":
            return

        return time_spent

    def front_room(self):
        time_spent = 0

        print("You are in the front room. Pick one of the below actions to perform by typing the corresponding number. \n"
              "1. Feed to dog \n"
              "2. Get on Your Phone \n"
              "3. Play Games \n"
              "4. Watch TV \n"
              "5. None of these, go to another room")
        action_to_take = input()
        if action_to_take == "1":
            time_spent += self.actionObject.feed_dog()
        elif action_to_take == "2":
            time_spent += self.actionObject.get_on_phone()
        elif action_to_take == "3":
            time_spent += self.actionObject.play_games()
        elif action_to_take == "4":
            time_spent += self.actionObject.watch_tv()
        elif action_to_take == "5":
            return

        return time_spent

    def kitchen(self, time_of_day):
        time_spent = 0

        print("You are in the kitchen \n"
              "Are there dishes to do? \n"
              "Type 'Y' for yes or 'N' for no.")
        dirty_dishes = input()
        if dirty_dishes == "Y":
            print("Do you want to do the dishes now? \n"
                  "Type 'Y' for yes or 'N' for no.")
            do_dishes = input()
            if do_dishes == "Y":
                time_spent += self.actionObject.do_dishes()
            else:
                print("You will need to do the dishes at some point today.")

        print("Are you hungry? \n"
              "Type 'Y' for yes or 'N' for no.")
        hungry = input()
        if hungry == "Y":
            time_spent += self.actionObject.make_food(time_of_day)

        print("Is there food in the house to make yourself something? \n"
              "Type 'Y' for yes or 'N' for no.")
        food_stocked = input()
        if food_stocked == "N":
            print("You will need to go to the grocery store to get food. Do you want to do this now? \n"
                  "Type 'Y' for yes or 'N' for no.")
            go_to_store = input()
            if go_to_store == "Y":
                time_spent += self.actionObject.grocery_shopping()
            else:
                print("You cannot make food right now and will need to go to the grocery store at some point today.")

        return time_spent

    def office(self):
        time_spent = 0

        print("You are in the office. Pick one of the below actions to perform by typing the corresponding number. \n"
              "1. Browse on the Internet \n"
              "2. Do a Craft \n"
              "3. Do School Work \n"
              "4. Log on for Work \n"
              "5. None of these, go to another room")
        action_to_take = input()
        if action_to_take == "1":
            time_spent += self.actionObject.browse_internet()
        elif action_to_take == "2":
            time_spent += self.actionObject.crafts()
        elif action_to_take == "3":
            time_spent += self.actionObject.school()
        elif action_to_take == "4":
            time_spent += self.actionObject.work()
        elif action_to_take == "5":
            return

        return time_spent

    def outside(self):
        time_spent = 0

        print("You are outside. Pick one of the below actions to perform by typing the corresponding number. \n"
              "1. Take the Dog to the Restroom \n"
              "2. None of these, go to another room")
        action_to_take = input()
        if action_to_take == "1":
            time_spent += self.actionObject.take_dog_out()
        elif action_to_take == "2":
            return

        return time_spent