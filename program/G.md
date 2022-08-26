---
title: Giacenza Media Conto BBVA
author: Francesco Ranellucci
date: \today
abstract: |
  Script creato per avere una giacenza media semi automatica (da implementare) in quanto la banca in questione sembra non fornirla.
  Per usarlo è necessario inserire l'importo equivalente all'ultimo giorno dell'anno precedente a quello su cui sarà calcolata la giacenza media e ogni singola operazione in entrata e uscita dell'anno seguente nel file "movimenti.csv" rispettando il formato (es. se serve per l'anno 2021, inserire importo relativo al 31/12/2020, reperibile da questo file dell'anno precedente, e tutti i movimenti del 2021). Per generare questo file è necessario compilare il programma con "make" nella directory comprendente i vari file e avere installati nel pc i seguenti programmi: Python3 e Pandoc.  
  Per info: [https://github.com/frr0/Giacenza_media](https://github.com/frr0/Giacenza_media)  
  Credits: [https://gist.github.com/nikiink/1003574fbed2daef673b9d0d88818fe6](https://gist.github.com/nikiink/1003574fbed2daef673b9d0d88818fe6)  
geometry: "letterpaper,top=2cm,bottom=2cm,left=2cm,right=2cm"
fontsize: 12pt
urlcolor: red
toc: false
---
\thispagestyle{empty}