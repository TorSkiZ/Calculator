# Overview
This repository contains a simple Python script that provides various functionalities related to linear functions and the mathematical constant π (pi). The script offers a text-based menu through which users can perform different calculations and visualizations.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Menu Options](#menu-options)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- Drawing a Linear Function: Visualizes a linear function based on user-provided coefficients.
- Checking Perpendicularity: Determines if two linear functions are perpendicular.
- Checking Parallelism: Determines if two linear functions are parallel or overlapping.
- Determining Function Behavior: Identifies if a linear function is constant, increasing, or decreasing.
- Printing π: Displays π to a user-specified number of decimal places.

## Requirements
- Python 3.x
- `arcade` library
- `mpmath` library

## Installation
### For Debian 12 Bookworm and similar
1. Clone the Repository
```
git clone https://github.com/TorSkiZ/calculator.git
cd calculator
```

2. Setup a Virtual Environment
```
sudo apt install python[x.xx]-venv (x.xx - Your version of Python)
python3 -m venv venv
```

3. Enter the Virtual Environment:
```
source venv/bin/activate
```

4. Install Dependencies
```
pip install arcade mpmath
```

## Usage
1. Enter the Virtual Environment:
```
source venv/bin/activate
```

2. Run the Script:
```
python3 main.py
```

3. Select an Option:
   - Follow the on-screen menu to choose the type of calculation or visualization you want to perform.
   - Enter the required coefficients or values when prompted.

## Menu Options
1. Drawing a Linear Function:
   - Enter the coefficients a and b when prompted.
   - A new window will open displaying the graph of the function y = ax + b.

2. Are Linear Functions Perpendicular?:
   - Enter the coefficients a1, b1 for the first function and a2, b2 for the second function.
   - The script will output whether the functions are perpendicular.

3. Are Linear Functions Parallel?:
   - Enter the coefficients a1, b1 for the first function and a2, b2 for the second function.
   - The script will output whether the functions are parallel or overlapping.

4. Is the Linear Function Constant, Increasing, or Decreasing?:
   - Enter the coefficients a and b.
   - The script will indicate whether the function is constant, increasing, or decreasing.

5. Print π:
   - Enter the number of decimal places to display.
   - The script will print π to the specified accuracy and the time taken for the calculation.

## Code Structure
- `draw_axes()`: Draws the coordinate axes for the graph.
- `draw_function(a, b)`: Draws the linear function y = ax + b.
- `menu()`: Displays the menu and handles user input.
- `option1()`: Handles the drawing of a linear function.
- `option2()`: Checks if two linear functions are perpendicular.
- `option3()`: Checks if two linear functions are parallel.
- `option4()`: Determines if a linear function is constant, increasing, or decreasing.
- `option5()`: Prints π to a specified number of decimal places.
- `invalid_option()`: Handles invalid menu options.

## Contributing
Contributions are welcome! If you have any suggestions or find any issues, please open an issue or submit a pull request. Please ensure your contributions align with the project's goals and coding standards.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contact
If you have any feedback, please reach out to me at wiktor.wasinski@wiciu.pl
