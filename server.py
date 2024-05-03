# app.py

from flask import render_template,jsonify
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/api', methods=['POST', 'GET'])
def api_response():
    from flask import jsonify
    if request.method == 'POST':
        return jsonify(**request.json)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8001)



