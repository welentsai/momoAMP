
import json

if __name__ == "__main__":
    # JSON to Python object dict 
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(x)
    print(type(y))
    print(y['age'])
    print(y)
    
    # a Python object (dict) to JSON
    x = {"name": "John", "age": 30, "city": "New York"}
    print(type(x))
    print(json.dumps(x))
    
    x = {
      "name": "John",
      "age": 30,
      "married": True,
      "divorced": False,
      "children": ("Ann","Billy"),
      "pets": None,
      "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
      ]
    }
    
    print(type(x))
    print(len(x)) # get length of a dict
    print(json.dumps(x))
    print(x['cars']) # get item from dict
    print(x['cars'][0]) # get item from list
    print(x['cars'][0]['model']) # get item from dict
    
    