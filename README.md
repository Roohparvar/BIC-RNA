# BIC-RNA

**BIC-RNA** is a repository for designing RNA sequences to solve the inverse RNA folding problem. This tool takes a secondary RNA structure in dot-bracket notation as input and suggests the RNA sequence required to achieve that structure.

## Project Overview
The inverse RNA folding problem involves identifying an RNA sequence that will fold into a specified secondary structure. This repository includes code and resources to facilitate the design of RNA sequences with desired secondary structures.

### Example
This tool analyzes the given RNA structure in dot-bracket format and returns an RNA sequence that, when folded, can form the secondary structure specified by the user.

## Features
- Input RNA secondary structure in dot-bracket notation
- Output RNA sequence optimized to match the given structure

## Raw Data
The raw data used in this project is downloaded from the bpRNA-1m Version 1.0, which is a database of single-molecule RNA secondary structures annotated by bpRNA. You can access the database [here](https://bprna.cgrb.oregonstate.edu/).

## Tools
We have added **VARNA: Visualization Applet for RNA secondary structure** to facilitate the visualization of RNA secondary structures. This tool allows you to view and analyze the RNA structures created during the project. You can download VARNA [here](https://varna.lisn.upsaclay.fr/index.php?lang=en&page=downloads&css=varna).

## Database

The database for this project currently includes data on External Elements, Stems, and Pseudoknots.

External Elements are nucleotide bases located at the beginning and end of RNA sequences that do not form bonds with other bases.
Stems are self-complementary, base-paired regions.
Pseudoknots are structures formed when a single-stranded region of RNA in the loop of a hairpin base-pairs with a complementary stretch of nucleotides elsewhere in the RNA chain.
These data have been systematically extracted and organized to facilitate in-depth analysis and support the design process. Future updates to the database may include additional RNA structural features and annotations to enhance its utility.
