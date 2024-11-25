from selenium import webdriver
from selenium.webdriver.common.by import By

from src.scrape.scraper import Scraper


class FantasyNameGeneratorScraper(Scraper):
    """
    Scrapes fantasynamegenerators.com for names of different categories.
    """

    # The categories are mapped to the URL and the index of the generation button below the names
    _CATEGORY_MAPPING = {
        "DWARF_MALE": ("https://www.fantasynamegenerators.com/dnd-dwarf-names.php", 0),
        "DWARF_FEMALE": ("https://www.fantasynamegenerators.com/dnd-dwarf-names.php", 1),
        "CHANGELING": ("https://www.fantasynamegenerators.com/dnd-changeling-names.php", 0),
    }

    def get_available_categories(self) -> list[str]:
        return list(self._CATEGORY_MAPPING.keys())

    @staticmethod
    def _fetch_names(url, gen_index=0):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.implicitly_wait(5)

        # We wait until this element is loaded to know that we can call name generation.
        driver.find_element(By.ID, "result")
        # Calling this can differentiate between the options on the generator, e.g., male/female.
        driver.execute_script(f"nameGen({gen_index});")
        # The script call invalidates the element, so we want to find it again.
        elem = driver.find_element(By.ID, "result")

        names = elem.text.split("\n")

        driver.close()
        return names

    def _get_name_batch(self, category: str) -> list[str]:
        url, gen_index = self._CATEGORY_MAPPING[category]
        names = self._fetch_names(url, gen_index)
        return names
