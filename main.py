from inference_sdk import InferenceHTTPClient
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    img_path = "/Users/lucky/X/aeroplane-prediction/imgs/airplane_520.jpg"

    # initialize the client
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key=os.getenv("API_KEY")
    )

    # infer on a local image
    result = CLIENT.infer(img_path, model_id="aeroplane-detection-gi2rt/1")

    # print(result)
    print("Total Aeroplanes detected:", len(result["predictions"]))
    # for k, v in result.items():
    #     print(k, v)


if __name__ == "__main__":
    main()
