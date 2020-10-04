import json
with open(r"C:\Pycharm_Project\Spider\tm\jsonfile\mobile_phone\华为手机/579484379629.json", "r", encoding="utf-8") as f:
    x = json.load(f)
    print(x)
    print(x[0]["rateContent"])