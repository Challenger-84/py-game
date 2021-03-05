def generateLevel(filename):
    row = []
    level = []
    levels = []
    # Opening the file
    with open(filename, 'rt') as f:
        text = f.readlines()
        for line in text:
            if not line.startswith('////'):
                line = line.strip()
                for i in range(0, len(line)):
                    row.append(line[i])
                level.append(row)
                row = []
            else:
                levels.append(level)
                level = []
    return levels
