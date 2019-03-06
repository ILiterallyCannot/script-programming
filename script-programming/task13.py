name = raw_input("Give your dog a name: ")
def dog_sleeps(name, time): #prints: X sleeps Y hours
    print name, " sleeps ", time, " hours"
def dog_walks(name, speed): #prints: X walks Y speed
    print name, " walks ", speed, " km/h"
def dog_runs(name, speed):  #prints: X runs Y speed
    print name, " can run ", speed, " km/h"
def dog_barks(name, sound): #prints: X barks with a sound Y
    print name, " says '", sound, "'"
#For example:

dog_walks(name, 5) #Musti walks 10.00km/h speed
dog_barks(name,"wuf wuf") # Musti barks with a sound "wuf wuf"
dog_runs(name, 20)
