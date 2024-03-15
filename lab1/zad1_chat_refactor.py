from datetime import datetime
import math #tego czat zapomnial dodac w refactorze

def get_date_object(dob_str):
    return datetime.strptime(dob_str, "%d-%m-%Y")

def calculate_wave(period, difference_days):
    return math.sin((2 * math.pi / period) * difference_days)

def get_feedback(wave_result):
    if wave_result <= 1 and wave_result > 0.5:
        print("Super wynik! Gratulacje!")
    elif wave_result <= 0.5 and wave_result >= -0.5:
        print("Zwykły wynik.")
    elif wave_result < 0.5 and wave_result > -1:
        print("Słabo... Będzie lepiej.")

def print_results(name, dob, difference):
    print(f"Witaj, {name}! Urodziłeś się {dob}. To było {difference.days} dni temu.")
    print("Wyniki fal:")
    for period, wave_type in [(23, "fizyczna"), (28, "emocjonalna"), (33, "intelektualna")]:
        wave_result = calculate_wave(period, difference.days)
        print(f"Wynik fali {wave_type}: {wave_result}")
        get_feedback(wave_result)

def main():
    name = input("Wpisz imię: ")
    dob_str = input("Wpisz datę urodzenia (DD-MM-YYYY): ")
    dob = get_date_object(dob_str)
    curr_date = datetime.now()
    difference = curr_date - dob
    print_results(name, dob, difference)

if __name__ == "__main__":
    main()
