import re

departmentHeader = re.compile("([\w ]+) Courses\n")
courseHeader = re.compile("([\w& ]+). ([^\.]+). (\d(?:-\d)? Units)")
prereqLine = re.compile("Prerequisite: ([^\.]+)")

with open('catalog.txt', 'r', encoding='utf8') as courseCatalog, open("courseList.txt", "w", encoding="utf8") as output:
    i = 0
    for line in courseCatalog:
        i += 1
        deptLine = departmentHeader.match(line)
        if deptLine:
            output.write(line)
            continue
        courseLine = courseHeader.match(line)
        if courseLine:
            output.write(line)
            continue
        prereqs = prereqLine.match(line)
        if prereqs:
            output.write("Prerequisite: " + prereqs.group(1) + "\n")
