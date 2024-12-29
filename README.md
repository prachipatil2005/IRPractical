# NLP and Machine Learning Practice

This repository contains practice scripts for Natural Language Processing (NLP) and Machine Learning tasks using Python.

## Files

- [Pract1_BitWise.py](Pract1_BitWise.py): This script demonstrates the use of `CountVectorizer` from `sklearn` to create a word count matrix from a corpus of documents. It also shows how to find indices where specific terms are present in the documents.
- [Pract2_Gram.py](Pract2_Gram.py): This script uses the Natural Language Toolkit (NLTK) to tokenize text and extract unigrams, bigrams, and trigrams.
- [Pract3_Metrics.py](Pract3_Metrics.py): This script calculates precision, recall, and F1 score using `sklearn.metrics` for a given set of ground truth and predicted relevance values.

## Requirements

- Python 3.x
- pandas
- scikit-learn
- nltk

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required packages:
    ```sh
    pip install pandas scikit-learn nltk
    ```

3. Download NLTK data:
    ```sh
    python -m nltk.downloader punkt
    ```

## Usage

### [Pract1_BitWise.py](http://_vscodecontentref_/0)

Run the script to generate a word count matrix and find indices based on specific terms:
```sh
python Pract1_BitWise.py
