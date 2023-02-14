const db = db.getSiblingDB("shop");

// Mongo init admin user
db.createUser(
    {
        user: "admin",
        pwd: "password",
        roles: [{ role: "root", db: "admin" }]
    }
)



// Create validators


const productSchema = {
    validator: {
        $jsonSchema: {
            bsonType: 'object',
            title: 'product object schema',
            required: ['amount', 'price', 'name'],
            properties: {
                amount: {
                    bsonType: 'int',
                    description: 'must be an integer and is required'
                },
                price: {
                    bsonType: 'double',
                    description: 'must be a double and is required'
                },
                name: {
                    bsonType: 'string',
                    description: 'must be a string and is required'
                },
                type: {
                    enum: ['food', 'drink', 'other'],
                    description: 'can only be one of the enum values and is required'
                }
            }
        }
    }
}

const clientSchema = {
    validator: {
        $jsonSchema: {
            bsonType: 'object',
            title: 'client object schema',
            required: ['name', 'email', 'phone'],
            properties: {
                name: {
                    bsonType: 'string',
                    description: 'must be a string and is required'
                },
                email: {
                    bsonType: 'string',
                    description: 'must be a string and is required'
                },
                phone: {
                    bsonType: 'string',
                    description: 'must be a string and is required',
                    pattern: '^[0-9]{3}-[0-9]{3}-[0-9]{4}$',
                },
            }
        }
    }
}

const orderSchema = {
    validator: {
        $jsonSchema: {
            bsonType: 'object',
            title: 'order object schema',
            required: ['client', 'products', 'total', 'date'],
            properties: {
                client: {
                    bsonType: 'objectId',
                    description: 'must be an objectId and is required'
                },
                products: {
                    bsonType: 'array',
                    description: 'must be an array and is required',
                    items: {
                        bsonType: 'objectId',
                        description: 'must be an objectId and is required'
                    }
                },
                total: {
                    bsonType: 'double',
                    description: 'must be a double and is required'
                },
                date: {
                    bsonType: 'date',
                    description: 'must be a date and is required'
                },
            }
        }
    }
}


// Create collections
db.createCollection("products", productSchema);
db.createCollection("clients", clientSchema);
db.createCollection("orders", orderSchema);