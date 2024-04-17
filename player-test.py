from player import Player

p1= Player("Tintin")
print(p1.getName())
p1.setName("Tin")
print(p1.getName())

print(p1.getScore()) ## 0

p1.setScore(10)
print(p1.getScore()) ## 1

p1.setScore(10)
p1.setScore(10)
print(p1.getScore()) ## 3

p1.setScore(-10)
p1.setScore(-10)
print(p1.getScore()) ## 1