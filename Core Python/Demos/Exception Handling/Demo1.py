try:
    no1 = int(input("enter th no1:"))
    no2 = int(input("enter th no2:"))
    print(no1//no2)
except ZeroDivisionError as e:
    print(f"Zero division {e}")
except ValueError as v:
    print(f"Value error {v}")
except Exception as e:
    print(f"Exception {e}")            