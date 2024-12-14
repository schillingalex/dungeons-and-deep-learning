import argparse
import os

from scrape.fantasynamegenerator import FantasyNameGeneratorScraper


def scrape_names_for_category(scraper, category, limit, output_path):
    names = scraper.get_names(category, limit=limit)
    filename = category + ".txt"
    with open(os.path.join(output_path, filename), "w") as f:
        f.write("\n".join(names))
    return names


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=str, dest="output_path", required=True,
                        help="Output directory, where the destination file (<name of category>.txt) will be placed.")
    parser.add_argument("-c", "--category", type=str, dest="category", default=None,
                        help="Category of names to get, e.g., DWARF_MALE, DWARF_FEMALE, CHANGELING. Optional, queries "
                             "all available categories by default.")
    parser.add_argument("-l", "--limit", type=int, dest="limit", default=1000,
                        help="Number of names to get (per category), default: 1000")
    args = parser.parse_args()

    scraper = FantasyNameGeneratorScraper(batches_per_call=100)
    if args.category is None:
        for c in scraper.get_available_categories():
            scrape_names_for_category(scraper, c, args.limit, args.output_path)
    else:
        scrape_names_for_category(scraper, args.category, args.limit, args.output_path)
