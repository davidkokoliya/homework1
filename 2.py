time = int(input("Insert Time in Sec "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Time in format hrs:min:sec   {hours} : {minutes} : {seconds}")