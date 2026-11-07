# Predicting Hotel Booking Cancellations

A data science project (2026) on hotel booking data. It asks whether a hotel can tell, at the moment a booking is made, which reservations are likely to be canceled, and what it should do about them.

**Main result:** a Random Forest trained on arrivals from 2015–2016 and tested on arrivals from 2017 reaches ROC-AUC 0.84. At a threshold of 0.30 it catches 70% of cancellations with 71% precision. It does better than a naive baseline and a simple business rule. The full write-up is in `reports/final_report.pdf`.

## Project structure

```
hotel-booking-cancellation/
├── data/
│   ├── hotel_bookings.csv          raw data (not in the repo, download below)
│   └── hotel_bookings_clean.csv    created by notebook 02 (not in the repo)
├── notebooks/
│   ├── 01_data_understanding.ipynb  audit: size, variables, target, quality, leakage
│   ├── 02_data_preparation.ipynb    cleaning + feature creation → clean CSV
│   ├── 03_eda.ipynb                 10 question-driven charts
│   └── 04_modeling.ipynb            baseline → LR → tree → RF / GB, evaluation, interpretation
├── reports/
│   ├── final_report.pdf             the report (source: final_report.md)
│   ├── figures/                     every chart used in the report
│   └── results_*.csv, key_results.json   result tables written by notebook 04
├── src/build_report.py              final_report.md → PDF (needs Google Chrome)
└── requirements.txt
```

## Getting the data

The dataset is *Hotel Booking Demand* (Antonio, Almeida & Nunes, 2019, *Data in Brief* 22:41–49). It is identical to the Kaggle "Hotel Booking Demand" file. Download the public copy into `data/`:

```bash
curl -L -o data/hotel_bookings.csv https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2020/2020-02-11/hotels.csv
```

Expected: 119,390 rows × 32 columns. The SHA-256 of the file used is `7c2ae42a7353905ea136e5c2287f17c92c5435826598bfbb8491c6f0c7b1fc06`.

## Reproducing the analysis

```bash
python3 -m venv .venv
```

```bash
.venv/bin/pip install -r requirements.txt
```

```bash
.venv/bin/jupyter notebook notebooks/
```

Run the notebooks in order (01 → 04). Notebook 02 writes the clean CSV that 03 and 04 read. Notebook 04 takes about 3–5 minutes on a laptop. All randomness uses seed 42, and every number in the report comes from these notebooks. There was no manual editing of the data.

**Google Colab:** upload the `notebooks/` and `data/` folders and keep the same layout. Notebooks read `../data/...` and write to `../reports/...`.

To rebuild the PDF after editing `reports/final_report.md`:

```bash
.venv/bin/python src/build_report.py
```
