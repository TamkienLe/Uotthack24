# Uotthack24
my name is Samuel Braun, I love programming and romantic walks on the beach.

## Steps to set up/run
### Setup python venv and install flask
1. Create python virtual environment ```python3 -m venv .venv```
2. Activate virtual environment every time you open a new terminal session: ```. .venv/bin/activate```
3. Instsall flask: ```pip install flask```

### Running:
1. Tell flask what the entrypoint is```export FLASK_APP=main.py```
2. run the app (should work after setting up venv): ```flask run```


## Flask Endpoint
```/visionText``` POST endpoint for an image file. Image needs to be named 'image'

## String manipulation algorithms
Need to manipulate strings to get important information out of clothing labels
## text_extract.py
Takes string input and produces an output that looks like this based on what could be found:
```json
{
    "location": "somewhere",
    "RN": 12345,
    "CA": 12345,
    "materials": {
        "COTTON": 80, 
        "POLYESTER": 20, 
        "NYLON": 0,
        "SILK": 0,
        "LEATHER": 0, 
        "WOOL": 0,
        "VISCOSE": 0,
        "LINEN": 0,
        "ACRYLIC FABRIC": 0
    }
}
```