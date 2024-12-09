import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
load_dotenv()
# Set the values of your computer vision endpoint and computer vision key
# as environment variables:
try:
    
    endpoint = os.getenv("computervision_endpoint")
    key = os.getenv("computervision_key")
except KeyError:
    print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
    print("Set them before running this sample.")
    exit()

# Create an Image Analysis client
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)


# 建立 Image Analysis 客戶端
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# 打開本地端圖片並進行分析
image_path = r"./runaway.jpg"
with open(image_path, "rb") as image_data:
    result = client.analyze(
        image_data=image_data,  # 使用 image_data 而非 image_url
        visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
        gender_neutral_caption=True  
    )

print("Image analysis results:")
# 印出圖片標題的分析結果
print(" Caption:")
if result.caption is not None:
    print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")

# 印出 OCR (文字讀取) 的分析結果
print(" Read:")
if result.read is not None:
    for block in result.read.blocks:
        for line in block.lines:
            print(f"   Line: '{line.text}', Bounding box {line.bounding_polygon}")
            for word in line.words:
                print(f"     Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}")