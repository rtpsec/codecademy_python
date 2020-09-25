def ground_shipping_cost(weight):
  if (weight < 2):
    return weight * 1.50 + 20.00
  elif (weight > 2) and (weight <= 6):
    return weight * 3.00 + 20.00
  elif (weight > 6) and (weight <= 10):
    return weight * 4.00 + 20.00
  else:
    return weight * 4.75 + 20.00

premium_ground_shipping = 125.00

def drone_shipping_cost(weight):
  if (weight <= 2):
    return weight * 4.50 + 0.00
  elif (weight >=2) and (weight <= 6):
    return weight * 9.00 + 0.00
  elif (weight >= 6) and (weight <= 10):
    return weight * 12.00 + 0.00
  else:
    return weight * 14.25 + 0.00

def find_savings(weight):
  ground_cost=(ground_shipping_cost(weight))
  drone_cost=(drone_shipping_cost(weight))
  premium_cost=125

  if (premium_cost < ground_cost) and (premium_cost < drone_cost):
    return "premium shipping is cheaper at $125.00"
  elif (ground_cost < drone_cost) and (ground_cost < premium_cost):
    return "Ground cost is the cheapest " + str(ground_cost)
  elif (drone_cost < ground_cost) and (drone_cost < premium_cost):
    return "Drone cost is the cheapest" + drone_cost
  else:
    return "Premium Cost is the cheapest" + premium_cost

print(find_savings(41.5))
