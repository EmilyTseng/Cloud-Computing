from traceback import print_tb
from unittest import result
from flask import Flask
import random
import json
app = Flask(__name__)

@app.route('/api')
def hello_world():
    food_name= {"Easy Chicken & Asparagus Stir-Fry" : 100, 
                    "Margherita Flatbread Pizza":50,
                    "15-Minute Lo Mein": 80,
                    "Sweet & Spicy Salmon" : 50,
                    "Rosemary Shrimp Tacos": 20,
                    "Butter Beans": 40, 
                    "Basil Pasta": 88,
                    "Cauliflower Stir-Fry": 68,
                    "Quesadilla with Gouda": 54,
                    "Green Goddess Grilled Cheese": 26,
                    "Buffalo-Style Pork Chops": 48, 
                    "Zucchini Noodles": 22,
                    "Chickpeas Skillet": 81,
                    "Blackened Tilapia": 46,
                    "Spinach & Tomato Tortellini": 32,
                    "Cherry Tomato and Basil Sauce": 22
                    }

    rand_num = random.randint(0,14)

    key = ''
    value = 0
    i = 0

    for itemK, itemV in food_name.items():
        if i == rand_num:
            key = itemK
            value = str(itemV)
            break
        i = i + 1

    result = json.dumps({key: value})

    return result

if __name__ == '__main__':
    # app.run(host="localhost", port=5000, debug=True)
    app.run(host="0.0.0.0", debug=True)