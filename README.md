# Patient Retention Prediction using Synthetic Data and Machine Learning

## Project Overview
This project predicts patient retention using synthetic data and machine learning. Synthetic datasets were generated using Python and JSON scripts to mimic real-world healthcare scenarios. The project implements advanced ML techniques to analyze patient data and provide insights for improving retention strategies.

---

## Key Features
- **Synthetic Data Generation**: Custom scripts generate realistic patient datasets, including demographic, clinical, and behavioral features.
- **Predictive Modeling**: Machine learning algorithms predict patient retention based on various features.
- **Data Exploration**: Detailed exploratory data analysis to understand key factors affecting retention.
- **Feature Engineering**: Tailored features to enhance model performance.
- **Visualization**: Insights presented through graphs and charts.

---

## Data
- **Train Data**: `Train Data - CSV.csv` (synthetic data for training models).
- **Test Data**: `Test Data - CSV.csv` and `Test Data V2.xlsx` (synthetic data for testing models).
- **Generated Data**: JSON and Python scripts (`address.json`, `dataset.py`) for generating synthetic data.

---

## Technologies Used
- **Languages**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, Scikit-learn, Faker
- **Tools**: Jupyter Notebook, JSON, CSV

---

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/patient-retention-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd patient-retention-prediction
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Jupyter Notebook:
   ```bash
   jupyter notebook ML_Model_V3.ipynb
   ```

---

## Usage
1. Generate synthetic data:
   - Run `dataset.py` and `address.py` to create synthetic datasets.
2. Train and test models:
   - Use the notebook `ML_Model_V3.ipynb` to preprocess data, train ML models, and evaluate predictions.
3. Analyze results:
   - Visualize patient retention trends and model performance using generated plots.

---

## License
This project is licensed under the [MIT License](LICENSE).
