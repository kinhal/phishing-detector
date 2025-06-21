# Phishing Page Detector

Uno strumento Python semplice per effettuare un controllo di base sugli URL e identificare potenziali pagine di phishing. Verifica la presenza di un certificato SSL valido e analizza l’URL alla ricerca di parole sospette comunemente usate negli attacchi di phishing.

---

## Funzionalità

- Controlla se l’URL utilizza HTTPS e ha un certificato SSL valido.
- Rileva parole chiave sospette nell’URL come "login", "secure", "verify" e altre.
- Strumento leggero, semplice da usare da terminale.
- Realizzato con `requests` e `colorama` per output colorato.

---

## Requisiti

- Python 3.x
- Librerie esterne:
  - `requests`
  - `colorama`

Installa le dipendenze con:

```bash
pip install -r requirements.txt
