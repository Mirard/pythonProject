user_time = int(input("Введите секунды >>> "))

hours = user_time // 3600
mins = (user_time % 3600) // 60
secs = (user_time % 3600) % 60

if hours // 10 > 0:
    if mins // 10 > 0:
        if secs // 10 > 0:
            print(f"Время: {hours}:{mins}:{secs}")
        else:
            print(f"Время: {hours}:{mins}:0{secs}")
    else:
        if secs // 10 > 0:
            print(f"Время: {hours}:0{mins}:{secs}")
        else:
            print(f"Время: {hours}:0{mins}:0{secs}")
else:
    if mins // 10 > 0:
        if secs // 10 > 0:
            print(f"Время: 0{hours}:{mins}:{secs}")
        else:
            print(f"Время: 0{hours}:{mins}:0{secs}")
    else:
        if secs // 10 > 0:
            print(f"Время: 0{hours}:0{mins}:{secs}")
        else:
            print(f"Время: 0{hours}:0{mins}:0{secs}")

print("Время вариант2: {:>02}:{:>02}:{:>02}".format(hours, mins, secs))
