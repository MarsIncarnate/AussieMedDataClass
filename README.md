# Medical Cannabis Market Trends Analysis

**Table of Contents**

- [Overview](#overview)
- [Project Description](#project-description)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is a comprehensive data analysis tool that facilitates the extraction and structuring of prescription data within Australia from 2012 to 2021. It serves as a critical component in the development of a Medical Cannabis dashboard for a client on Fiverr. The tool organizes the data in a structured and easily accessible format, providing valuable insights into market trends.

## Project Description

### Data Collection

The project begins by collecting and organizing prescription data from multiple sources. The data is classified by year and stored in individual Excel files, where each file represents a specific year's prescription data.

### Data Categorization

The project employs a categorized medication data file, `categorized_medication_data.xlsx`, which serves as a reference for medication names and their corresponding categories. The tool utilizes this reference to categorize the prescription data effectively.

### Data Population

The core functionality of this project is the data population process. The script iterates through each year's prescription data, matches it with categorized medication data, and updates the medication's corresponding category for each year. This process ensures that the data is structured for easy analysis.

### Missing Data Handling

To maintain data integrity, the tool identifies and fills missing prescription data with zeros, ensuring that the analysis is as accurate as possible.

### Data Export

The project saves the updated categorized medication data to the `categorized_medication_data.xlsx` file. This structured data is now ready for further analysis and integration into the Medical Cannabis dashboard.

## Prerequisites

Before running the project, ensure that you have the following prerequisites:

- Python (3.6 or higher)
- Pandas library
- Openpyxl library

You can install the required Python libraries using the following commands:

```bash
pip install pandas openpyxl
```

## Getting Started

Clone the repository to your local machine:
```bash
git clone https://github.com/MarsIncarnate/AussieMedDataClass.git
cd AussieMedDataClass
```

Place your prescription data files for each year (e.g., prescription_data_2012.xlsx, prescription_data_2013.xlsx) in the project directory.

Ensure that the categorized_medication_data.xlsx file is available and properly structured.

Usage
To run the data population script, execute the following command in your project directory:

```bash
python data_population.py
```

The script will process the prescription data, update the categorized medication data, and save the results to the categorized_medication_data.xlsx file.

## Project Structure
The project structure is as follows:

data_population.py: The main script for populating and structuring the data.
categorized_medication_data.xlsx: Reference file for categorized medication data.
prescription_data_YEAR.xlsx: Prescription data files for each year.
Contributing
Contributions are welcome! If you'd like to improve this project or have ideas for enhancements, please submit a pull request or open an issue.

## License
This project is licensed under the MIT License.