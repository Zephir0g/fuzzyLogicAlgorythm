import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definition of fuzzy sets for temperature
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['medium'] = fuzz.trimf(temperature.universe, [0, 50, 100])
temperature['high'] = fuzz.trimf(temperature.universe, [50, 100, 100])
temperature['extremely high'] = fuzz.trimf(temperature.universe, [75, 100, 100])
temperature['extremely low'] = fuzz.trimf(temperature.universe, [0, 0, 10])

# Definition of fuzzy sets for wind speed
wind_speed = ctrl.Antecedent(np.arange(0, 101, 1), 'wind_speed')
wind_speed['slow'] = fuzz.trimf(wind_speed.universe, [0, 0, 50])
wind_speed['medium'] = fuzz.trimf(wind_speed.universe, [0, 50, 100])
wind_speed['fast'] = fuzz.trimf(wind_speed.universe, [50, 100, 100])

# Determination of fuzzy sets for material melting probability
probability = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'probability')
probability['not melt'] = fuzz.trimf(probability.universe, [0, 0, 0.5])
probability['partial melt'] = fuzz.trimf(probability.universe, [0, 0.5, 1])
probability['complete melt'] = fuzz.trimf(probability.universe, [0.5, 1, 1])

# Plotting the membership functions
temperature.view()
wind_speed.view()
probability.view()
# show the chart
plt.show()

# Determination of fuzzy rules
rule1 = ctrl.Rule(temperature['extremely low'] & wind_speed['slow'], probability['not melt'])
rule2 = ctrl.Rule(temperature['extremely low'] & wind_speed['medium'], probability['not melt'])
rule3 = ctrl.Rule(temperature['extremely low'] & wind_speed['fast'], probability['partial melt'])
rule4 = ctrl.Rule(temperature['low'] & wind_speed['slow'], probability['not melt'])
rule5 = ctrl.Rule(temperature['low'] & wind_speed['medium'], probability['partial melt'])
rule6 = ctrl.Rule(temperature['low'] & wind_speed['fast'], probability['partial melt'])
rule7 = ctrl.Rule(temperature['medium'] & wind_speed['slow'], probability['partial melt'])
rule8 = ctrl.Rule(temperature['medium'] & wind_speed['medium'], probability['partial melt'])
rule9 = ctrl.Rule(temperature['medium'] & wind_speed['fast'], probability['complete melt'])
rule10 = ctrl.Rule(temperature['high'] & wind_speed['slow'], probability['partial melt'])
rule11 = ctrl.Rule(temperature['high'] & wind_speed['medium'], probability['partial melt'])
rule12 = ctrl.Rule(temperature['high'] & wind_speed['fast'], probability['partial melt'])
rule13 = ctrl.Rule(temperature['extremely high'] & wind_speed['slow'], probability['not melt'])
rule14 = ctrl.Rule(temperature['extremely high'] & wind_speed['medium'], probability['partial melt'])
rule15 = ctrl.Rule(temperature['extremely high'] & wind_speed['fast'], probability['partial melt'])

# Creating a control system
melt_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8,
                                rule9, rule10, rule11, rule12, rule13, rule14, rule15])

# Creating a control system simulator
melt_simulation = ctrl.ControlSystemSimulation(melt_ctrl)

# Setting the input values
melt_simulation.input['temperature'] = 35
melt_simulation.input['wind_speed'] = 2.5

# Calculating the result
melt_simulation.compute()

# Printing the result
print(melt_simulation.output['probability'])

# Displaying the obtained membership function for probability
probability.view(sim=melt_simulation)
