def time_converter(hour, minute, period):
    # Converting 12-hour time to 24-hour time

    if period == "am" and hour == 12:  # if midnight the hour should be set to 0
        hour = 0

    elif period == "pm" and hour <= 12:  # if it is PM and not already in 24-hour time, add 12 to the hour
        hour += 12

    # Formating of the hour and minute to have 2 digits 
    return f"{hour:02d}{minute:02d}"

# different test cases
print(time_converter(12, 00, "am"))  
print(time_converter(8, 30, "am"))  
print(time_converter(8, 30, "pm"))
