all: output.txt assignment7.5.pdf

assignment7.5.pdf: assignment7.5.tex
	pdflatex assignment7.5.tex

output.txt: main.py
	./main.py > output.txt

test: all
	open assignment7.5.pdf

clean:
	rm output.txt assignment7.5.pdf
