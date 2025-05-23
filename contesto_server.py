from flask import Flask, request, jsonify
from flask_cors import CORS
from ContestoAI import ContestoAI

app = Flask(__name__)
CORS(app)

contesto = ContestoAI()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "✅ Contesto AI attivo"})

@app.route("/aggiorna", methods=["POST"])
def aggiorna():
    data = request.get_json()
    luogo = data.get("luogo", "")
    utente = data.get("utente", "")
    situazione = data.get("situazione", "")

    if not luogo or not utente or not situazione:
        return jsonify({"success": False, "errore": "Dati mancanti."})

    stato = contesto.aggiorna(luogo, utente, situazione)
    return jsonify({"success": True, "stato": stato})

@app.route("/stato", methods=["GET"])
def stato():
    return jsonify({"success": True, "stato": contesto.stato()})

if __name__ == "__main__":
    app.run(port=3014)