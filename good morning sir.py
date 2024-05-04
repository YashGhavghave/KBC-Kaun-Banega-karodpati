import time
import gtts
import playsound

timestamp = time.strftime ('%H:%M:%S')
print (timestamp)

timestamp = (int (time.strftime ('%H')))
# print(type(timestamp))
# print(timestamp)
if (0 <= timestamp <= 11):
    print ("Good morning sir")
    Alpha = "Good morning sir"
    sound = gtts.gTTS (Alpha, lang="en")
    sound.save ("yash.mp3")
    playsound.playsound ("yash.mp3")

elif (12 <= timestamp < 17):
    print ("Good afternoon sir")
    Beta = "Good afternoon sir"
    sound = gtts.gTTS (Beta, lang="en")
    sound.save ("yash.mp3")
    playsound.playsound ("yash.mp3")



elif (17 <= timestamp <= 21):
    print ("Good evening sir")
    Can = "Good evening sir"
    sound = gtts.gTTS (Can, lang="en")
    sound.save ("yash.mp3")
    playsound.playsound ("yash.mp3")


else:
    print ("Good Night sir")
    yash = "Good night sir"
    sound = gtts.gTTS (yash, lang="en")
    sound.save ("yash.mp3")
    playsound.playsound ("yash.mp3")

# sound=gtts.gTTS(text, lang="hi")
# sound.save("yash.mp3")
# playsound.playsound("yash.mp3")
#
# # Alpha=Alpha


# else:
#    print("Have a great time")

# timestamp=int(time.strftime('%M'))
# print(type(timestamp))
# print(timestamp)
# timestamp=int(time.strftime('%S'))
# print(type(timestamp))
# print(timestamp)
