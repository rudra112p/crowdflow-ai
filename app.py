from flask import Flask, render_template, request
import joblib
import pandas as pd


app = Flask(__name__)

model = joblib.load("models/random_forest_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/insights")
def insights():
    return render_template("insights.html")


def convert_to_time_slot(time_value):
    if not time_value:
        return "0830-0845"

    hour, minute = map(int, time_value.split(":"))

    start_minute = (minute // 15) * 15

    start_hour = hour
    end_hour = hour
    end_minute = start_minute + 15

    if end_minute == 60:
        end_minute = 0
        end_hour = (hour + 1) % 24

    start = f"{start_hour:02d}{start_minute:02d}"
    end = f"{end_hour:02d}{end_minute:02d}"

    return f"{start}-{end}"


@app.route("/predict", methods=["GET", "POST"])
def predict():

    prediction = None
    crowd_level = None
    message = None
    advice = None

    origin = ""
    destination = ""
    selected_day = ""
    selected_time = ""
    time_slot = ""

    if request.method == "POST":

        origin = request.form.get("origin", "").strip()
        destination = request.form.get("destination", "").strip()
        selected_day = request.form.get("day", "")
        selected_time = request.form.get("time", "")

        time_slot = convert_to_time_slot(selected_time)

        model_input = pd.DataFrame([{
            "From Station": origin,
            "To Station": destination,
            "Line": "Bakerloo",
            "Dir": "SB",
            "Day_Type": selected_day,
            "Time_Slot": time_slot
        }])

        result = model.predict(model_input)

        prediction = round(float(result[0]), 2)

        if prediction <= 112:
            crowd_level = "Low"
            message = "Passenger demand is expected to be relatively low."
            advice = "This may be a more comfortable period to travel."

        elif prediction <= 352:
            crowd_level = "Moderate"
            message = "Passenger demand is expected to be moderate."
            advice = "Normal passenger activity is expected during this period."

        elif prediction <= 700:
            crowd_level = "High"
            message = "Passenger demand is expected to be high. The journey may feel busy."
            advice = "If your journey is flexible, consider checking a nearby departure time."

        else:
            crowd_level = "Very High"
            message = "Very high passenger demand is expected."
            advice = "Consider travelling at another time if your journey is flexible."

    return render_template(
        "predict.html",
        prediction=prediction,
        crowd_level=crowd_level,
        message=message,
        advice=advice,
        origin=origin,
        destination=destination,
        selected_day=selected_day,
        selected_time=selected_time,
        time_slot=time_slot
    )


@app.route("/recommendation")
def recommendation():

    origin = request.args.get("origin", "")
    destination = request.args.get("destination", "")
    selected_time = request.args.get("time", "")
    prediction = request.args.get("prediction", "")
    crowd_level = request.args.get("crowd_level", "")

    return render_template(
        "recommendation.html",
        origin=origin,
        destination=destination,
        selected_time=selected_time,
        prediction=prediction,
        crowd_level=crowd_level
    )


if __name__ == "__main__":
    app.run(debug=True)