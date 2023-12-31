# Material Melting Prediction Using Fuzzy Logic

This Python script models the likelihood of a material melting based on two environmental factors: temperature and wind speed. The script uses fuzzy logic principles to simulate the real-world complexities and uncertainties associated with such a process.

## Dependencies

This script depends on the following Python libraries:

- matplotlib
- numpy
- scikit-fuzzy

To install these dependencies, you can use pip:

``pip install matplotlib numpy scikit-fuzzy``


## Usage

To use this script, simply run it in your Python environment. The script is currently set to simulate the scenario where the temperature is 35 degrees and the wind speed is 2.5 m/s.

```python
melt_simulation.input['temperature'] = 35
melt_simulation.input['wind_speed'] = 2.5

melt_simulation.compute()
```

The script will output a graph showing the likelihood of the material melting at the given temperature and wind speed.

