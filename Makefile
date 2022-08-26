target:
	python3 program/client.py > Giacenza_media.md
	pandoc -s movimenti.csv -o movimenti.md
	pandoc -s program/G.md Giacenza_media.md movimenti.md -o Giacenza.pdf
	# pandoc -s program/G.md Giacenza_media.md -o Giacenza.pdf
	rm movimenti.md Giacenza_media.md
