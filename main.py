from similarity import get_similarity
from stt import audio_to_text
from recorder import recorder
from subprocess import Popen
from ocpd_questionare import ocpd_questionare

Popen("say Hi! Welcome to Artificial Intelligent Diagnosis of Mental Disorders. Please tell me about your symptomes: ",
      shell=True).communicate()

# recorded_symptomes = recorder(40, "output1.wav",
#                               "XXXXX",
#                               "XXXX")

# with open("current_symptomes.txt", "w") as f:
#     f.write(recorded_symptomes)

disorders_model = {"adhd": ["disorders/adhd.txt"],
                   "bodyDysmorphic": ["disorders/bodyDysmprphic.txt"],
                   "histronicDisorder": ["disorders/histronic.txt"],
                   "insomniaDisorder": ["disorders/insomniaDisorder.txt"],
                   "majorDepressive": ["disorders/majorDepressive.txt"],
                   "narcissism": ["disorders/narcissistic.txt"],
                   "ocd": ["disorders/ocd.txt"], "obssesiveCompulsiveDisorder": ["disorders/ocpd.txt"],
                   "panicDisorder": ["disorders/panicDisorder.txt"],
                   "paranoia": ["disorders/paranoid.txt"],
                   "ptsd": ["disorders/ptsd.txt"],
                   "schizofernia": ["disorders/schizofernia.txt"],
                   "schizoid": ["disorders/schizoid.txt"],
                   "socialanxiety": ["disorders/socialAnxietyDisorder.txt"]}


def find_most_similar(microsoft_key, current_symptomes, disorders_model):
    most_similar = None
    biggest_similar = 0
    for i in disorders_model.keys():
        similarity = get_similarity(microsoft_key, current_symptomes,
                                    disorders_model[i][0])
        similarity = float(similarity)
        # Add the similarity number to the model
        disorders_model[i].append(similarity)

        if similarity > biggest_similar:
            most_similar = i
            biggest_similar = similarity
    return(most_similar, round(biggest_similar, 2) * 100)


result = find_most_similar("XXXXXX",
                           "current_symptomes.txt", disorders_model)
print result

diognosed_disorder = result[0]
diognosed_percentage = str(int(result[1]))
print diognosed_percentage

Popen("say You have " + diognosed_percentage + " percent chance of having" + diognosed_disorder + ". lets narrow down the diognosis.",
      shell=True).communicate()

ocpd_result = ocpd_questionare()

if ocpd_result:
  print "YES"
else:
  print "NOO"
