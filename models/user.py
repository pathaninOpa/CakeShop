from datetime import datetime
schema = {
    "jsonType": "object",
    "required": ["name", "email", "password"],
    "properties": {
        "name": {
            "jsonType": "string",
            "description": "must be a string and is required"
        },
        "email": {
            "jsonType": "string",
            "minimum": 0,
            "description": "must be an string and is required"
        },
        "password": {
            "jsonType": "string",
            "description": "must be a string and is required"
        }
    },
    # { "createdAt": datetime.now(datetime.UTC),
    # "updatedAt": datetime.now(datetime.UTC):}
}


# db.create_collection("mycollection_with_schema", validator={"$jsonSchema": schema})
