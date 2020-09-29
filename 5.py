profit = float(input("Insert profit "))
costs = float(input("Insert costs "))
if profit > costs:
    print(f"Company works with a profit. Rentability is  {profit / costs:.2f}")
    workers = int(input("Insert a number of workers in a company "))
    print(f"profit per one employee {profit / workers:.2f}")
elif profit == costs:
    print("Company is neither profitable or unprofitable")
else:
    print("Company is unprofitable")