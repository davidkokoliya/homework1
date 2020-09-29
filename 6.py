a = int(input("First day result "))
b = int(input("Desired result "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"You will get desired result at %.d day" % result_days)