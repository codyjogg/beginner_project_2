# incident report 

client_name = input("Please type the name of the client" )
age = int(input("What is the client's age?" ))
incident_type = input("Please describe the incident that took place" )
severity_level = int(input("Please rate the severity from 0 - 10" ))

# Veriables above will be what ask for the users input. btw codyjogg created this :)

if age >= 18:
    age_group = "adult"
elif age >= 13:
    age_group = "teen"
else:
    age_group = "child"


#new variable for severity_level

if severity_level >= 8:
    risk_level = "high risk"
elif severity_level >= 4:
    risk_level = "medium risk"
else: 
    risk_level = "low risk"


print("\n==============================")
print("        INCIDENT REPORT        ")
print("==============================\n")

print(f"Client Name: {client_name}")
print(f"Age: {age}")
print(f"Age Group: {age_group}")

print("------------------------------")

print(f"Incident Type: {incident_type}")

print("------------------------------")

print(f"Severity Level (Raw): {severity_level}")
print(f"Risk Level: {risk_level}")

print("\n==============================")
print("        END OF REPORT         ")
print("==============================")