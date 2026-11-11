# Digital Humanities Data Parsing & ETL Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![XML/TEI](https://img.shields.io/badge/Format-TEI%2FXML-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A modular Data Extraction, Transformation, and Loading (ETL) pipeline designed for computational humanities research. It parses historical TEI/XML manuscripts, archaeological corpora, and unstructured JSON metadata into structured relational SQL databases.

---

## 🎯 Academic & Technical Overview

In Computational Humanities, historical corpora are typically encoded in hierarchical XML/TEI (Text Encoding Initiative) standards. This repository implements an automated workflow to:
1. Parse hierarchical TEI nodes using `lxml` and XPath expressions.
2. Normalize legacy character encodings and clean irregular metadata strings.
3. Ingest normalized entity tables into relational SQLite schemas with full foreign key referential integrity.

---

## 📁 Repository Structure

```text
digital-humanities-data-parsing/
├── README.md               # Project documentation and architectural overview
├── requirements.txt        # Python package dependencies
├── schema.sql              # Relational database DDL schema
├── data/
│   ├── raw_tei/            # Input TEI/XML manuscript files
│   └── raw_json/           # Input unstructured metadata files
├── scripts/
│   ├── tei_parser.py       # XPath extraction for TEI headers and text bodies
│   ├── json_transformer.py # Cleaning and string normalization
│   └── db_loader.py        # SQLite database ingestion pipeline
└── database/
    └── dh_corpus.db        # Output SQLite database file
