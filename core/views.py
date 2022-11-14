from core import app
from flask import jsonify, request
import time

USERS = [
    {
        "id": 1,
        "name": "John"
    }
]

CATEGORIES = [
    {
        "id": 1,
        "name": "Food"
    }
]

RECORDS = [
    {
        "id": 1,
        "user_id": 1,
        "category_id": 1,
        "created": 1666544270,
        "amount": 280
    }
]


@app.route("/users")
def get_users():
    user_id = request.args.get('id', default=None, type=int)
    if user_id:
        found_user = next((user for user in USERS if user["id"] == user_id), None)
        if found_user:
            return jsonify({"user": found_user})
        else:
            return jsonify({"error": "User not found."})
    else:
        return jsonify({"users": USERS})


@app.route("/user", methods=['POST'])
def create_users():
    user_data = request.get_json()
    try:
        if user_data["name"]:
            id_dont_exist = False
            user_id = 1
            while not id_dont_exist:
                id_exist = next((user for user in USERS if user["id"] == user_id), None)
                if id_exist:
                    user_id += 1
                else:
                    id_dont_exist = True
            user = {
                "id": user_id,
                "name": user_data["name"]
            }
            USERS.append(user)
            return jsonify(user)
        else:
            return jsonify({"error": "Not all parameters set."})
    except Exception:
        return jsonify({"error": "Invalid user data."})


@app.route("/categories")
def get_categories():
    category_id = request.args.get('id', default=None, type=int)
    if category_id:
        found_category = next((category for category in CATEGORIES if category["id"] == category_id), None)
        if found_category:
            return jsonify({"category": found_category})
        else:
            return jsonify({"error": "Category not found."})
    else:
        return jsonify({"categories": CATEGORIES})


@app.route("/category", methods=['POST'])
def create_category():
    category_data = request.get_json()
    try:
        if category_data["name"]:
            id_dont_exist = False
            category_id = 1
            while not id_dont_exist:
                id_exist = next((category for category in CATEGORIES if category["id"] == category_id), None)
                if id_exist:
                    category_id += 1
                else:
                    id_dont_exist = True
            category = {
                "id": category_id,
                "name": category_data["name"]
            }
            CATEGORIES.append(category)
            return jsonify(category)
        else:
            return jsonify({"error": "Not all parameters set."})
    except Exception:
        return jsonify({"error": "Invalid category data."})


@app.route("/records")
def get_records():
    record_id = request.args.get('id', default=None, type=int)
    user_id = request.args.get('user_id', default=None, type=int)
    category_id = request.args.get('category_id', default=None, type=int)
    if record_id:
        found_record = next((record for record in RECORDS if record["id"] == record_id), None)
        if found_record:
            return jsonify({"record": found_record})
        else:
            return jsonify({"error": "Record not found."})
    else:
        if user_id:
            if category_id:
                records = list(filter(lambda record: record['user_id'] == user_id and record["category_id"] == category_id, RECORDS))
                if len(records) > 0:
                    return jsonify({"records": records})
                else:
                    return jsonify({"error": "Records from this user in this category not found."})
            else:
                records = list(filter(lambda record: record['user_id'] == user_id, RECORDS))
                if len(records) > 0:
                    return jsonify({"records": records})
                else:
                    return jsonify({"error": "Records from this user not found."})
        else:
            return jsonify({"records": RECORDS})


@app.route("/record", methods=['POST'])
def create_record():
    record_data = request.get_json()
    try:
        if record_data["user_id"] and record_data["category_id"] and record_data["amount"]:
            id_dont_exist = False
            record_id = 1
            while not id_dont_exist:
                id_exist = next((record for record in RECORDS if record["id"] == record_id), None)
                if id_exist:
                    record_id += 1
                else:
                    id_dont_exist = True
            record = {
                "id": record_id,
                "user_id": record_data["user_id"],
                "category_id": record_data["category_id"],
                "amount": record_data["amount"],
                "created": int(time.time())
            }
            RECORDS.append(record)
            return jsonify(record)
        else:
            return jsonify({"error": "Not all parameters set."})
    except Exception:
        return jsonify({"error": "Invalid record data."})


@app.route("/")
def index():
    return "Flask app"
