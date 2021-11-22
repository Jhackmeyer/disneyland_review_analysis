from flask import Flask, render_template, request
from run_ml import predictions

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
        print((request.form["month"]))
        print((request.form["tourist_value"]))
        print((request.form["locations"]))

        month = request.form["month"]
        tourist = request.form["tourist_value"]
        location = request.form["locations"]

        prediction = predictions(month, tourist, location)

        output = prediction[0]

        results = ""

        if(output == 0):
            results = "We suggest visiting Disneyland in California!"
            img_result = "https://thumbs.dreamstime.com/b/disneyland-walt-disney-statue-princess-castle-anaheim-california-136919187.jpg"
        elif(output == 1):
            results = "We predict you would love Disneyland in Hong Kong!"
            img_result = "https://fortheloveofthemouse.com/wp-content/uploads/2020/01/40-2.jpg"
        elif(output == 2):
            results = "We highly recommend you visit Disneyland in Paris"
            img_result = "https://st.depositphotos.com/1846219/3398/i/600/depositphotos_33981847-stock-photo-beautiful-scene-in-disneyland-paris.jpg"

        print(output)
        return render_template("results.html", results=results, img_result=img_result)



