# deitynamegenerator
small project using gibi (markov chains) to generate deity names for worldbuilding


usage
===

    pip install gibi

The corpus.txt file is a list of deity names sourced from wikipedia and then cleaned up by removing names with non-alphabetic characters or spaces.

The matrix.gibi file has been generated from the corpus for your convenience. If you edit the corpus, re-run ``corpus2matrix.py`` to produce the matrix file as follows:

    python corpus2matrix.py

To generate a randon deity name, run ``generatedeityname.py``.

    python generatedeityname.py

For added convenience, ``generatedeityname.py`` accepts a ``--names`` parameter, an integer specifying the number of names to generate.

    python generatedeityname.py --names 100

