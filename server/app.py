from flask import Flask, jsonify, request, send_file
from io import BytesIO
import qrcode
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def return_home():
    return jsonify({'message': 'Hello World'})

@app.route('/submit', methods=['POST'])
def create_qr():
    
    data = request.json
    if data.get('isOpen'):
        text=f"{data.get('URL')}"
    else:
        text=f"Name: {data.get('name')} \n Phone Number: {data.get('phoneNumber')}"
    if not text:
        return jsonify({'error': 'No comment provided'}), 400
    
    img = qrcode.make(text)
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

# if __name__ == '__main__':
#     app.run(debug=True, port=8080)
