# Data Pipeline

A collection of Python examples and exercises demonstrating object-oriented programming (OOP), data handling, serialization, deserialization, and various programming concepts. This repository serves as a learning resource for building data pipelines and understanding Python fundamentals.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [constraction_example.py](https://github.com/RayhanShajib/datapipeline/blob/main/constraction_example.py)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## datapipeline/
|-- [constraction_example.py](https://github.com/RayhanShajib/datapipeline/blob/main/constraction_example.py)
├── - [menu_driven.py](https://github.com/RayhanShajib/datapipeline/blob/main/menu_driven.py)
├── - [oop1.py](https://github.com/RayhanShajib/datapipeline/blob/main/oop1.py)
├── [oop2.py](https://github.com/RayhanShajib/datapipeline/blob/main/oop2.py)
├── [sodaBottle.py](https://github.com/RayhanShajib/datapipeline/blob/main/sodaBottle.py)
├── [1_inventory](https://github.com/RayhanShajib/datapipeline/tree/main/1_inventory)
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

### File Structure Details

- `file_handler.py`: Utility class for reading files
- `inventory.csv`: Sample CSV data with items (name, value, category, weight)
- `*.py` files: Main execution scripts and class definitions

## Dependencies

- Python 3.8+
- Built-in modules: `dataclasses`, `os`, `typing.`

No external packages are required.
