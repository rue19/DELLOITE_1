import json, unittest
from datetime import datetime

with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)

# Helper to convert ISO 8601 string to milliseconds
def iso_to_millis(iso_str):
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    return int((dt - datetime(1970, 1, 1)).total_seconds() * 1000)

def convertFromFormat1(jsonObject):
    return {
        "timestamp": jsonObject["timestamp"],
        "deviceId": jsonObject["deviceID"],
        "location": jsonObject["location"],
        "temperature": jsonObject["temp"],
        "status": jsonObject["operationStatus"]
    }

def convertFromFormat2(jsonObject):
    location = "/".join([
        jsonObject["country"],
        jsonObject["city"],
        jsonObject["area"],
        jsonObject["factory"],
        jsonObject["section"]
    ])
    return {
        "timestamp": iso_to_millis(jsonObject["timestamp"]),
        "deviceId": jsonObject["device"]["id"],
        "location": location,
        "temperature": jsonObject["data"]["temperature"],
        "status": jsonObject["data"]["status"]
    }

def main(jsonObject):
    if "deviceID" in jsonObject:
        return convertFromFormat1(jsonObject)
    else:
        return convertFromFormat2(jsonObject)

class TestSolution(unittest.TestCase):

    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    unittest.main()

