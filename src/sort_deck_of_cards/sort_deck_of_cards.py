"""A."""


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank."""
    a = {}
    for c in cards:
        a.setdefault(c, []).append(c)
    cards = []
    cards.extend(a['A']) if 'A' in a else None
    for num in list(range(2, 10)):
        if str(num) in a:
            cards.extend(a[str(num)])
    cards.extend(a['T']) if 'T' in a else None
    cards.extend(a['J']) if 'J' in a else None
    cards.extend(a['Q']) if 'Q' in a else None
    cards.extend(a['K']) if 'K' in a else None
    return cards
