from allpairspy import AllPairs




def getallpairspy(parameters):

    print("PAIRWISE:")
    for i, pairs in enumerate(AllPairs(parameters)):
        print("{:2d}: {}".format(i, pairs))

def main():
    parameters = [
        ["Brand X", "Brand Y"],
        ["98", "NT", "2000", "XP"],
        ["Internal", "Modem"],
        ["Salaried", "Hourly", "Part-Time", "Contr."],
        [6, 10, 15, 30, 60],
    ]


    getallpairspy(parameters)
if __name__ == "__main__":
    main()






















