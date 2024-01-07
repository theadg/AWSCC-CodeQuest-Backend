baseFilePath = '/Users/badg/Documents/repos/AWSCC-CodeQuest-Backend/backend/day-11'

namesList = []

def sortNames(names):
    return sorted(names)

def arrangeNames(names):
    # Add '\n" to each of the names
    for index,name in enumerate(names):
        if "\n" not in name:
            names[index] = f"{name}\n"

    return names;

def handleSortAndArrangeNames(names):
    return arrangeNames(sortNames(names))

# Open a file for reading
with open(f"{baseFilePath}/file.txt", 'r') as file:
    lines = file.readlines()
    # Add names to namesList
    for line in lines:
        namesList.append(line)

sortedNames = handleSortAndArrangeNames(namesList)

with open(f"{baseFilePath}/file.txt", 'w') as file:
    lines = file.writelines(sortedNames)



    