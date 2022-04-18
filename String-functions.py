text = "temperature and facts about the moon".title()
print(text) #Temperature And Facts About The Moon
text = "Temperature And Facts About The Moon".lower()
print(text) #temperature and facts about the moon
text = "Temperature And Facts About The Moon".upper()
print(text) #TEMPERATURE AND FACTS ABOUT THE MOON


text = "Temperature And Facts About The Moon".split(" ")
print(text) #['Temperature', 'And', 'Facts', 'About', 'The', 'Moon']
print(' + '.join(text)) #Temperature + And + Facts + About + The + Moon

text1 = "temperature and facts about the moon".find("Tera")
print(text1) #-1
text1 = "temperature and facts about the moon".find("moon")
print(text1) #32

text2 = "temperature and facts about the moon".count("oo")
print(text2) #1
text2 = "temperature and facts about the moon".count("Mars")
print(text2) #0

mars_temperature = "The highest temperature on Mars is about 30 C"
mars_temperature = mars_temperature.split()
print(type(mars_temperature[-2])) #class STR
print(mars_temperature[-2].isnumeric()) #True

print("-60".startswith('-')) #True
print("30 C".endswith("C")) #True

print("This is Celsius".replace("Celsius","C")) #This is C

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
text = text.split(". ")
print(text)

for sentence in text:
    if "temperature" in sentence:
        print(sentence)
#The highest daylight temperature of the Moon is 127 C.

mass_percentage = 15
print("""You are lighter on the {0}, because on the {0} 
you would weigh about {1} of your weight on Earth {word}""".format("Moon", mass_percentage, word="!#@"))
#You are lighter on the Moon, because on the Moon
#you would weigh about 15 of your weight on Earth !#@

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")
#On the Moon, you would weigh about 16.7% of your weight on Earth