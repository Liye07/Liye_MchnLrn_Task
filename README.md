# Machine Learning Task

This project demonstrates a simple machine learning application using linear regression to predict house prices based on size.

It generates synthetic data for house sizes (ranging from 1000 to 5000 square feet) and calculates prices with some noise to mimic real-world variability.

The data is organized into a pandas DataFrame, where features (size) and target variables (price) are separated.

The dataset is split into training (80%) and testing (20%) sets to ensure an unbiased evaluation of the model.

A linear regression model is trained on the training data to learn the relationship between house sizes and prices.

The model then makes predictions on the testing set, which is evaluated using Mean Squared Error (MSE) to quantify performance, with lower values indicating better accuracy.

Finally, a scatter plot visualizes the actual versus predicted prices, enhancing the understanding of the model's effectiveness.

Overall, this project provides a clear example of how to implement and evaluate a basic machine learning model.

    

# How to set the machine learning task on your own machine

1. Install Python on your pc.

2. Set up a virtual environment:

    - Open your terminal or command prompt.
    - Create a virtual environment by typing "python -m venv myenv".
    - Activate the virtual environment:
        + On Windows, type "myenv\Scripts\activate".
        + On macOS/Linux, type "source myenv/bin/activate".

3. Install the required libraries by running "pip install pandas numpy matplotlib scikit-learn".

4. Download the project code file 'house_price_prediction.py' to your local machine.

5. Run the code:

    Navigate to the directory where the code file is located.
    Type "python house_price_prediction.py" to execute the code.

6. View the results:

    Check the terminal for the Mean Squared Error output.

    A scatter plot will also appear, showing the actual versus predicted house prices.
