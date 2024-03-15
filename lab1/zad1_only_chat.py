#prompts
#1
#Write a python program that will ask a user for his name and his birthday. then proceed to calculate the number of days, which is represented as "t" argument) he's been alive and based on that calculate his physical wave as sin((2 pi/23)*t), emotional wave as sin((2 pi/28)*t) and intellectual wave as sin((2 pi/33)*t) and print out a message welcoming the user with his name, number of days, and printing out the results of all three waves with a comment, if the result is above 0.5 ("Nice keep it up!), result between 0.5 and -0.5 ("Regular result"), result below -0.5 ("ohh bad day, it will get better") 
#2
#we also want to print out the actual results of waves


import math

def calculate_waves(t):
    physical_wave = math.sin((2 * math.pi / 23) * t)
    emotional_wave = math.sin((2 * math.pi / 28) * t)
    intellectual_wave = math.sin((2 * math.pi / 33) * t)
    return physical_wave, emotional_wave, intellectual_wave

def interpret_result(result):
    if result > 0.5:
        return "Nice, keep it up!"
    elif result < -0.5:
        return "Ohh, bad day, it will get better."
    else:
        return "Regular result."

def main():
    name = input("What is your name? ")
    birthday = input("What is your birthday (YYYY-MM-DD)? ")
    
    # Calculate number of days alive
    today_date = "2024-03-15"  # Current date for demonstration
    # Replace with actual current date in real-world scenario
    days_alive = (datetime.datetime.strptime(today_date, "%Y-%m-%d") - datetime.datetime.strptime(birthday, "%Y-%m-%d")).days
    
    physical_wave, emotional_wave, intellectual_wave = calculate_waves(days_alive)
    
    print(f"Welcome, {name}!")
    print(f"You have been alive for {days_alive} days.")
    print("Physical wave:", interpret_result(physical_wave), physical_wave)
    print("Emotional wave:", interpret_result(emotional_wave), emotional_wave)
    print("Intellectual wave:", interpret_result(intellectual_wave), intellectual_wave)

if __name__ == "__main__":
    import datetime
    main()
