from datetime import datetime
import json

def mappingFunction(inputData):
    mappedData = {}
    mappedData['data'] = {}
    mappedData['data']['buildingId'] = {
        'value': inputData['att']['buildingId'],
        'unit': 'None'
    }
    mappedData['data']['electricConsumption'] = {
        'value': inputData['att']['electricConsumption'],
        'unit': 'kWh'
    }
    mappedData['data']['period'] = {
        'value': inputData['att']['period'],
        'unit': 'None'
    }
    mappedData['generator_id'] = inputData.get('generatorId')
    mappedData['timestamp'] = inputData.get('timestamp')
    mappedData['topic'] = inputData.get('topic')
    print(json.dumps(mappedData, indent=4))
    return mappedData


if __name__ == '__main__':
    mappingFunction(
    {
    "timestamp": "ora", 
    "generatorId": "generatore con oggetti", 
    "topic": "topic con Array", 
    "att": {
        "buildingId": "1234", 
        "nOfFloors": "5", 
        "buildingName": "edificio 1", 
        "rooms": [
            {
                "area": "32",
                "nOfPeople": "4",
                "floor": "2",
                "roomId": "1"
            }
        ],
        "electricConsumption": "234.78",
        "period": {
            "start_ts": "11:22:33",
            "end_ts": "22:33:44"
        }
    }
}
)
    

  
"""
{
    "timestamp": "ora", 
    "generatorId": "generatore con oggetti", 
    "topic": "topic con Array", 
    "data": {
        "buildingId": "1234", 
        "nOfFloors": "5", 
        "buildingName": "edificio 1", 
        "rooms": [
            {
                "area": "32",
                "nOfPeople": "4",
                "floor": "2",
                "roomId": "1"
            }
        ],
        "electricConsumption": "234.78",
        "period": {
            "start_ts": "11:22:33",
            "end_ts": "22:33:44"
        }
    }
}
   
 {
        "timestamp": "11:22:33", 
        "generatorId": "generatore chaive:valore", 
        "topic": "solo chiave:valore", 
        "buildingId": "1234", 
        "buildingName": "edificio t", 
        "area": "200",
        "electricConsumption": "567.89"
    }
"""