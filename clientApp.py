from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin  #Flask/Django to create REST APIs,  CORS=Coss Origine Resource Sharing, (API=Web Services)
                                                # a package to enable CORS in Flask GCPs deployment can be viewed through AWS or..
                                                ## It allows requests comming from different platforms for app
from com_in_ineuron_ai_utils.utils import decodeImage
from predict import dogcat


## Old Approch for deployment was MVC (Model,View,Contriller or BackendTeam)
# New Approch of Fask is  MVT (Model, View, Template=for UI decoration part)


# for me it was continuously showing me pakages installation notification so insttaled packeges via command prommt (but in opened inadministrator mode).
# then initially it was showing me the base env as well as system 32 as directory, the changed env to "Deployment_dogcat_new_" (which i have
# created new in pycharm) but my requirements.txt file was in C:/dowload/DeepLearning Folder so I chnged directory to that folder fired the command as,
# "pip install -r requirements.txt" then all required packages got downloaded in that env only.     (tensorflow pckg was of 68Mb so skipped it)

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)




#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = dogcat(self.filename)



@app.route("/", methods=['GET'])  # at very first, after hitting URL, By default action=Empty (/) and default method = GET
@cross_origin()
def home():
    return render_template('index.html')    # home() will return index.html page,  UPLOAD= convert image to Base64 code,
                                            # PREDICT=convert uploaded image to Jason string and predict  through model
    


@app.route("/predict", methods=['POST'])  # if this condition satisfies then control goes to below Box POST=to Predict, GET=to Upload
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictiondogcat()
    return jsonify(result)



##  Don't Uncomment below lines for Pivotal Cloud deployment
## port = int(os.getenv("PORT",5000))    # Comment it for local host deployment
# if __name__ == "__main__":
#     clApp = ClientApp()
#     app.run(debug=True, port = port)              # Change it to app.run(debug=True) to execute locally
#     #app.run(host='0.0.0.0', port=5000, debug=True)


# Final code for Pivotal Deployment
port = int(os.getenv("PORT"))

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=port)
    #app.run(debug=True)






# To push our code on CF (cloud Foundary) we need Commamd Line Interface (CF CLI App)
# Runtime.txt file to specify version of python we r going to use in app deployment
# procfile = to tell app from which file execution should start