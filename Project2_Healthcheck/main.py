import time

print("Welcome tp QuickHealth Pro Max – Terminal Edition")
print()

print("No loops. No functions. Just pure beginner Python logic ✨")
print()
print()

print("👋 Hello there! Let's check how you're doing today.")


#Coolect user's peronal details

print("👤 Personal Details")

name = input("Your name:").strip()
gender = input("Gender (male / female / other): ").strip()
age = int(input("Age:"))
city = input("Your city (for nearby care suggestions):").strip()


# Convert name and city for formatting
name_clean = name.title()
city_title = city.title()

# gather user's health inputs

print("🤒 Symptoms & Health Info")
symptom = input("Select all symptoms you're experiencing: (fever, cough, fatigue, headache, chest pain, breathlessness): ").strip()
symptom = input("Which one is more troubling: (headache, fatigue):").strip()
temperature = float(input("🌡️ Body Temperature (°F):"))
sick_days = int(input("📅 Days you’ve felt unwell:"))
smoking = input("🚬 Do you smoke? (Yes / No): ").strip()
sleep_hours = float(input("🛌 Hours of sleep last night:"))
mood = input("🧠 Current Mood:(calm, anxious, sad, irritable):").strip()
pre_existingcondition = input("🏥 Do you have any pre-existing conditions? (Yes / No):").strip()


# Risk scoring logic

# ⚙️ 3. Risk Scoring Logic
print("\n⚙️ Analyzing...")
print("🧾 Your Health Summary")

risk_score = 0

# Fever ≥ 102°F or sick > 3 days then +3
if temperature >= 102 or sick_days > 3:
    risk_score =risk_score + 3

# Age ≥ 60 with fever then +2
if age >= 60 and symptom == "fever":
    risk_score =risk_score + 2

# Cough ≥ 5 days then +2
if symptom == "cough" and sick_days >= 5:
    risk_score =risk_score + 2

# Fatigue and age > 30 then +2
if symptom == "fatigue" and age > 30:
    risk_score =risk_score + 2

# Headache with temp > 100°F then +2
if symptom == "headache" and temperature > 100:
    risk_score =risk_score + 2

# Chest pain then +3
if symptom == "chest pain":
    risk_score = risk_score + 3

# Breathlessness then +4
if symptom == "breathlessness":
    risk_score =risk_score + 4

# Smoker then +2
if smoking == "yes":
    risk_score =risk_score + 2

# Sleep < 6 hrs then +1
if sleep_hours < 6:
    rrisk_score =risk_score + 1

# Mood = anxious/sad/irritable then +1
if mood == "anxious" or mood == "sad" or mood == "irritable":
    risk_score =risk_score + 1

# Pre-existing conditions = yes then +2
if pre_existingcondition == "yes":
    risk_score =risk_score + 2


# health risk result

print("\n📊 Health Risk Result")

if risk_score <= 3:
    print("🟢 Low Risk – Keep taking care of yourself! 💚")
elif risk_score <= 6:
    print("🟠 Moderate Risk – Monitor your health and consider seeing a doctor. 🧡")
else:
    print("🔴 High Risk – Please consult a healthcare professional immediately. ❤️")








