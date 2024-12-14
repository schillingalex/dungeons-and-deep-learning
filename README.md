Personal project for experimentation with machine-learning-based name generation for fantasy settings
such as Dungeons & Dragons.

# Installation

```bash
pip install -r requirements.txt
```

Tested with Python 3.11.

# Dataset Generation

To generate text files with 1000 names for each available category
by scraping fantasynamegenerators.com, use the following command:

```bash
python src/scrape_names.py -o data/ -l 1000
```
