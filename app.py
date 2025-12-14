from flask import Flask, render_template, request

app = Flask(__name__)

# Route for home page
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle form submission
@app.route("/calculate", methods=["POST"])
def calculate():
    weight = float(request.form["weight"])
    height = float(request.form["height"])

    # BMI calculation
    bmi = weight / (height ** 2)

    # BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return f"<h2>Your BMI is: {bmi:.2f}</h2><h3>Category: {category}</h3>"

if __name__ == "__main__":
    app.run(debug=True)