G=Giacenza.pdf
M=movimenti.csv
GM=Giacenza_media.txt

target:
	python3 client.py > Giacenza_media.md
	pandoc -s movimenti.csv -o movimenti.md
	pandoc -s G.md Giacenza_media.md movimenti.md -o Giacenza.pdf
	# pandoc -s G.md Giacenza_media.md -o Giacenza.pdf
