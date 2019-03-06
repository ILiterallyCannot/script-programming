def tulosta(countrycodes,codemap,countries):
    for code in countrycodes:
        print codemap[code]
        print "\tPrime Minister:", countries[codemap[code]]["Prime Minister"][0], "who is", countries[codemap[code]]["Prime Minister"][1],"years old"
        print "\tPopulation:", countries[codemap[code]]["Population"],"million\n"
