print(f"buongiorno benvenuto nella tua calcolatrice prego inserisci il tuo nome: ")
nome_utente = input().strip()

print(f"Perfetto {nome_utente} procediamo")

def numero(messaggio):
    while True:
        testo = input(messaggio)
        try:
            return float(testo.replace(",", "."))
        except ValueError:
            print("non è un numero, riprova")
            

def chiedi_segno():
    while True:
     segno = input(f"scegli il tuo segno fra ('+''-''*''/'): ").strip()
     if segno in ["+", "-", "*", "/"]:
            return segno
     print("segno non valido, riprova")
     

def calcola(n1, segno, n2):
    if segno == "+":
        return n1 + n2
    elif segno == "-":
        return n1 - n2
    elif segno == "*":
        return n1 * n2
    elif segno == "/":
        if n2 == 0:
            print("Errore: divisione per zero non consentita.")
            return None
        return n1 / n2
    

n1 = numero("inserisci il primo numero: ")
segno = chiedi_segno()
n2 = numero("inserisci il secondo numero: ")

risultato = calcola(n1, segno, n2)
if risultato is not None:
    print(f"{nome_utente}, il risultato è: {round(risultato, 2)}")