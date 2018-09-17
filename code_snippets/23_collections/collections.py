from typing import List, Set, Dict, Tuple


def filter_countries(
    countries: Dict[int, str],             # country code to name
    locations: List[Tuple[float, float]],  # lat / long of users
    blacklist: Set[str],                   # shouldn't be available
) -> List[str]:
    pass
