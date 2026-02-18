names = "sHAHEER, mUSTAFA, aRISHA, hAZIK, zARYAB, sARIM, uMER, aBDULLAH, aHMAR, hASSAN, aNAS, aSHER AND aHMAD."

case_name = "sHAHEER, mUSTAFA, aRISHA, hAZIK, zARYAB, sARIM, uMER, aBDULLAH, aHMAR, hASSAN, aNAS, aSHER AND aHMAD."

def swap_case(str):
    result = str.swapcase()
    return result

print(swap_case(names))

def case_fold(str):
    result = str.casefold()
    return result

print(case_fold(names))

def title_case(str):
    result = str.title()
    return result

print(title_case(case_name))