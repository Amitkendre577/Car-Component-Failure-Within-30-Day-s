from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model and preprocessor
model = joblib.load('randomforest_model .joblib')  # Random Forest model
preprocessor = joblib.load('preprocessor.joblib')  # ColumnTransformer pipeline

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get form inputs
            component = request.form['component']
            mileage = request.form['mileage']
            car_age = request.form['car_age']
            part_age = request.form['part_age']
            temp_exp = request.form['temp_exposure']
            service_count = request.form['service_count']
            driving_style = request.form['driving_style']

            # Validate all fields
            if not all([component, mileage, car_age, part_age, temp_exp, service_count, driving_style]):
                raise ValueError("Please fill in all fields.")

            # Convert numeric inputs
            mileage = float(mileage)
            car_age = float(car_age)
            part_age = float(part_age)
            temp_exp = float(temp_exp)
            service_count = int(service_count)

            # Create a DataFrame with correct column names
            input_df = pd.DataFrame([{
                'Component': component,
                'Mileage': mileage,
                'Car_Age': car_age,
                'Part_Age': part_age,
                'Temp_Exposure': temp_exp,
                'Service_Count': service_count,
                'Driving_Style': driving_style
            }])

            # Preprocess input
            transformed_input = preprocessor.transform(input_df)

            # Predict
            prediction = model.predict(transformed_input)[0]
            result = "will FAIL within 30 days" if prediction == 1 else "will NOT fail within 30 days"

            return render_template('result.html', prediction_text=f'{component} {result}.')

        except Exception as e:
            return render_template('result.html', prediction_text=f'Error: {str(e)}')

    return render_template('predict.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == "__main__":
    app.run(debug=True)
