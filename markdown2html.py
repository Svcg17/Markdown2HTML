#!/usr/bin/python3
"""
    Starting script that takes two arguments:
        - the Markdown file
        - the output file name
"""
if __name__ == "__main__":
    import sys
    from os import path

    markD = {"#": "h1", "##": "h2", "###": "h3", "####": "h4", "#####": "h5", "######": "h6", "-": ["ul", "li"]}

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not path.exists(sys.argv[1]) or not str(sys.argv[1]).endswith(".md"):
        sys.stderr.write("Missing " + sys.argv[1] + '\n')
        exit(1)

    with open(sys.argv[1], mode='r') as fr, open(sys.argv[2], mode='w+') as fw:
        first = 0
        read = fr.readlines()
        for i, line in enumerate(read):
            lineSplit = line.split(' ')
            # Headings
            print('#####', line)
            if lineSplit[0].startswith('#') and lineSplit[0] in markD:
                print('heading')
                tag = markD[lineSplit[0]]
                toWrite = line.replace("{} ".format(lineSplit[0]), "<{}>".format(tag))
                toWrite = toWrite[:-1] + ("</{}>\n".format(tag))
                fw.write(toWrite)
            # Lists
            elif lineSplit[0].startswith("-") and lineSplit[0] in markD:
                #if its the first item list
                if not first:
                    toWrite = "<{}>\n".format(markD[lineSplit[0]][0])
                    fw.write(toWrite)
                    first = 1
                # do every time for '-'
                tag = markD[lineSplit[0]][1]
                toWrite = line.replace("{} ".format(lineSplit[0]), "<{}>".format(tag))
                toWrite = toWrite[:-1] + ("</{}>\n".format(tag))
                fw.write(toWrite)
                # if its the last item list
                if first and not read[i + 1].startswith("- "):
                    toWrite = "</{}>\n".format(markD[lineSplit[0]][0])
                    fw.write(toWrite)
                    first = 0
            else:
                fw.write(line)
        exit(0)
"""
elif not first and lineSplit[0].startswith("-") and lineSplit[0] in markD:
    ul = markD[lineSplit[0]][0] 
    li = markD[lineSplit[0]][1] 
    toWrite = line.replace("{} ".format(lineSplit[0]), "<{}>\n<{}>".format(ul, li))
    toWrite = toWrite[:-1] +("</{}>\n".format(li))
    first = 1
    fw.write(toWrite)
    if first and next(fr).startswith(lineSplit[0]):
        toWrite = line.replace("{} ".format(lineSplit[0]), "<{}>".format(li))
        toWrite = toWrite[:-1] +("</{}>\n".format(li))
        fw.write(toWrite)
    elif first and not next(line).startswith(lineSplit[0]):
        fw.write('lastone')
*/
"""