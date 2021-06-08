# NLP_PlotCollocations
Calculate and plot the frequencies of 2-word and 3-word combinations in text.

PlotCollocations.ipynb
Main script that performs the following:
(i) reads in pdfs
(ii) cleans the text:
      lemmatization
      removing stop-words
      removing user-defined stop-words (useless_words.docx)
      removing non-English words unless the user previously specified them to be important (informative_words.docx)
(iii) calculates and plots the n most frequent words and word-combinations

read_pdf.py
Function to read in pdfs. Normal and scanned pdfs are both supported.

clean_text.pdf
Funtion that performs the lemmatization and text_cleaning

useless_words.docx
Corpus-specific stop-words defined by the user (in the current case: legal stop-words)

informative_words.docx
All non-English words are removed, unless they are on this list

Plots
Results folder containing the output of PlotCollocations.ipynb.
