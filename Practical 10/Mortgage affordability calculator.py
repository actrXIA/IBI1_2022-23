def house_afford(value, salary):
    """Determines if a house is affordable(5 times the salary)."""
    if value <= 5 * salary:
        return "Yes"
    else:
        return "No"

house_value = 180000
salary = 35000
can_afford = house_afford (house_value, salary)
print(can_afford)
