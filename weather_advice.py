weather_advice = {
    "sunny": "Wear a t-shirt and sunglasses.",
    "rainy": "Don't forget your umbrella and a raincoat.",
    "cold": "Make sure to wear a warm coat and a scarf."
}

while True:
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower().strip()
    
    if weather in weather_advice:
        print(weather_advice[weather])
        break
    else:
        valid_options = ", ".join(weather_advice.keys())
        print(f"Sorry, I don't have recommendations for '{weather}'. Please choose one of these: {valid_options}.")
