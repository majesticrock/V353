all: build/main.pdf

# hier Python-Skripte:
build/plot-aufladen.pdf: plot-aufladen.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot-aufladen.py

build/plot-amplitude.pdf: plot-amplitude.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot-amplitude.py

build/plot-phasenverschiebung.pdf: plot-phasenverschiebung.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot-phasenverschiebung.py

build/plot-polar.pdf: polarplot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python polarplot.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot-aufladen.pdf build/plot-amplitude.pdf build/plot-phasenverschiebung.pdf build/plot-polar.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
