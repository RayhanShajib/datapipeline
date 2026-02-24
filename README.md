<<<<<<< HEAD
# datapipeline
# 4 Pillars

OOP Basic Pillars

1. Inheritance
2. Abstraction
3. Polymorphism
4. Encapsulation


=======
# Data Pipeline

A collection of Python examples and exercises demonstrating object-oriented programming (OOP), data handling, serialization, deserialization, and various programming concepts. This repository serves as a learning resource for building data pipelines and understanding Python fundamentals.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Object-Oriented Programming Examples**: Basic classes like Person, Car, User, and SodaBottle
- **Data Handling**: File reading, CSV processing, inventory management
- **Serialization/Deserialization**: Converting objects to/from CSV format
- **Menu-Driven Applications**: Interactive console-based menus
- **Utility Classes**: Temperature converter, coin acceptor, counter
- **Data Pipeline Concepts**: Reading, processing, and writing data

## Project Structure

```
datapipeline/
├── README.md
├── constraction_example.py          # Class vs instance attributes example
├── menu_driven.py                   # Menu-driven application example
├── oop1.py                          # Basic OOP with Person class
├── oop2.py                          # Using SodaBottle class
├── sodaBottle.py                    # SodaBottle class implementation
├── 1_inventory/                     # Basic inventory management
│   ├── file_handler.py
│   ├── inventory.csv
│   └── main.py
├── 2_deserialization/               # CSV deserialization to objects
│   ├── file_handler.py
│   ├── inventory.csv
│   ├── item.py
│   └── main.py
├── 3_serialization/                 # Object serialization to CSV
│   ├── file_handler.py
│   ├── inventory.csv
│   ├── Item.py
│   └── main.py
├── car/                             # Car class example
│   ├── car.py
│   └── main.py
├── user/                            # User class example
│   ├── main.py
│   └── user.py
└── WO tasks/                        # Work order tasks
    ├── coinAcceptor/
    │   ├── coin_acceptor.py
    │   └── main.py
    ├── coinAcceptorCLI/
    │   ├── coin_acceptor.py
    │   └── main.py
    ├── counter/
    │   ├── counter.py
    │   └── main.py
    ├── temperatureConverter/
    │   ├── main.py
    │   └── temperature_converter.py
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RayhanShajib/datapipeline.git
   cd datapipeline
   ```

2. Ensure Python 3.8+ is installed on your system.

3. No additional dependencies are required for most examples, but for advanced features, you may need:
   - dataclasses (built-in for Python 3.7+)

## Usage

### Running Individual Examples

Each module can be run independently. Navigate to the desired directory and execute the `main.py` file:

```bash
python main.py
```

### Specific Examples

#### Menu-Driven Application

```bash
python menu_driven.py
```

Displays a simple menu with options to print "Hello, World!" or exit.

#### OOP Examples

- `oop1.py`: Creates and displays a Person object
- `oop2.py`: Demonstrates SodaBottle class usage
- `constraction_example.py`: Shows class vs instance attributes

#### Data Pipeline Examples

1. **Basic Inventory** (`1_inventory/`):
   - Reads inventory from CSV
   - Displays items

2. **Deserialization** (`2_deserialization/`):
   - Reads CSV data
   - Creates Item objects from CSV rows
   - Displays item prices

3. **Serialization** (`3_serialization/`):
   - Reads CSV data
   - Deserializes to Item objects
   - Can serialize objects back to CSV format

#### Utility Classes

- **Car** (`car/`): Basic car simulation
- **User** (`user/`): User management
- **Temperature Converter** (`WO tasks/temperatureConverter/`): Convert between Celsius, Fahrenheit, and Kelvin
- **Coin Acceptor** (`WO tasks/coinAcceptor/`): Simulate coin insertion and acceptance
- **Counter** (`WO tasks/counter/`): Simple counter functionality

### File Structure Details

- `file_handler.py`: Utility class for reading files
- `inventory.csv`: Sample CSV data with items (name, value, category, weight)
- `*.py` files: Main execution scripts and class definitions

## Dependencies

- Python 3.8+
- Built-in modules: `dataclasses`, `os`, `typing`

No external packages are required.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
>>>>>>> a87e64e (readme.md file recreated)
