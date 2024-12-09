from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os
import glob
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv()

# Get path to images folder
dirname = os.path.dirname(__file__)
images_folder = os.path.join(dirname, 'images')

# Create variables for your project
publish_iteration_name = "catanddog_class"
project_id = os.getenv("w102_hw_project_id")

# Create variables for your prediction resource
prediction_key = os.getenv("w102_hw_prediction_key")
endpoint = os.getenv("w102_hw_endpoint")

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint, prediction_credentials)

labels = ['cat', 'dog']

y_true = []  # 真實標籤
y_pred = []  # 預測標籤

image_files = glob.glob(os.path.join(images_folder, "*.jpg"))

print("圖片檔案清單:", image_files)


for image_file in image_files:
    with open(image_file, "rb") as image_contents:
        results = predictor.classify_image(project_id, publish_iteration_name, image_contents.read())
        
        # 根據預測結果將預測標籤與真實標籤添加到列表中
        for prediction in results.predictions:
            predicted_tag = prediction.tag_name
            y_pred.append(predicted_tag)
            
            # 透過檔名提取實際標籤
            actual_tag = image_file.split(os.sep)[-1].split(' ')[0] 
            y_true.append(actual_tag)

# print("predicted_tag",predicted_tag,'\n')
print("y_true",y_true,'\n')

# 計算混淆矩陣
cm = confusion_matrix(y_true, y_pred, labels=labels)

# 顯示混淆矩陣
print("Confusion Matrix:")
print(cm)

fig, ax = plt.subplots()
cax = ax.matshow(cm, cmap='Blues')
fig.colorbar(cax)

# 顯示標籤
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)

# 顯示數字
for (i, j), val in np.ndenumerate(cm):
    ax.text(j, i, f'{val}', ha='center', va='center', color='red')

plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()