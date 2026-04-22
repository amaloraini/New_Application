from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Dummy product data
PRODUCTS = [
    {
        "id": 1,
        "name": "Aura V1 Wireless Headphones",
        "price": 299.99,
        "description": "High-fidelity audio with active noise cancellation and glass-crafted earcups.",
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=600&q=80",
        "category": "Audio"
    },
    {
        "id": 2,
        "name": "Lumina Smart Watch",
        "price": 199.50,
        "description": "Minimalist design with advanced health tracking and an edge-to-edge OLED display.",
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=600&q=80",
        "category": "Wearables"
    },
    {
        "id": 3,
        "name": "Zenith Mechanical Keyboard",
        "price": 150.00,
        "description": "Premium typing experience with tactile switches and customizable RGB backlighting.",
        "image": "https://images.unsplash.com/photo-1595225476474-87563907a212?auto=format&fit=crop&w=600&q=80",
        "category": "Accessories"
    },
    {
        "id": 4,
        "name": "Nova Portable Projector",
        "price": 450.00,
        "description": "Cinematic experience on the go with 4K resolution and built-in spatial audio.",
        "image": "https://images.unsplash.com/photo-1605773527852-c546a8584ea3?auto=format&fit=crop&w=600&q=80",
        "category": "Home Cinema"
    },
    {
        "id": 5,
        "name": "Eclipse Gaming Mouse",
        "price": 89.99,
        "description": "Ultra-lightweight wireless mouse with pinpoint accuracy and ergonomic design.",
        "image": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?auto=format&fit=crop&w=600&q=80",
        "category": "Gaming"
    },
    {
        "id": 6,
        "name": "Aero Drone Pro",
        "price": 899.00,
        "description": "Professional aerial photography with a 3-axis gimbal and obstacle avoidance.",
        "image": "https://images.unsplash.com/photo-1473968512647-3e447244af8f?auto=format&fit=crop&w=600&q=80",
        "category": "Cameras"
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

@app.route('/api/products')
def get_products():
    return jsonify(PRODUCTS)

@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    # In a real app, you would save this to a database or session
    return jsonify({"message": "Product added to cart", "cart_item": data}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
