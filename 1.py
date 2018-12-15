import sys
from _curses import beep
from builtins import print
dataFile = open('WBC.data', 'r').read()

# Makes data file ready to use by assigning every record to a dictionary class name dataDic.
dataDic = {i.split(',')[0]: i.split(',')[1:] for i in dataFile.split('\n')}

miss_value_list= []
negative= []
positive= []

def fix_miss(document,list):

    for i in range(9):
        totalvalue = 0
        totalcount=0
        for check in list:
            if check[i] not in "?":
                totalvalue=totalvalue+int(check[i])
                totalcount=1+totalcount
        if document[i] in "?":
            document[i]= str(round(totalvalue/totalcount))
            miss_value_list.append(round(totalvalue/totalcount))


def DataClean(dataDic):

    list_of_records_benign=[]
    list_of_records_malignant=[]
    for document in dataDic.values():
        if document[9] in "malignant":
            list_of_records_malignant.append(document)
        else:
            list_of_records_benign.append(document)
    for document in dataDic.values():
        if document[9] in "malignant":
            fix_miss(document, list_of_records_malignant)
        else:
            fix_miss(document, list_of_records_benign)
    total= 0
    for i in miss_value_list:
        total= total+i
    return total/len(miss_value_list)


# Performas step-wise search in WBC database, design the content and arguments depending on your design


def performStepWiseSearch(argument):
    list = argument.split(",")
    for i in range(9):
        element = list[i]
        for an_element_of_the_list in dataDic.values():
            if len(element.split(":")) == 1:
                pass
            elif len(element.split(":")) == 2:
                number = int(element.split(":")[1])
                procedure = element.split(":")[0]
                if procedure == "<":
                    if not int(an_element_of_the_list[i])<number:
                        an_element_of_the_list[9] = "fail"
                if procedure == "<=":
                    if not int(an_element_of_the_list[i])<= number:
                        an_element_of_the_list[9] = "fail"
                if procedure == ">":
                    if not int(an_element_of_the_list[i])>number:
                        an_element_of_the_list[9] = "fail"
                if procedure == ">=":
                    if not int(an_element_of_the_list[i])>=number:
                        an_element_of_the_list[9] = "fail"
                if procedure == "!=":
                    if not int(an_element_of_the_list[i])!=number:
                        an_element_of_the_list[9] = "fail"
                if procedure == "=":

                    if not int(an_element_of_the_list[i]) == number:
                        an_element_of_the_list[9] = "fail"
    for i in dataDic.values():
        if i[9]=="malignant":
            positive.append("#")
        if i[9]=="benign":
            negative.append("#")

# 1st phase: Cleaning WBC Database


print('The average of all missing values is  : ' + '{0:.4f}'.format(DataClean(dataDic)))

# 2nd phase: Retrieving knowledge from WBC dataset
argv=sys.argv[1]
performStepWiseSearch(argv)
lenpos=len(positive)
lenneg=len(negative)
x=(len(positive)/(len(negative)+len(positive)))
print('\nTest Results:\n'
      '----------------------------------------------'
      '\nPositive (malignant) cases            : ' + str(lenpos) +
      '\nNegative (benign) cases               : ' + str(lenneg) +
      '\nThe probability of being positive     : ' + '{0:.4f}'.format(x) +
      '\n----------------------------------------------')


