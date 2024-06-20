
def check_compliance():
    compliance = input("__________ is the process of adhering to internal standards and external regulations and enables organizations to avoid fines and security breaches.\n Enter the missing word!: ")
    if compliance == "compliance":
        return True
    else:
        return False
    
def check_security_frameworks():
    security_frameworks = input("________ __________ are guidelines used for building plans to help mitigate risks and threats to data and privacy.\n Please enter the missing word: ")
    if security_frameworks == "security frameworks":
        return True
    else:
        return False
    
#calling the function

result = check_compliance()
print(result)
result = check_security_frameworks()
print(result)
