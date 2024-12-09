from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os
from dotenv import load_dotenv
load_dotenv()

# Get path to images folder
dirname = os.path.dirname(__file__)
images_folder = os.path.join(dirname, 'images')

# Create variables for your project
publish_iteration_name = "catanddog_object"
project_id = os.getenv("w103_project_id")

# Create variables for your prediction resource
prediction_key = os.getenv("w103_prediction_key")
endpoint = os.getenv("w103_endpoint")

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint, prediction_credentials)

# Open an image and make a prediction
with open(os.path.join(images_folder, "cat (103).jpg"), "rb") as image_contents:
    results = predictor.detect_image(project_id, publish_iteration_name, image_contents)

# Display the results
for prediction in results.predictions:
    print(f"{prediction.tag_name}: {prediction.probability * 100 :.2f}%")
