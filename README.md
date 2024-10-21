# House Price Prediction Model
## Overview
**This repository contains a machine learning model for predicting house prices using Python, scikit-learn, and TensorFlow. The model is trained on a dataset of house features and sale prices, and can be used to make predictions on new, unseen data.**

## Getting Started
### Prerequisites
1. Python 3.6 or later
2. scikit-learn 0.23 or later
3. TensorFlow 2.3 or later
4. pandas 1.1 or later
5. numpy 1.19 or later
6. matplotlib 3.3 or later
### Installation
1. Clone the repository: 'git clone https://github.com/Muskaan-Aggarwal/house-price-prediction.git'

### Running the Model
1. Run the training.py script to train the model: python training.py
2. Run the evaluating.py script to make predictions on new data: python evaluating.py
## Dataset
The dataset used to train the model is a sample dataset of house features and sale prices. The dataset is split into training and testing sets, with 80% of the data used for training and 20% used for testing.

## Model Architecture
The model is a neural network with the following architecture:

1. Input layer: 16 features (13 continuous, 3 categorical)
2. Hidden layer: 64 units, ReLU activation
3. Output layer: 1 unit, linear activation
   
The model is trained using the mean squared error loss function and the Adam optimizer.

## Performance

The model achieves a mean squared error of 0.12 on the testing set.

## Usage
To use the model, simply run the evaluating.py script and pass in the features of the house you want to predict the price for. For example:
![Screenshot 2024-07-11 002850](https://github.com/Muskaan-Aggarwal/house-price-predictor/assets/146640075/67d9dca7-526e-4bfe-a7c8-fca1e74c2b64)

The script will output the predicted sale price of the house.

## Contributing
Contributions are welcome! If you'd like to contribute to the model or suggest improvements, please open an issue or submit a pull request.

## Acknowledgments
This model was developed using the following resources:

1. Scikit-learn documentation
2. TensorFlow documentation
3. Kaggle house prices dataset
