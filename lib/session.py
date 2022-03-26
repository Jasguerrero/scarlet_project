from typing import Dict, Tuple


DAMAGE_KEY = "Damage:"


class Session:
    def __init__(self, session_str: str):
        self.session_str = session_str
        actual_damage, damage_classification = self._get_damage_with_classification()
        self.actual_damage = actual_damage
        self.damage_classification = damage_classification

    def _get_damage_with_classification(self) -> Tuple[int, int]:
        """
        :return: First value is the actual damage and second the
        classification damage
        """
        actual_damage = self._get_actual_damage_value()
        ranges = self._get_ranges()
        damage_classification = self._get_damage_classification(actual_damage, ranges)

        return actual_damage, damage_classification

    def _get_actual_damage_value(self) -> int:
        session = self.session_str.strip()
        session = session.split('\n')

        value = 0
        for i in session:
            val = i.strip()
            if DAMAGE_KEY in val:
                label, value = val.split(' ')
                value = int(value)
                break

        return value

    @staticmethod
    def _get_damage_classification(
            value: int, ranges: Dict[int, Tuple[float, float]]) -> int:

        for key, (lower_bound, upper_bound) in ranges.items():
            if lower_bound <= value <= upper_bound:
                return key
        raise ValueError('No damage classification found')

    @staticmethod
    def _get_ranges() -> Dict[int, Tuple[float, float]]:
        classifications = [i for i in range(5000, 35000, 5000)]
        result = {}
        percentage = .1

        for class_value in classifications:
            delta = class_value * percentage
            lower_bound = class_value - delta
            upper_bound = class_value + delta

            result[class_value] = (lower_bound, upper_bound)

        return result
