
  

# DSC180 - Auditlab

<a  href="https://github.com/jonathanlo411/dsc180/releases"><img  src="https://img.shields.io/github/v/release/jonathanlo411/dsc180"></a><a  href="https://github.com/jonathanlo411/dsc180/blob/main/LICENSE"><img  src="https://img.shields.io/github/license/jonathanlo411/dsc180"></a>

[![Alt](https://repobeats.axiom.co/api/embed/3777d591e1e999f0e7c2f9f1d15f73cd820e72aa.svg "Repobeats analytics image for DSC180")](https://github.com/jonathanlo411/dsc180/pulse/monthly)

  

## Overview

This repository contains files related to auditing opaque ML models. There is a `util.py` file that contains general overhead setup but most of the analysis and data collection work is completed within the notebooks. It also contains a `script.py` file which will act as the main querying method.

### Key Links
- Code - [github.com/jonathanlo411/dsc180](https://github.com/jonathanlo411/dsc180)
- Final Report - [dsc180a.lojot.com/finalreport.pdf](https://dsc180a.lojot.com/finalreport.pdf)
- Website - [dsc180a.lojot.com/](https://dsc180a.lojot.com/)

### Usage

First, use the `script.py` file as a querying method. All results will be saved into a `results.csv`

Options:

-  `-d`, `--debug`: Writes to the log dir

-  `-s`, `--serialize`: Serializes the raw HTML for ad hoc analysis

  

Next, you can load the `results.csv` as demonstrated in `notebooks/analysis-template.ipynb`.

### Tech Stack

Web querying is handled by Selenium using a head based Chromium browser. There is an option to use the `requests` package in place of Selenium. Core language is in Python.

  

## Class Details

**Course Instructor**: Stuart Geiger [[contact](mailto:sgeiger@ucsd.edu)]<br>

**Course Description**: This group is for students interested in empirically investigating the outputs of real-world algorithmic systems for bias, discrimination, and other social issues --- particularly those where the code and/or training data are not publicly available. Do facial recognition classifiers work equally well on all kinds of faces? Does a job candidate's demographics impact which jobs they are recommended on a job search site? When you ask a generative image model to create images of a data scientist, what is the distribution by demographics?

We will study classic audits of non-algorithmic decision systems (e.g. equal opportunity hiring investigations in the 1970s) and contemporary audits of real-world ML/AI systems. We will learn various approaches to investigate such opaque systems, including auditing via synthetic training datasets, user reports, API scraping, fake/sockpuppet accounts, and headless browsers (where you programmatically control a web browser). We will also learn and discuss the legal and ethical issues around this kind of auditing, particularly around violating a platform's terms and conditions, which are complex. All students must take and pass the UCSD/CITI IRB Human Subject Protection Training online course (Social and Behavioral Basic) by week 3 of Fall, as well as submit their proposed Winter projects to the UCSD Institutional Review Board for legal and ethical review. For a selection of readings on this topic, see a past syllabus for a related graduate course: [https://auditlab.stuartgeiger.com](https://auditlab.stuartgeiger.com/)

> [1] https://dsc-capstone.org/enrollment/<br>

> [2] [Course Syllabus](https://docs.google.com/document/d/1Q4y7Ofg8xJ6HnVUTobOqWGffsgqovzODCnS3HzUg-oc/edit#heading=h.bdvzzd9u4w17)