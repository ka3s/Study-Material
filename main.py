
#question 1
def check_compliance():
    compliance = input("__________ is the process of adhering to internal standards and external regulations and enables organizations to avoid fines and security breaches.\n What is the answer to this question?: ")
    if compliance == "compliance":
        return True
    else:
        return False
    
#question 2
def check_security_frameworks():
    security_frameworks = input("________ __________ are guidelines used for building plans to help mitigate risks and threats to data and privacy.\n What is the answer to this question?: ")
    if security_frameworks == "security frameworks":
        return True
    else:
        return False

#question 3
def check_security_controls():
    security_controls = input("________ ________ are safeguards designed to reduce specific security risks. They are used with security frameworks to establish a strong security posture.\n What is the answer to this question?: ")
    if security_controls == "security controls":
        return True
    else:
        return False

#question 4
def check_security_posture():
    security_posture = input("________ _______ is an organization’s ability to manage its defense of critical assets and data and react to change. A strong security posture leads to lower risk for the organization.\n What is the answer to this question?: ")
    if security_posture == "security posture":
        return True
    else:
        return False
    
#question 5
def check_threat_actor():
    threat_actor = input("A ______ _____, or malicious attacker, is any person or group who presents a security risk. This risk can relate to computers, applications, networks, and data.\n What is the answer to this question?: ")
    if threat_actor == "threat actor":
        return True
    else:
        return False

#question 6
def check_internal_threat():
    internal_threat = input("an ________ ______ can be a current or former employee, an external vendor, or a trusted partner who poses a security risk. At times, an internal threat is accidental. For example, an employee who accidentally clicks on a malicious email link would be considered an accidental threat. Other times, the internal threat actor intentionally engages in risky activities, such as unauthorized data access.\n What is the answer to this question?: ")
    if internal_threat == "internal threat":
        return True
    else:
        return False

#question 7
def check_network_security():
    network_security = input("_______ ________ is the practice of keeping an organization's network infrastructure secure from unauthorized access. This includes data, services, systems, and devices that are stored in an organization’s network.\n What is the answer to this question?: ")
    if network_security == "network security":
        return True
    else:
        return False

#question 8
def check_cloud_security():
    cloud_security = input("_____ ________ is the process of ensuring that assets stored in the cloud are properly configured, or set up correctly, and access to those assets is limited to authorized users. The cloud is a network made up of a collection of servers or computers that store resources and data in remote physical locations known as data centers that can be accessed via the internet. Cloud security is a growing subfield of cybersecurity that specifically focuses on the protection of data, applications, and infrastructure in the cloud.\n What is the answer to this question?: ")
    if cloud_security == "cloud security":
        return True
    else:
        return False
    
#question 9
def check_programming():
    programming = input("___________ is a process that can be used to create a specific set of instructions for a computer to execute tasks. These tasks can include: \n *Automation of repetitive tasks (e.g., searching a list of malicious domains)\n *Reviewing web traffic\n *Alerting suspicious activity\n What is the answer to this question?: ")
    if programming == "programming":
        return True
    else:
        return False

#calling the function

result = check_compliance()
print(result)

result = check_security_frameworks()
print(result)

result = check_security_controls()
print(result)

result = check_security_posture()
print(result)

result = check_threat_actor()
print(result)

result = check_internal_threat()
print(result)

result = check_network_security()
print(result)

result = check_cloud_security()
print(result)

result = check_programming()
print(result)
