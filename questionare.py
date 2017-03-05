from subprocess import Popen


def ocpd_questionare():
    positive_response = 0
    print("Are you preoccupied with details, rules, lists, order," +
          "organization, or schedulesto the extent that the major point of the activity is lost? Y/N")
    Popen("say Are you preoccupied with details, rules, lists, order," +
          "organization, or schedules to the extent that the major point of the activity is lost?",
          shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Do you Show perfectionism that interferes with task completion (e.g., is unable to complete a project because your own overly strict standards are not met)? Y/N")
    Popen("say Do you Show perfectionism that interferes with task completion?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Are you excessively devoted to work and productivity to the exclusion of leisure activities and friendships? Y/N")
    Popen("say Are you excessively devoted to work and productivity to the exclusion of leisure activities and friendships?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Are you overconscientious, scrupulous, and inflexible about matters of morality, ethics, or values? Y/N")
    Popen("say Are you overconscientious, scrupulous, and inflexible about matters of morality, ethics, or values?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Are you unable to discard worn-out or worthless objects even when they have no sentimental value. Y/N")
    Popen("say Are you unable to discard worn-out or worthless objects even when they have no sentimental value.?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Are you reluctant to delegate tasks or to work with others unless they submit to exactly your way of doing things? Y/N")
    Popen("say Are you reluctant to delegate tasks or to work with others unless they submit to exactly your way of doing things?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Do you Adopt a miserly spending style toward both self and others; money is viewed assomething to be hoarded for future catastrophes? Y/N")
    Popen("say Do you Adopt a miserly spending style toward both self and others and money is viewed assomething to be hoarded for future catastrophes?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Do you Show rigidity and stubbornness? Y/N")
    Popen("say Do you show rigidity and stubborness?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    if positive_response >= 4:
        return True
    else:
        return False


def narcissism_questionare():
    positive_response = 0
    print("Do you have a grandiose sense of self-importance? Y/N")
    Popen("say Do you have a grandiose sense of self-importance?",
          shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Are you preoccupied with fantasies of unlimited success, power, brilliance, beauty, or ideal love? Y/N")
    Popen("say Are you preoccupied with fantasies of unlimited success, power, brilliance, beauty, or ideal love?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Are you often envious of others or believes that others are envious of you? Y/N")
    Popen("say Are you often envious of others or believes that others are envious of you?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Do you believe that you are special and unique and can only be understood by, or should associate with, other special or high-status people? Y/N")
    Popen("say Do you believe that you are special and unique and can only be understood by, or should associate with, other special or high-status people?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Do you require excessive admiration? Y/N")
    Popen("say Do you require excessive admiration?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Do you have a sense of entitlement? Y/N")
    Popen("say Do you have a sense of entitlement?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Are you interpersonally exploitative? Y/N")
    Popen("say Are you interpersonally exploitative??", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Do you lack empathy are you unwilling to recognize or identify with the feelings and needs of others? Y/N")
    Popen("say Do you lack empathy are you unwilling to recognize or identify with the feelings and needs of others?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    print("Do you show arrogant, haughty behaviors or attitudes? Y/N")
    Popen("say Do you show arrogant, haughty behaviors or attitudes?", shell=True).communicate()
    response = raw_input()
    if response == "Y":
        positive_response += 1
    if positive_response >= 5:
        return True
    else:
        return False
