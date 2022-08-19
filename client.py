import csv
from datetime import datetime
from datetime import timedelta

#
# Lo script legge i movimenti dell'anno dal file movimenti.csv che deve
# avere questo formato, per esempio:
# data valuta;importo;note
# 31/12/2018;0;saldo a fine anno precedente
# 9/10/2019;50,5
# 24/10/2019;469,5
#
# La prima riga e' l'intestazione e deve essere data valuta;importo;note
# La seconda riga deve essere il saldo al 31/12 dell'anno precedente,
# se il conto e' stato aperto durante l'anno mettere 0.
# Le altre righe poi contengono i movimenti dell'anno fino al 31/12
# (anche non ordinati cronologicamente)
#
def main():
  csv_file = open('movimenti.csv', mode='r')
  csv_reader = csv.DictReader(csv_file, delimiter=';')

  # Leggo il file csv e sommo i valori con le stesse date
  # chiave: timestamp, valore: somma importi della giornata
  importi_csv = {}
  for riga in csv_reader:
    importo = riga["importo"]
    importo = float(importo.replace(",",".")) #sostituisco la virgola col punto
    dataValutaDt = datetime.strptime(riga["data valuta"], "%d/%m/%Y")
    timestampValuta = datetime.timestamp(dataValutaDt)
    importi_in_data = importi_csv.get(timestampValuta, 0)
    importi_in_data = importi_in_data + importo
    importi_csv[timestampValuta] = importi_in_data

  csv_file.close()

  # Trasformo il dizionario in un array cosi' mantengo l'ordine e creo un altro
  # dizionario clone dell'array, con chiave il timestamp
  importi_ord_per_data = []
  importi = {}
  i = 0
  anno = 0
  for ts in sorted (importi_csv):
    data = datetime.fromtimestamp(ts)
    importo = importi_csv[ts]
    dataFmt = datetime.strftime(data, "%d/%m/%Y")
    if (i == 0): #la prima data deve essere il 31 dicembre dell'anno precedente
      anno = data.year + 1
      mese = data.month
      giorno = data.day
      if (giorno != 31 and mese != 12):
        print("Errore per la data %s: la prima data in ordine deve essere il 31/12 dell'anno precedente" % dataFmt)
        return

    else: #le altre devono essere dell'anno corrente
      if (data.year != anno):
        print("Errore per la data %s: le date devono appartenere allo stesso anno a parte la prima che deve essere il 31/12 dell'anno precedente" % dataFmt)
        return

    importi_ord_per_data.append({"timestamp": ts, "data": data, "importo": importo})
    importi[ts] = {"timestamp": ts, "data": data, "importo": importo}
    i+=1

  # Ora calcolo i saldi a fine giornata e li inserisco nell'array e nel dizionario
  # print(importi_ord_per_data)
  saldo = 0
  for importo in importi_ord_per_data:
    saldo = saldo + importo["importo"]
    importo["saldo"] = saldo
    # metto il saldo anche nel dizionario
    timestamp = importo["timestamp"]
    importi[timestamp]["saldo"] = saldo

  # Il saldo giace nel giorno successivo, quindi devo considerare i saldi dal 31/12/A-1 al 30/12/A
  # Qui completo il dizionario aggiungendo tutti i giorni dell'anno, anche quelli che
  # non hanno avuto movimenti ed inserendo i saldi, includo anche il 31/12/A-1
  dataCorrente = datetime.strptime("30/12/%d" % (anno - 1), "%d/%m/%Y")
  while True:
    dataPrecedente = dataCorrente
    dataCorrente = dataCorrente + timedelta(days=1)
    
    if (dataCorrente.month == 1 and dataCorrente.day == 1 and dataCorrente.year == (anno + 1)):
      break
    else:
      ts = datetime.timestamp(dataCorrente)
      importo_giorno = importi.get(ts)
      if (importo_giorno == None):
        #saldo non presente, prendo il saldo dal giorno precedente
        tsPrecedente = datetime.timestamp(dataPrecedente)
        importi[ts] = {"timestamp": ts, "data": dataCorrente, "importo": 0, "saldo": importi[tsPrecedente]["saldo"]}
        
      #print("%d/%d/%d Saldo: %f" % (dataCorrente.day, dataCorrente.month, dataCorrente.year, importi[ts]["saldo"]))

  # Calcolo i numeri sommando tutti i saldi nel dizionario dal 31/12/A-1 al 30/12/A
  numeri = 0
  saldo_fine_anno = 0
  for ts in sorted (importi):
    data = importi[ts]["data"]
    if (data.year == anno and data.month == 12 and data.day == 31):
      saldo_fine_anno = importi[ts]["saldo"]
    else:
      numeri = numeri + importi[ts]["saldo"]
  
  # La giacenza media si calcola dividendo sempre per 365 anche se l'anno e bisestile
  giacenza_media = ("%.2f" % (numeri/365)).replace(".",",")
  saldo_fine_anno = ("%.2f" % saldo_fine_anno).replace(".",",")
  print("GIACENZA MEDIA %d: %s - SALDO AL 31/12/%d: %s" % (anno, giacenza_media, anno, saldo_fine_anno))

  # Stampo i saldi da array
  #for importo in importi_ord_per_data:
  #  print("%s;%f;%f" % (importo["dataGMA"], importo["importo"], importo["saldo"]))

  # Stampo i saldi (da dizionario)
  #for ts in sorted (importi):
  #  print("%d/%d/%f" % (importi[ts]["data"].day, importi[ts]["data"].month, importi[ts]["saldo"]))

if __name__ == '__main__': 
  main()
