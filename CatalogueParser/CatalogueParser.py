import re
from Course import Course

departmentHeader = re.compile("([\w ]+) Courses\n")
courseHeader = re.compile("([\w& ]+). ([^\.]+). (\d(?:-\d)? Units)")
prereqLine = re.compile("Prerequisite: ([A-Z]{2,}[^\.]+)")
class CatalogueParser:
    def __init__(self, catalogueFile):
        self.catalogueFile = catalogueFile
        self.catalogue = dict()
    
    def parse(self):
        with open(self.catalogueFile, 'r', encoding='utf8') as courseCatalog:
            currentCourse = None
            for line in courseCatalog:
#                 print(line)
#                 deptLine = departmentHeader.match(line)
#                 if deptLine:
#                     continue
                courseLine = courseHeader.match(line)
                if courseLine:
                    if currentCourse:
                        self.catalogue[currentCourse.shortName] = currentCourse
                    currentCourse = Course(courseLine.group(1))
                    currentCourse.fullName = courseLine.group(2)
                    currentCourse.units = courseLine.group(3)
                    continue
                prereqs = prereqLine.match(line)
                if prereqs:
                    if currentCourse == None:
                        print("Prereqs but no course?! " + prereqs.group(1))
                        continue
                    try:
                        currentCourse.setRequirements(prereqs.group(1))
                    except:
                        print("Except")
                        print(line)


if __name__ == "__main__":
    parser = CatalogueParser("catalog.txt")
    parser.parse()
    csCourses = [x for x in parser.catalogue.keys() if "CS" in x]
    for key in csCourses:
        course = parser.catalogue[key]
        print(course.shortName)
        print(course.getRequirementsList())