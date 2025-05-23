from datetime import datetime
import json
import os

class ContestoAI:
    """
    Analizza lo stato dell'ambiente, dell'utente e del sistema.
    Suggerisce modalità comportamentali per Agape.
    """

    def __init__(self):
        self.file_stato = "contesto.json"
        self.stato_attuale = self._carica()

    def _carica(self):
        if os.path.exists(self.file_stato):
            with open(self.file_stato, "r") as f:
                return json.load(f)
        return {}

    def aggiorna(self, luogo: str, utente: str, situazione: str) -> dict:
        self.stato_attuale = {
            "data": datetime.now().isoformat(),
            "luogo": luogo,
            "utente": utente,
            "situazione": situazione,
            "suggerimento": self._suggerisci(luogo, utente, situazione)
        }
        self._salva()
        return self.stato_attuale

    def _suggerisci(self, luogo: str, utente: str, situazione: str) -> str:
        if "riunione" in situazione.lower():
            return "Modalità silenziosa e professionale"
        if "bambino" in utente.lower():
            return "Voce dolce e linguaggio semplice"
        if "notte" in luogo.lower():
            return "Risposte brevi e tono basso"
        return "Modalità standard e reattiva"

    def _salva(self):
        with open(self.file_stato, "w") as f:
            json.dump(self.stato_attuale, f, indent=2)

    def stato(self) -> dict:
        return self.stato_attuale