from flask import Flask, request, jsonify
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "running", "message": "API is live"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        student_data = CustomData(
            gender=data["gender"],
            race_ethnicity=data["race_ethnicity"],
            parental_level_of_education=data["parental_level_of_education"],
            lunch=data["lunch"],
            test_preparation_course=data["test_preparation_course"],
            reading_score=float(data["reading_score"]),
            writing_score=float(data["writing_score"])
        )

        input_df = student_data.get_data_as_data_frame()
        pipeline = PredictPipeline()
        prediction = pipeline.predict(input_df)

        # Ensure JSON serializable
        predicted_value = float(prediction[0])

        return jsonify({
            "success": True,
            "predicted_math_score": round(predicted_value, 2)
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
