from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!"
    else:
        anger = response["anger"]
        disgust = response["disgust"]
        fear = response["fear"]
        joy = response["joy"]
        sadness = response["sadness"]
        dominant = f"<b>{response['dominant_emotion']}</b>"

        output = (
            f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant}."
        )
        return output

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
