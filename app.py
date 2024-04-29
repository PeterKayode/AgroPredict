# Import the libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Load the pickle model file
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# Route the Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route the register page
@app.route('/register')
def register():
    return render_template('register.html')

# Route the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route the transit page
@app.route('/transit')
def transit():
    return render_template('transit.html')

# Route the diseasepred page
@app.route('/diseasepred')
def diseasepred():
    return render_template('diseasepred.html')

# Route the fertilizerpred page
@app.route('/fertilizerpred')
def fertilizerpred():
    return render_template('fertilizerpred.html')

# Route the chatus page
@app.route('/chatus')
def chatus():
    return render_template('chatus.html')

# Route the Soil Test webpage
@app.route('/croppred')
def croppred():
    return render_template('soiltest.html')

# Route the Prediction value via the form on the Soil Test webpage
@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template('soiltest.html', prediction_text='The most suitable crop for planting on this piece of land is {}'.format(output))

# Route the rice data page
@app.route('/rice')
def rice():
    return render_template('rice.html')

# Route the maize page
@app.route('/maize')
def maize():
    return render_template('maize.html')

# Route the chickpea page
@app.route('/chickpea')
def chickpea():
    return render_template('chickpea.html')

# Route the kidney page
@app.route('/kidney')
def kidney():
    return render_template('kidney.html')

# Route the pigeon page
@app.route('/pigeon')
def pigeon():
    return render_template('pigeon.html')

# Route the moth page
@app.route('/moth')
def moth():
    return render_template('moth.html')

# Route the mung page
@app.route('/mung')
def mung():
    return render_template('mung.html')

# Route the black page
@app.route('/black')
def black():
    return render_template('black.html')

# Route the lentil page
@app.route('/lentil')
def lentil():
    return render_template('lentil.html')

# Route the pome page
@app.route('/pome')
def pome():
    return render_template('pome.html')

# Route the banana page
@app.route('/banana')
def banana():
    return render_template('banana.html')

# Route the mango page
@app.route('/mango')
def mango():
    return render_template('mango.html')

# Route the grapes page
@app.route('/grapes')
def grapes():
    return render_template('grapes.html')

# Route the water page
@app.route('/water')
def water():
    return render_template('water.html')

# Route the musk page
@app.route('/musk')
def musk():
    return render_template('musk.html')

# Route the apple page
@app.route('/apple')
def apple():
    return render_template('apple.html')

# Route the orange page
@app.route('/orange')
def orange():
    return render_template('orange.html')

# Route the pawpaw page
@app.route('/pawpaw')
def pawpaw():
    return render_template('pawpaw.html')

# Route the coconut page
@app.route('/coconut')
def coconut():
    return render_template('coconut.html')

# Route the cotton page
@app.route('/cotton')
def cotton():
    return render_template('cotton.html')

# Route the jute page
@app.route('/jute')
def jute():
    return render_template('jute.html')

# Route the coffee page
@app.route('/coffee')
def coffee():
    return render_template('coffee.html')


# Run the web application
if __name__ == "__main__":
    app.run(debug=True)

