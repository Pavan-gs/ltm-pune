import azure.functions as func
import json

app = func.FunctionApp()

@app.route(route="get_order_status")
def get_order_status(req: func.HttpRequest):

    order_id = req.params.get("order_id")

    orders = {
        
        "1001": "Delivered",
        "1002": "Shipped",
        "1003": "Processing"
    }

    result = orders.get(order_id, "Order not found")

    return func.HttpResponse(
        json.dumps({
            "order_id": order_id,
            "status": result
        }),
        mimetype="application/json"
    )

# order_id=1001
# https://myfunctions.azurewebsites.net/api/get_order_status?order_id=1001

#Order Tracking
import azure.functions as func
import json

app = func.FunctionApp()

@app.route(route="get_order_status")
def get_order_status(req: func.HttpRequest):

    order_id = req.params.get("order_id")

    orders = {
        "1001": {
            "status": "Delivered",
            "delivery_date": "2026-06-10"
        },
        "1002": {
            "status": "Shipped",
            "expected_delivery": "2026-06-14"
        }
    }

    result = orders.get(order_id, {"status": "Order not found"})

    return func.HttpResponse(
        json.dumps(result),
        mimetype="application/json"
    )

# Product Search
import azure.functions as func
import json

app = func.FunctionApp()

@app.route(route="search_products")
def search_products(req: func.HttpRequest):

    category = req.params.get("category")

    products = {
        "laptop": [
            {
                "name": "HP Victus",
                "price": 65000
            },
            {
                "name": "Lenovo LOQ",
                "price": 72000
            }
        ],
        "mobile": [
            {
                "name": "Samsung S24",
                "price": 75000
            }
        ]
    }

    result = products.get(category, [])

    return func.HttpResponse(
        json.dumps(result),
        mimetype="application/json"
    )

# Create Support Ticket

import azure.functions as func
import json
import random

app = func.FunctionApp()

@app.route(route="create_ticket")
def create_ticket(req: func.HttpRequest):

    issue = req.params.get("issue")

    ticket_id = f"INC{random.randint(1000,9999)}"

    return func.HttpResponse(
        json.dumps({
            "ticket_id": ticket_id,
            "issue": issue,
            "status": "Created"
        }),
        mimetype="application/json"
    )