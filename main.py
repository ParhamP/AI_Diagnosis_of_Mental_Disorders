from similarity import get_similarity
from stt import audio_to_text
from recorder import recorder
from subprocess import Popen
import questionare

Popen("say Welcome to Artificial Intelligent Diagnosis of Mental Disorders. Please tell me about your symptomes: ",
      shell=True).communicate()

# recorded_symptomes = recorder(40, "output1.wav",
#                               "XXXXX",
#                               "XXXX")

# with open("current_symptomes.txt", "w") as f:
#     f.write(recorded_symptomes)

disorders_model = {"adhd": ["disorders/adhd.txt", "adhd_questionare"],
                   "bodyDysmorphic": ["disorders/bodyDysmprphic.txt", "bodyDysmorphic_questionare"],
                   "histronicDisorder": ["disorders/histronic.txt", "histronic_questionare"],
                   "insomniaDisorder": ["disorders/insomniaDisorder.txt", "insomnia_questionare"],
                   "majorDepressive": ["disorders/majorDepressive.txt", "majorDepression_questionare"],
                   "narcissism": ["disorders/narcissistic.txt", "narcissism_questionare"],
                   "ocd": ["disorders/ocd.txt", "ocd_questionare"], "obssesiveCompulsivePersonalityDisorder": ["disorders/ocpd.txt", "ocpd_questionare"],
                   "panicDisorder": ["disorders/panicDisorder.txt", "panicDisorder_questionare"],
                   "paranoia": ["disorders/paranoid.txt", "paranoia_questionare"],
                   "ptsd": ["disorders/ptsd.txt", "ptsd_questionare"],
                   "schizofernia": ["disorders/schizofernia.txt", "schizofernia_questionare"],
                   "schizoid": ["disorders/schizoid.txt", "schizoid_questionare"],
                   "socialanxiety": ["disorders/socialAnxietyDisorder.txt", "socialAnxiety_questionare"]}


def find_most_similar(microsoft_key, current_symptomes, disorders_model):
    most_similar = None
    biggest_similar = 0
    second_biggest = 0
    second_similar = None
    for i in disorders_model.keys():
        similarity = get_similarity(microsoft_key, current_symptomes,
                                    disorders_model[i][0])
        similarity = float(similarity)
        # Add the similarity number to the model
        disorders_model[i].append(similarity)

        if similarity > biggest_similar:
            second_biggest = biggest_similar
            second_similar = most_similar
            most_similar = i
            biggest_similar = similarity
    return(most_similar, round(biggest_similar, 2) * 100, second_similar, str(round(second_biggest, 2) * 100))


result = find_most_similar("8f4d24ff4697465e9b07ca7ba1e2c55f",
                           "current_symptomes.txt", disorders_model)

print(disorders_model)

diagnosed_second_biggest = result[3]
diagnosed_second_similar = result[2]
diognosed_disorder = result[0]
diognosed_percentage = str(int(result[1]))

Popen("say You have " + diognosed_percentage + " percent chance of having" + diognosed_disorder + " and " + diagnosed_second_biggest + " percent chance of having " + diagnosed_second_similar + ". Lets narrow down the diognosis.",
      shell=True).communicate()

diognossed_questionare = getattr(questionare,
                                 disorders_model[diognosed_disorder][1])()

if diognossed_questionare:
  Popen("say You are diagnosed with " + diognosed_disorder + ".",
      shell=True).communicate()
else:
  Popen("say You don't have all the symptomes necessary to be diagnosed with " + diognosed_disorder + ".",
      shell=True).communicate()
