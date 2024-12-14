from selenium import webdriver
from selenium.webdriver.common.by import By

from src.scrape.scraper import Scraper


class FantasyNameGeneratorScraper(Scraper):
    """
    Scrapes fantasynamegenerators.com for names of different categories.
    """

    # The categories are mapped to the URL and the index of the generation button below the names
    _CATEGORY_MAPPING = {
        "CHANGELING": ("https://www.fantasynamegenerators.com/dnd-changeling-names.php", 0),
        "DRAGONBORN_MALE": ("https://www.fantasynamegenerators.com/dnd-dragonborn-names.php", 0),
        "DRAGONBORN_FEMALE": ("https://www.fantasynamegenerators.com/dnd-dragonborn-names.php", 1),
        "DRAGONBORN_CHILD": ("https://www.fantasynamegenerators.com/dnd-dragonborn-names.php", 2),
        "DROW_MALE": ("https://www.fantasynamegenerators.com/dnd-drow-names.php", 0),
        "DROW_FEMALE": ("https://www.fantasynamegenerators.com/dnd-drow-names.php", 1),
        "DWARF_MALE": ("https://www.fantasynamegenerators.com/dnd-dwarf-names.php", 0),
        "DWARF_FEMALE": ("https://www.fantasynamegenerators.com/dnd-dwarf-names.php", 1),
        "ELF_MALE": ("https://www.fantasynamegenerators.com/dnd-elf-names.php", 0),
        "ELF_FEMALE": ("https://www.fantasynamegenerators.com/dnd-elf-names.php", 1),
        "ELF_CHILD": ("https://www.fantasynamegenerators.com/dnd-elf-names.php", 2),
        "GNOME_MALE": ("https://www.fantasynamegenerators.com/dnd-gnome-names.php", 0),
        "GNOME_FEMALE": ("https://www.fantasynamegenerators.com/dnd-gnome-names.php", 1),
        "GOBLIN_MALE": ("https://www.fantasynamegenerators.com/dnd-goblin-names.php", 0),
        "GOBLIN_FEMALE": ("https://www.fantasynamegenerators.com/dnd-goblin-names.php", 1),
        "HALFLING_MALE": ("https://www.fantasynamegenerators.com/dnd-halfling-names.php", 0),
        "HALFLING_FEMALE": ("https://www.fantasynamegenerators.com/dnd-halfling-names.php", 1),
        "HUMAN_MALE": ("https://www.fantasynamegenerators.com/dnd-human-names.php", 0),
        "HUMAN_FEMALE": ("https://www.fantasynamegenerators.com/dnd-human-names.php", 1),
        "KENKU": ("https://www.fantasynamegenerators.com/dnd-kenku-names.php", 0),
        "ORC_MALE": ("https://www.fantasynamegenerators.com/dnd-orc-names.php", 0),
        "ORC_FEMALE": ("https://www.fantasynamegenerators.com/dnd-orc-names.php", 1),
        "TIEFLING_MALE": ("https://www.fantasynamegenerators.com/dnd-tiefling-names.php", 0),
        "TIEFLING_FEMALE": ("https://www.fantasynamegenerators.com/dnd-tiefling-names.php", 1),
        "TIEFLING_VIRTUE": ("https://www.fantasynamegenerators.com/dnd-tiefling-names.php", 2),
        "WARFORGED": ("https://www.fantasynamegenerators.com/dnd-warforged-names.php", 0),
    }

    def __init__(self, batches_per_call=10):
        """
        :param batches_per_call: How many times to hit the "Get Names" button each time the site is loaded.
        """
        super(FantasyNameGeneratorScraper, self).__init__()
        self.batches_per_call = batches_per_call

    def get_available_categories(self) -> list[str]:
        return list(self._CATEGORY_MAPPING.keys())

    def _fetch_names(self, url, gen_index=0):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.implicitly_wait(10)

        # We wait until this element is loaded to know that we can call name generation.
        driver.find_element(By.ID, "result")

        names = []
        for _ in range(self.batches_per_call):
            # Calling this can differentiate between the options on the generator, e.g., male/female.
            driver.execute_script(f"nameGen({gen_index});")
            # The script call invalidates the element, so we want to find it again.
            elem = driver.find_element(By.ID, "result")
            names.extend(elem.text.split("\n"))

        driver.close()
        return names

    def _get_name_batch(self, category: str) -> list[str]:
        url, gen_index = self._CATEGORY_MAPPING[category]
        names = self._fetch_names(url, gen_index)
        return names
