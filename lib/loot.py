class Loot:
    def __init__(self, loot_raw: str):
        self.loot_raw = loot_raw
        self.item_counts = self._get_item_counts()

    def _get_item_counts(self):
        _, items = self.loot_raw.split('chest: ')
        items = items.split(',')
        item_counts = {}
        for item in items:
            item_raw = self._clean_item_data(item)
            item_count, item_name = self._get_count_label(item_raw)
            item_counts[item_name] = item_count

        return item_counts

    @staticmethod
    def _clean_item_data(item: str):
        item = item.strip().replace('.', '')
        if item.endswith('s'):
            item = ''.join(list(item)[:-1])
        return item

    @staticmethod
    def _get_count_label(item_raw: str):
        item_split = item_raw.split(' ')
        if item_split[0] in ['a', 'an']:
            item_count = 1
        else:
            item_count = int(item_split[0])

        return item_count, '_'.join(item_split[1:])
