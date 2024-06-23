
#created a check answer function to get rid of the million if and else statements
def check_answer(question, correct_answer):
    user_answer = input(question)
    return user_answer.strip().lower() == correct_answer
 
#instead of each individual statement, added a list of questions
#dictionary to check if the answer is correct
study_qna = [
    #question 1
    {"question": "__________ is the process of adhering to internal standards and external regulations and enables organizations to avoid fines and security breaches.\n What is the answer to this question?: ", "answer": "compliance"},
    #question 2
    {"question": "________ __________ are guidelines used for building plans to help mitigate risks and threats to data and privacy.\n What is the answer to this question?: ", "answer": "security frameworks"},
    #question 3
    {"question": "________ ________ are safeguards designed to reduce specific security risks. They are used with security frameworks to establish a strong security posture.\n What is the answer to this question?: ", "answer": "security controls"},
    #question 4
    {"question": "________ _______ is an organization’s ability to manage its defense of critical assets and data and react to change. A strong security posture leads to lower risk for the organization.\n What is the answer to this question?: ", "answer": "security posture"},
    #question 5
    {"question": "A ______ _____, or malicious attacker, is any person or group who presents a security risk. This risk can relate to computers, applications, networks, and data.\n What is the answer to this question?: ", "answer": "threat actor"},
    #question 6
    {"question": "An ________ ______ can be a current or former employee, an external vendor, or a trusted partner who poses a security risk. At times, an internal threat is accidental. For example, an employee who accidentally clicks on a malicious email link would be considered an accidental threat. Other times, the internal threat actor intentionally engages in risky activities, such as unauthorized data access.\n What is the answer to this question?: ", "answer": "internal threat"},
    #question 7
    {"question": "_______ ________ is the practice of keeping an organization's network infrastructure secure from unauthorized access. This includes data, services, systems, and devices that are stored in an organization’s network.\n What is the answer to this question?: ", "answer": "network security"},
    #question 8
    {"question": "_____ ________ is the process of ensuring that assets stored in the cloud are properly configured, or set up correctly, and access to those assets is limited to authorized users. The cloud is a network made up of a collection of servers or computers that store resources and data in remote physical locations known as data centers that can be accessed via the internet. Cloud security is a growing subfield of cybersecurity that specifically focuses on the protection of data, applications, and infrastructure in the cloud.\n What is the answer to this question?: ", "answer": "cloud security"},
    #question 9
    {"question": "___________ is a process that can be used to create a specific set of instructions for a computer to execute tasks. These tasks can include: \n *Automation of repetitive tasks (e.g., searching a list of malicious domains)\n *Reviewing web traffic\n *Alerting suspicious activity\n What is the answer to this question?: ", "answer": "programming"},
    #part 4 Question 1
    {"question": "________ ________ is a software program used to prevent, detect, and eliminate malware and viruses. It is also called anti-malware.\n What is the answer to this question?: ", "answer": "antivirus software"},
    #p4 Question 2
    {"question": "________: An organized collection of information or data.\n Fill in the blank: ", "answer": "database"},
    #p4 Question 3
    {"question": "____ _____: A specific piece of information. \n Fill in the blank: ", "answer": "data point"},
    #p4 Question 4
    {"question": "_________ _________ ______: An Application that monitors system activity and alerts on possible intrusions.\n Fill in the blank: ", "answer": "Intrusion Detection System"},
    #p4 Question 5
    {"question": "__________ makes data unreadable and difficult to decode for an unauthorized user; its main goal is to ensure confidentiality of private data.\n What is the answer to this question?: ", "answer": "encryption"},
    #p4 Question 6
    {"question": "___________ _______, is the act of participating in a simulated attack that helps identify vulnerabilities in a system, network, website, application, and processes. It is a thorough risk assesment that can evaluate and identify external and internal threats as well as weaknesses.\n What is the answer to this Question?: ", "answer": "Penetration Testing"},
    #p4 Question 7
    {"question": "_____ is an open source operating system. \n What is the answer to this question?: ", "answer": "linux"},
    #p4 Question 8
    {"question": "A ___ is a record of events that occur within an organization's systems\n What is the answer to this question?: ", "answer": "log"},
    #p4 Question 9
    {"question": "_______ ________ ________: A tool designed to capture and analyze data traffic within a network\n Fill in the blank: ", "answer": "Network Protocol Analyzer"},
    #p4 Question 10
    {"question": "_______ __ _______: Is a sequence outlining the order of data that must be preserved from first to last\n Fill in the blank: ", "answer": "Order of Volatility"},
    #4q11
    {"question": "________ ___________ ___ __________: Is an application that collects and analyzes log data to monitor critical activities in an ogranization\n Fill in the blank: ", "answer": "Security Information And Management"},
    #4q12
    {"question": "___: Is a query language used to create, interact with, and request information from a database.\n Fill in the blank: ", "answer": "SQL"}

]

#calling the function here, returning results per question answered
for qna in study_qna:
    result = check_answer(qna["question"], qna["answer"])
    print(result)