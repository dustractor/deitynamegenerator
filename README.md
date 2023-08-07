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

Which produces output such as the following:

    liosn'dana kass khurima aptuta phet frt dimeuso pdebrisenaete qunisus ugeramer
    nzitanyahini neasunda fos nesh iminae speu mesagae kalugainauri giti
    bamellibachaner uvinayatotysytyshe mikibiniket mius ebderisa ulu phefnzauranono
    fia mefo era dikropo statisitirethtity swisiga helieriari enga dunossheibe ana
    ithuedicli sieradu naneta turet myanngamani aliot kummoni deni nulgisoli
    alilirori himbomuopdikubu feviote bekal bese joret mandisetitongulosinei
    ponitiha deialinia nmerendr kwati cisngosemepheigli tew kobanensy fus anga
    himinzaintem tiba zilutje suma takoime poraca ereti nono nirianu san'giatti
    tewe kun eta sowy atico urtheradr omueriars aborirka mphiorithusealeicetapa
    pear ona liamb hola pana qelioseitemplaw mboiguteseti ona phia ris ask
    liriagbanumb fumaeli olanepsire bite wrel awinorwutaei heterarmitumemnishei
    baqetra phei
