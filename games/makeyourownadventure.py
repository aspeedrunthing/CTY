import csv
def playstory(story, path, options):
    choice = 0
    currentstory1 = 0
    currentpath = []
    currentoption = 0
    print(story[0][0])
    for i in range(0, options[0][0]):
        if i == len(path[0])-1:
            choice = int(input("or {}: {}".format(i+1,path[0][i])))
        elif i == 0:
            print("will you 1: {},".format(path[0][i]), end=" ")
        else:
            print("or {}: {},".format(i+1,path[0][i]), end=" ")
    choice = choice+currentoption
    for i in range(0, choice-1):
        currentoption+=options[currentstory1+1][i]
    currentpath.append(choice)
    currentstory1 += 1
    while options[currentstory1][choice-1] > 0:
        print(story[currentstory1][currentpath[len(currentpath)-1]-1])
        for i in range(0, options[currentstory1][choice-1]):
            if i == options[currentstory1][choice-1]-1:
                choice = int(input("or {}: {}".format(i+1,path[currentstory1][i+currentoption])))
            elif i == 0:
                print("will you 1: {},".format(path[currentstory1][i+currentoption]), end=" ")
            else:
                print("or {}: {},".format(i+1,path[currentstory1][i+currentoption]), end=" ")
        choice = choice+currentoption
        currentoption = 0
        currentstory1 += 1
        for i in range(0, choice-1):
            currentoption+=options[currentstory1][i]
        currentpath.append(choice)
    print(story[currentstory1][choice-1])
    print(end[abs(options[currentstory1][choice-1])][0])
story = []
path = []
options = []
action = "a"
end = []
saveload = input("do you want to LOAD a file or WRITE your own").lower()
if saveload == "write":
    story.append([input("What do you want your introduction line to be")])
    path.append([])
    options.append([int(input("How many paths do you want from the introduction?"))])
    for i in range(0, options[0][0]):
        path[len(path)-1].append(input("Choose a path option"))
    while not action == "stop":
        action = input("Do you want to CONTINUE your story or STOP").lower()
        if action == "stop":
            break
        story.append([])
        path.append([])
        options.append([])
        paths = 0
        for i in range(0, len(path[len(path)-2])):
            story[len(story)-1].append(input("What do you want next line to be for this path?"))
            paths = int(input("How many paths do you want from the previous line?"))
            if paths != 0:
                options[len(options)-1].append(paths)
            else:
                options[len(options)-1].append(-len(end))
            if paths == 0:
                end.append([input("Choose an ending")])
            for o in range(0, options[len(options)-1][i]):
                path[len(path)-1].append(input("Choose a path option"))
    saveload = input("Do you want to SAVE this story").lower()
    if saveload == "save":
        savefile = input("What do you want your file name to be?")
        f = open("{}1".format(savefile), "w")
        for i in range(0, len(story)):
            for o in range(0, len(story[i])):
                if o == len(story[i])-1:
                    f.write(str(story[i][o]))
                else:
                    f.write(str(story[i][o]))
                    f.write("\t")
            if not i == len(story)-1:
                f.write("\n")
        f.close()
        f = open("{}2".format(savefile), "w")
        for i in range(0, len(path)):
            for o in range(0, len(path[i])):
                if o == len(path[i])-1:
                    f.write(str(path[i][o]))
                else:
                    f.write(str(path[i][o]))
                    f.write("\t")
            if not i == len(path)-1:
                f.write("\n")
        f.close()
        f = open("{}3".format(savefile), "w")
        for i in range(0, len(options)):
            for o in range(0, len(options[i])):
                if o == len(options[i])-1:
                    f.write(str(options[i][o]))
                else:
                    f.write(str(options[i][o]))
                    f.write("\t")
            if not i == len(options)-1:
                f.write("\n")
        f.close()
        f = open("{}4".format(savefile), "w")
        for i in range(0, len(end)):
            for o in range(0, len(end[i])):
                if o == len(end[i])-1:
                    f.write(str(end[i][o]))
                else:
                    f.write(str(end[i][o]))
                    f.write("\t")
            if not i == len(end)-1:
                f.write("\n")
        f.close()
elif saveload == "load":
    load = input("What file do you want to load? (has to be one that exists)")
    file = open("{}1".format(load), "r")
    source = file.read()
    lines = source.split("\n")
    reader = csv.reader(lines, delimiter='\t')
    story = [word for word in [row for row in reader]]
    file = open("{}2".format(load), "r")
    source = file.read()
    lines = source.split("\n")
    reader = csv.reader(lines, delimiter='\t')
    path = [word for word in [row for row in reader]]
    file = open("{}3".format(load), "r")
    source = file.read()
    lines = source.split("\n")
    reader = csv.reader(lines, delimiter='\t')
    options = [word for word in [row for row in reader]]
    file = open("{}4".format(load), "r")
    source = file.read()
    lines = source.split("\n")
    reader = csv.reader(lines, delimiter='\t')
    end = [word for word in [row for row in reader]]
    for i in range(0, len(options)):
        for o in range(0, len(options[i])):
            options[i][o] = int(options[i][o]) 
playstory(story, path, options)