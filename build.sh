#!/bin/bash

#We're going to build all the course stuff to PDF and html files, ditch the .tex intermediates, and drop
#them into the website folder

#First the outline
#echo -e '\n\nOutline\n\n'
#ipython nbconvert outline.ipynb --to html 
#ipython nbconvert outline.ipynb --to latex --post PDF --template './templates/outline.tplx'
#rm outline.tex
#mv outline.html ./webpage/
#mv outline.pdf ./webpage/

#The pretest
#echo -e '\n\nPretest\n\n'
#ipython nbconvert pretest.ipynb --to latex --post PDF --template './templates/pretest.tplx'
#rm pretest.tex
#mv pretest.pdf ./webpage/

#The lecture notes
echo -e '\n\nLecture Notes\n\n'
ipython nbconvert week*_notes.ipynb --to html
ipython nbconvert week*_notes.ipynb --to latex --post PDF --template './templates/lecture_notes.tplx'
rm week*_notes.tex
mv week*_notes.html ./webpage/lecture_notes/
mv week*_notes.pdf ./webpage/lecture_notes/

#The homeworks
echo -e '\n\nHomework\n\n'
ipython nbconvert week*_hw.ipynb --to html
ipython nbconvert week*_hw.ipynb --to latex --post PDF --template './templates/homework.tplx'
rm week*_hw.tex
mv week*_hw.html ./webpage/homeworks/
mv week*_hw.pdf ./webpage/homeworks/

#The homework solutions
echo -e '\n\nHomework Solutions\n\n'
ipython nbconvert week*_hwsol.ipynb --to html
ipython nbconvert week*_hwsol.ipynb --to latex --post PDF --template './templates/homework.tplx'
rm week*_hwsol.tex
mv week*_hwsol.html ./webpage/homeworks/
mv week*_hwsol.pdf ./webpage/homeworks/
