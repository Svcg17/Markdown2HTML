#!/usr/bin/python3
"""
    Starting script that takes two arguments:
        - the Markdown file
        - the output file name
"""
if __name__ == "__main__":
    import sys
    from os import path

    markD = {"#": "h1", "##": "h2", "###": "h3", "####": "h4", "#####": "h5", "######": "h6", "-": "ul", "*": "ol"}

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not path.exists(sys.argv[1]) or not str(sys.argv[1]).endswith(".md"):
        sys.stderr.write("Missing " + sys.argv[1] + '\n')
        exit(1)

    with open(sys.argv[1], mode='r') as fr, open(sys.argv[2], mode='w+') as fw:
        first = 0
        f = 0
        read = fr.readlines()
        for i, line in enumerate(read):
            lineSplit = line.split(' ')
            if lineSplit[0] in markD:
                # Headings
                if lineSplit[0].startswith('#'):
                    tag = markD[lineSplit[0]]
                    toWrite = line.replace("{} ".format(lineSplit[0]), "<{}>".format(tag))
                    toWrite = toWrite[:-1] + ("</{}>\n".format(tag))
                    fw.write(toWrite)
                # Lists
                elif lineSplit[0].startswith("-") or lineSplit[0].startswith("*"):
                    tag = markD[lineSplit[0]]
                    #if its the first item list
                    if not first:
                        toWrite = "<{}>\n".format(tag)
                        fw.write(toWrite)
                        first = lineSplit[0]
                    # do every time for '-' or '*'
                    toWrite = line.replace("{} ".format(lineSplit[0]), "<li>")
                    toWrite = toWrite[:-1] + ("</li>\n")
                    fw.write(toWrite)
                    # if its the last item list
                    if i is len(read) - 1 or not read[i + 1].startswith("{} ".format(first)):
                        toWrite = "</{}>\n".format(tag)
                        fw.write(toWrite)
                        first = 0
            else:
                # paragraphs 
                if line[0] != "\n":
                    if not f:
                        fw.write("<p>\n")
                        f = 1
                    fw.write(line)
                    if i != len(read) - 1 and read[i + 1][0] != "\n" and read[i + 1][0] not in markD:
                        fw.write("</br>\n")
                        continue
                    else: 
                        fw.write("</p>\n")
                        f = 0
                else:
                    fw.write(line)
        exit(0)
