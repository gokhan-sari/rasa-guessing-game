# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, SlotSet

import random, json

class RandomAnimalSelect(Action):

    def name(self) -> Text:
        return "action_random_animal_select"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data = []
        with open('animals.json') as file:
            data = json.load(file)['data']

        random_number = random.randrange(len(data))
        selected_animal = data[random_number]

        slot_sets = []

        for key, value in selected_animal.items():
            slot_name = "animal_" + str(key)
            slot_value = value
            slot_sets.append(SlotSet(slot_name, slot_value))

        dispatcher.utter_message("Try to guess the animal I am thinking of.")

        return slot_sets

class ActionColorGuess(Action):

    def name(self) -> Text:
        return "action_color_guess"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_guess = tracker.get_slot("user_guess")
        animal_color = tracker.get_slot("animal_color")

        if(user_guess.lower() == animal_color.lower()):
            dispatcher.utter_message("Yes, it is " + str(user_guess) + ".")
        else:
            dispatcher.utter_message("No, it is not " + str(user_guess) + ".")

        return []

class ActionColorTell(Action):

    def name(self) -> Text:
        return "action_color_tell"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        animal_color = tracker.get_slot("animal_color")
        dispatcher.utter_message("It is " + str(animal_color) + ".")

        return []

class ActionLegGuess(Action):

    def name(self) -> Text:
        return "action_leg_guess"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_guess = tracker.get_slot("user_guess")
        animal_legs = tracker.get_slot("animal_legs")

        if(int(user_guess) == int(animal_legs)):
            dispatcher.utter_message("Yes, it has " + str(user_guess) + " legs.")
        elif(int(user_guess) < int(animal_legs)):
            dispatcher.utter_message("No, it has more than " + str(user_guess) + " legs.")
        elif(int(user_guess) > int(animal_legs)):
            dispatcher.utter_message("No, it has less than " + str(user_guess) + " legs.")
        else:
            dispatcher.utter_message("Try again.")

        return []

class ActionLegTell(Action):

    def name(self) -> Text:
        return "action_leg_tell"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        animal_legs = tracker.get_slot("animal_legs")
        dispatcher.utter_message("It has " + str(animal_legs) + " legs.")

        return []

class ActionTalentGuess(Action):

    def name(self) -> Text:
        return "action_talent_guess"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_guess = tracker.get_slot("user_guess")
        talent = tracker.get_slot("animal_" + user_guess.lower())

        if(talent == "Yes"):
            dispatcher.utter_message("Yes, it can " + user_guess + ".")
        else:
            dispatcher.utter_message("No, it can't.")

        return []

class ActionAnimalGuess(Action):

    def name(self) -> Text:
        return "action_animal_guess"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_guess = tracker.get_slot("user_guess")
        animal_name = tracker.get_slot("animal_name")

        if(user_guess.lower() == animal_name.lower()):
            dispatcher.utter_message("Congratulations, you guessed it correctly, it is a " + str(user_guess) + " indeed.")
        else:
            dispatcher.utter_message("No, it is not a " + str(user_guess) + ".")

        return []

class ActionAnimalTell(Action):

    def name(self) -> Text:
        return "action_animal_tell"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        animal_name = tracker.get_slot("animal_name")
        dispatcher.utter_message("I was thinking of a " + str(animal_name) + ".")

        return []