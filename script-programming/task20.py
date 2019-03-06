countrycodes = ["fi", "se", "no"]
codemap = {"fi":"Finland","se":"Sweden","no":"Norway"}
countries = {"Finland" : {"Prime Minister": ("Juha Sipila", 54),"Population":5.439}, "Sweden" : {"Prime Minister": ("Steven Lofven", 58), "Population":9.593},"Norway" : { "Prime Minister": ("Erna Solberg",54), "Population":5.084}}

for code in countrycodes:
    print codemap[code]
    print "\tPrime Minister:", countries[codemap[code]]["Prime Minister"][0], "who is", countries[codemap[code]]["Prime Minister"][1],"years old"
    print "\tPopulation:", countries[codemap[code]]["Population"],"million\n"
