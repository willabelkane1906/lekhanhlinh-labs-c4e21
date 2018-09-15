from flask import Flask, render_template
app = Flask(__name__)
@app.route("/bmi/<int:height>/<int:weight>")
def calculate(height, weight):
    m_height = height * 0.01
    BMI = weight / (m_height * m_height)
    
    if BMI < 16:
        cond = "severely underweight"
    elif BMI > 16 and BMI < 18.5:
        cond = "underweight"    
    elif BMI > 18.5 and BMI < 25:
        cond = "normal"
    elif BMI > 25 and BMI < 30:
        cond = "overweight"
    elif BMI > 30:
        cond = " obese"

    return render_template("bmi.html", bmi=BMI, cond=cond  )

print("runing app")
if __name__ == "__main__":
    app.run(debug=True)