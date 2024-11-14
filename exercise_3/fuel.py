def get_percent(prompt):
    while True:
        try:
            user_input = input(prompt)
            proper_fraction = user_input.find('/');
            is_proper_fraction = True if proper_fraction > 0 else False
            
            if not is_proper_fraction:
                print("Value is not a proper fraction!")
                break

            values = user_input.split("/")
            x = int(values[0])
            y = int(values[1])

            percentage = int((x / y) * 100)
            
            if percentage > 50:
                print("F (Tank is almost full)")
            elif percentage == 50:
                print("Tank is half full")
            else:
                print('E (tank is almost empty)')

            print(f"Percentage: {percentage}%")
            break
        except:
            pass

get_percent("Enter a fraction: ")