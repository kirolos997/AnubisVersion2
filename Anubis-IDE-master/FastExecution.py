# Welcome in fast Execution Mode
# 1- Write your tested function inside the specified section
# 2- Place your passed arguments (if function needs) inside the function call

# Section for testing function, can take many parameters
# WARNING! Do NOT CHANGE THIS FUNCTION NAME
# WARNING! SAVE FIRST BEFORE EXECUTION

def testedFunction(parametersList):

    # parametersList is an array containing the passed parameters from the main caller function
    # So to access parameters you will write parametersList[0,1,2,....]

    if(parametersList[0]==parametersList[1]):
             print('The maximum number is the first = ')
             print(parametersList[0])

    else:
             print('The maximum number is the second = ')
             print(parametersList[1])

