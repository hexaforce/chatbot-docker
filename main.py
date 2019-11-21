from flask import Flask, render_template, request, jsonify
import aiml
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():

    brain_file = "bot_brain.brn"
    message = str(request.form['messageText'])
    kernel = aiml.Kernel()

    if os.path.isfile(brain_file):
        kernel.bootstrap(brainFile=brain_file)
    else:
        kernel.bootstrap(learnFiles=os.path.abspath("aiml/std-startup.xml"), commands="load aiml b")
        kernel.saveBrain(brain_file)

    # kernel now ready for use
    while True:
        if message == "quit":
            exit()
        elif message == "save":
            kernel.saveBrain(brain_file)
        else:
            bot_response = kernel.respond(message)
            # print bot_response
            return jsonify({'status': 'OK', 'answer': bot_response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
