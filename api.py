from flask import Flask, request, jsonify
import testing
obj = testing.Testing()

app = Flask(__name__)

@app.route('/<query>', methods=["POST","GET"])
def getMSG(query):
    query = str(query)
    #username = request.args.get('username')
    reply= obj.response(query)
    return jsonify({'query':query,
                    'reply':reply})

if __name__ == "__main__":
    app.run(debug=True,port=5000)