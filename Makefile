G=Giacenza.pdf
M=movimenti.csv
GM=Giacenza_media.txt

target:
	echo "# Giacenza Media\n" > Giacenza_media.md
	python3 client.py > Giacenza_media.md
	pandoc -s movimenti.csv -o movimenti.md
	pandoc -s G.md movimenti.md Giacenza_media.md -o Giacenza.pdf
