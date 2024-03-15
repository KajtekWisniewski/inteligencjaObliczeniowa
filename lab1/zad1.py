from datetime import datetime, timedelta
import math

name = input("Wpisz imie: ")

dob = input("wpisz date urodzenia (DD-MM-YYYY): ")
datedob = datetime(int(dob[6:10]),int(dob[3:5]),int(dob[0:2]))
curr_date = datetime.now()

difference = curr_date - datedob

def calculate_wave(arg, difference_days):
    return math.sin((2*math.pi/arg)*difference_days)

def get_feedback(wave_result):
    match wave_result:
        case _ if wave_result <=1 and wave_result > 0.5:
            print("super wynik gratuluje")
        case _ if wave_result <= 0.5 and wave_result >= -0.5:
            print("zwykly wynik")
        case _ if wave_result < 0.5 and wave_result > -1:
            print("slabooo, bedzie lepiej")
    return
        
def results():
    physical_wave = calculate_wave(23, difference.days)
    emotional_wave = calculate_wave(28, difference.days)
    intellectual_wave = calculate_wave(33, difference.days)
    print("wynik fali fizycznej:", physical_wave)
    get_feedback(physical_wave)
    print("wynik fali emocjonalnej:", emotional_wave)
    get_feedback(emotional_wave)
    print("wynik fali intelektualnej:", intellectual_wave)
    get_feedback(intellectual_wave)
    return


print("witaj,", name + " urodziles sie", dob, "bylo to", difference.days, "dni temu")
results()

