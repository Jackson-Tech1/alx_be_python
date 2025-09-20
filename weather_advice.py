test_conditions = ["sunny", "rainy", "cold", "windy"]
def give_recommendation(weather):
weather = weather.lower()
if weather == "sunny":
return "Wear a t-shirt and sunglasses."
elif weather == "rainy":
return "Don't forget your umbrella and a raincoat."
elif weather == "cold":
return "Make sure to wear a warm coat and a scarf."
else:
return "Sorry, I don't have recommendations for this weather."
for condition in test_conditions:
print(f"Input: {condition}")
print(f"Output: {give_recommendation(condition)}\n")
