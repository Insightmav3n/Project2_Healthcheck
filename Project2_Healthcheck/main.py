import time

print("Welcome tp QuickHealth Pro Max")
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

print("\n⚙️ Analyzing...")
print("🧾 Your Health Summary")

time.sleep(2)
print("=" * 60)

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


#  Personalized Advice

print("\n📌 Personalized Advice")
# Female and age ≥ 45 → recommend health screening Male and smoker → suggest quitting smoking Sleep < 6 → suggest getting more rest Mood = anxious → suggest relaxation/breathing Pre-existing conditions → suggest medical attention 

if gender == 'female' and age >= 45:
   print("Suggestion: Please consult a primary care physician for a health screening.")

elif gender == 'male' and smoking=='Yes':
    print("Suggestion: For better health, we suggest you quit smoking.")

elif sleep_hours < 6:
    print("Suggestion: It would be better if you rest more.")

elif mood == 'anxious':
    print("Suggestion: Try relaxation and breathing techniques to uplift your mood.")

elif pre_existingcondition == 'Yes':
    print("🔴 Caution: With pre-existing conditions, regular medical attention is important. Please consult your doctor.")


print(f"🏥 For urgent care near you in {city.title()}, consider visiting your nearest walk-in clinic or using a local health directory.")

print()

print("🧠 Mental Wellness Tip")
print("Take 10 minutes for yourself. Music, meditation, or even silence can help.")

print()
print()

print(f"✅ Thank you {name_clean} for using QuickHealth Pro Max. Get well soon! 💙")










