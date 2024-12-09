from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os
from dotenv import load_dotenv
load_dotenv()


prediction_key = os.getenv("w10_hwprediction_key")
cv_endpoint = os.getenv("w10_hwcv_endpoint")
publish_iteration_name = 'catanddog_class'
project_id = os.getenv("w10_hwproject_id")

image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwyXeKDN29AmZgZPLS7n0Bepe8QmVappBwZCeA3XWEbWNdiDFB"

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(cv_endpoint, prediction_credentials)

results = predictor.classify_image_url(project_id,publish_iteration_name,url=image_url)

for prediction in results.predictions:
  print("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))