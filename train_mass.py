train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp, c_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

def c_to_f(c_temp, f_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp


f100_in_celsius = f_to_c(100, "")
c0_in_farenheit = c_to_f(0, "")


def get_force(mass, acceleration):
    mass_acceleration = mass * acceleration
    return mass_acceleration
train_force = get_force(train_mass,train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")
