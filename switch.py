def get_day_name(day):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(day, "Invalid day")  # Default value for invalid keys

# Test the function
print(get_day_name(3))  # Output: Wednesday
print(get_day_name(10)) # Output: Invalid day
