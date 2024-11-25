from abc import ABC, abstractmethod


class Scraper(ABC):
    @abstractmethod
    def get_available_categories(self) -> list[str]:
        """
        Returns a list of available categories to pass to get_names. Each subclass may have different categories,
        depending on the source website.

        :return: List of available categories.
        """
        pass

    @abstractmethod
    def _get_name_batch(self, category: str) -> list[str]:
        """
        Protected method to get a single batch of names for a given category. Batch size is undefined and depends on
        the name source.

        :param category: The category to get names for.
        :return: List of names of the given category.
        """
        pass

    def get_names(self, category: str, limit: int = 100, allow_duplicates: bool = False) -> list[str]:
        """
        Method to get a list of <limit> names for a given category with optional duplicate removal.

        Available categories vary between scrapers, use `get_available_categories` to get a list.

        :param category: The category to get names for.
        :param limit: The number of names to get.
        :param allow_duplicates: Toggles duplicate removal. Optional, default: False.
        :return: List of names of the given category containing at most <limit> names.
        """
        # Validate is category is available for the current scraper
        assert category in self.get_available_categories(), f"Category '{category}' is not available"

        names = []
        while len(names) < limit:
            # Call method for subclasses to handle the details
            names.extend(self._get_name_batch(category))

            # Duplicate removal, may be slow to do for each batch when requesting too many names
            if not allow_duplicates:
                names = list(dict.fromkeys(names))
        return names[:limit]
