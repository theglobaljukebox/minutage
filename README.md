# Minutage Data


[![DOI](https://zenodo.org/badge/343250326.svg)](https://zenodo.org/badge/latestdoi/343250326)


Minutage is a dataset forming part of [The Global Jukebox](https://theglobaljukebox.org/#). 
For full details including detailed description of the datasets and how to use and interpret them, see:

Wood, A. L. C., Kirby, K. R., Ember, C. R., Silbert, S., Daikoku, H., McBride, J., Passmore, S., Paulay, F., Flory, M., Szinger, J., D’Arcangelo, G., Guarino, M., Atayeva, M., Rifkin, J., Baron, V., El Hajli, M., Szinger, M., & Savage, P. E. (2021). The Global Jukebox: A public database of performing arts and culture. PsyArXiv preprint. https://doi.org/10.31234/osf.io/4z97j


This repository is for pulling, formatting, validating and cleaning the minutage dataset.

Data is presented in three data tables within raw/

| file          | description                                              |
|---------------|----------------------------------------------------------|
| data.csv      | Codings of the phrasing and breath patterns in each song |
| phrasing.csv  | Metadata on each song file                               |
| societies.csv | Metadata on the societies from which the songs originate |
| codings.csv   | Metadata on the codings used in data.csv				   |


## How to cite the Global Jukebox

Research that uses data from the Global Jukebox should cite both the original source(s) of the data and this paper (e.g., research using data from the Cantometrics dataset: “Lomax (1968); Wood et al. (2021)”). The reference list should include the date that data were accessed and URL for the Global Jukebox (http://theglobaljukebox.org), in addition to the full reference for Lomax (1968). Additionally, Cantometrics is versioned and stored on Zenodo. Users can cite the specific dataset and version used by visiting [zenodo website].

## Versions

See the [list of releases](https://github.com/theglobaljukebox/minutage/releases) for available released versions of Minutage data.

## Acknowledgements

The Global Jukebox would not exist without the extensive recordings collected throughout the world by Alan Lomax; we would like to acknowledge his years of work by  and the enormous contributions made by other scholars in the field towards maintaining and updating the data.

## Funding 

The Global Jukebox has been developed with support from the National Endowment for the Arts, the National Endowment for the Humanities, the Concordia Foundation, the Rock Foundation, and Odyssey Productions.

## Updating

To update the data held in this repository you must have access to the central Google Drive folders held by Cultural Equity. If you do not have access to these files please contact Anna LC Wood or Stella Silbert. 

If you do have access to these files, the repository can be updated using the following steps:

1. Clone the repository to your local machine. This can be done by copying the url from the green box labelled "Code" on the top of this page and typing `git clone <url>` into the terminal
2. Within the cloned repository, type `make download` to initiate the download of files from Google Drive. This step may ask you to confirm your access credentials to the data stored on Google Drive.  The result of this step is an updated local version of the dataset.
3. If there are significant changes, we reccomend to create a new git branch. To do this type `git branch <your name for the branch>` into the terminal, replacing the text within <> with a descriptive name reflecting the changes. Then type `git checkout <your name for the branch>`. Finally, type `git commit -am 'a descriptive message of the changes'` followed by `git push`. If this is the first time you are commiting a change, git may ask you to type a different command that willbe displayed in the terminal. 
4. If changes are minor, then you need only use `git commit -am 'a descriptive message'` followed by `git push`. 
