
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
]

study_qnaTwo = [
    #p2q1
    {"question": "________ ________ is a software program used to prevent, detect, and eliminate malware and viruses. It is also called anti-malware.\n What is the answer to this question?: ", "answer": "antivirus software"},
    #p2q2
    {"question": "________: An organized collection of information or data.\n Fill in the blank: ", "answer": "database"},
    #p2q3
    {"question": "____ _____: A specific piece of information. \n Fill in the blank: ", "answer": "data point"},
    #p2q4
    {"question": "_________ _________ ______: An Application that monitors system activity and alerts on possible intrusions.\n Fill in the blank: ", "answer": "Intrusion Detection System"},
    #p2q5
    {"question": "__________ makes data unreadable and difficult to decode for an unauthorized user; its main goal is to ensure confidentiality of private data.\n What is the answer to this question?: ", "answer": "encryption"},
    #p2q6
    {"question": "___________ _______, is the act of participating in a simulated attack that helps identify vulnerabilities in a system, network, website, application, and processes. It is a thorough risk assesment that can evaluate and identify external and internal threats as well as weaknesses.\n What is the answer to this Question?: ", "answer": "Penetration Testing"},
    #p2q7
    {"question": "_____ is an open source operating system. \n What is the answer to this question?: ", "answer": "linux"},
    #p2q8
    {"question": "A ___ is a record of events that occur within an organization's systems\n What is the answer to this question?: ", "answer": "log"},
    #p2q9
    {"question": "_______ ________ ________: A tool designed to capture and analyze data traffic within a network\n Fill in the blank: ", "answer": "Network Protocol Analyzer"},
    #p2q10
    {"question": "_______ __ _______: Is a sequence outlining the order of data that must be preserved from first to last\n Fill in the blank: ", "answer": "Order of Volatility"},
    #2q11
    {"question": "________ ___________ ___ __________: Is an application that collects and analyzes log data to monitor critical activities in an ogranization\n Fill in the blank: ", "answer": "Security Information And Management"},
    #2q12
    {"question": "___: Is a query language used to create, interact with, and request information from a database.\n Fill in the blank: ", "answer": "SQL"}
]

#CISSP DOMAINS

study_domains = [
    #p3q1
    {"question": "What is the first domain?: ", "answer": "security and risk management"},
    #p3q2
    {"question": "What is the second domain?: ", "answer": "asset security"},
    #p3q3
    {"question": "What is the third domain?: ", "answer": "security architecture and engineering"},
    #p3q4
    {"question": "What is the fourth domain?: ", "answer": "communication and network security"},
    #p3q5
    {"question": "What is the fifth domain?: ", "answer": "identity and access management"},
    #p3q6
    {"question": "What is the sixth domain?: ", "answer": "security assessment and testing"},
    #p3q7
    {"question": "What is the seventh domain?: ", "answer": "security operations"},
    #p3q8
    {"question": "What is the eighth domain?: ", "answer": "software development security"}
]

#Randomize the order later

study_domain_definitions = [
    #p4q1
    {"question": "The ___ domain is focused on defining security goals and objectives, risk mitigation, compliance, business continuity, and legal regulation: ", "answer": "1st"},
    #p4q2
    {"question": "The ___ domain is focused on securing digital and physical assets. It's also related to the storage, maintenance, retention, and destruction of data: ", "answer": "2nd"},
    #p4q3
    {"question": "The ___ domain is focused on optimizing data security by ensuring effective tools, systems, and processes are in place to protect an organization's assets and data: ", "answer": "3rd"},
    #p4q4
    {"question": "The ___ domain is focused on managing and securing physical networks and wireless communication: ", "answer": "4th"},
    #p4q5
    {"question": "The ___ domain is focused on access and authorization to keep data secure, by making sure users follow established policies to control and manage assets: ", "answer": "5th"},
    #p4q6
    {"question": "The ___ domain is focused on conducting security control testing, collecting and analyzing data, and conducting security audits to monitor for risks, threats, and vulnerabilities: ", "answer": "6th"},
    #p4q7
    {"question": "The ___ domain is focused on conducting investigations and implementing preventative measures: ", "answer": "7th"},
    #p4q8
    {"question": "The ___ domain is focused on using secure coding practices: ", "answer": "8th"}
]

#calling the function here, returning results per question answered
def qna_qna(study):    
    for qna in study:
        result = check_answer(qna["question"], qna["answer"])
        print(result)

def main():
    while True:
        choose_test = input("Choose which test(enter 1,2,3,4)")
        if choose_test == "1":
            qna_qna(study_qna)
            break
        elif choose_test == "2":
            qna_qna(study_qnaTwo)
            break
        elif choose_test == "3":
            qna_qna(study_domains)
            break
        elif choose_test == "4":
            qna_qna(study_domain_definitions)
            break

if __name__ == "__main__":
    main()