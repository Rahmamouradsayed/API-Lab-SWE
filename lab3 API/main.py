from flask import Flask, request, jsonify
app = Flask(__name__)

items=[]
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items),200

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id']==item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({'message': 'Item not Found'}), 404

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    item = {'id': len(items)+1, 'name': data['name']}
    items.append(item)
    return jsonify(item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        item['name'] = data['name']
        return jsonify(item), 200
    return jsonify({'message':'Item Not Found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

if __name__=='__main__':
    app.run(debug=True)


