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
