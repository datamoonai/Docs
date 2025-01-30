import json
from threading import Thread

import requests
import utility
import datetime
from utility.plate_utility import get_persian_letter

def send_custom_log_thread(params):
    custom_params = params["custom_params"]
    if custom_params["name"] == "my_custom_api":
        log, camera, camera_meta= params["log"], params["camera"], params["camera_meta"]
        dt = datetime.datetime.fromtimestamp(log.time // 1000)
        date_path = dt.strftime("%Y/%m/%d")

        plate = "_" + log.selected_plate[:2] + "_" +log.selected_plate[2:-5]+"_"+log.selected_plate[-5:]
        filename = dt.strftime("%Y-%m-%d_%H-%M-%S") + plate  # Keep only the first three digits of the microsecond

        # Step 3: Construct the full path
        full_path_p = f"listen/{date_path}/{filename}" + "-p.jpg"
        full_path_c = f"listen/{date_path}/{filename}" + "-c.jpg"

        params = custom_params["my_custom_api_params"]
        payload = {
          "User": params["username"],
          "Pass": params["password"],
          "ParkingGateId": int(camera_meta["node_id"]) if "node_id" in camera_meta else 1,
          "PelakSection4": int(log.selected_plate[:2]),
          "PelakSection2": int(log.selected_plate[-5:-2]),
          "PelakSection3": get_persian_letter(log.selected_plate[2:-5]),
          "PelakSection1": int(log.selected_plate[-2:]),
          "ClientDateM": dt.strftime("%Y-%m-%d %H:%M:%S"),
          "VehicleType": 1,
          "InOutType": 1 if camera.is_inside else 3,
          "IsInvalidDateM": True,
          "ServerURL": None,
          "PlateFileName": full_path_p,
          "PlateBase64File": utility.utilities.get_base64_from_bgr(
                            utility.utilities.resize(log.best_image, 128)),
          "TruckFileName": full_path_c,
          "TruckBase64File": utility.utilities.get_base64_from_bgr(
                            utility.utilities.resize(log.best_car_image, 512)),
          "confidence": "6.99;6.99;6.99;6.99;6.99;6.99;6.99;6.99;",
          "ocrId": log.id,
          "movementStatus": "moving away" if log.direction == 1 else "approaching",
          "ocrAccuracy": log.best_ocr_accuracy
        }

        #with open("custom_api.json", "w+") as f:
        #    f.write(json.dumps(payload))
        response = requests.post(params["url"], json = payload, verify = False)
        print("Custom api", response.status_code)

def send_custom_log(params):
    thread = Thread(target=send_custom_log_thread, args=(params,))
    thread.start()