from util.input import get_input_as_list
from collections import defaultdict

def calculate_best_sequence(initial_secrets):
    MODULO = 16777216  # 2^24
    MAX_NUMBERS = 2000
    SEQUENCE_LENGTH = 4
    results = list()
    
    for secret in initial_secrets:
        for _ in range(2000):
            secret = (secret ^ (secret * 64)) % MODULO
            secret = (secret ^ (secret // 32)) % MODULO
            secret = (secret ^ (secret * 2048)) % MODULO
        results.append(secret)

    def generate_prices(secret):
        prices = []
        for _ in range(MAX_NUMBERS + 1):
            secret = (secret ^ (secret * 64)) % MODULO
            secret = (secret ^ (secret // 32)) % MODULO
            secret = (secret ^ (secret * 2048)) % MODULO
            prices.append(secret % 10)
        return prices

    buyer_changes = []
    buyer_prices = []
    for secret in initial_secrets:
        prices = generate_prices(secret)
        changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        buyer_prices.append(prices)
        buyer_changes.append(changes)

    sequence_totals = defaultdict(int)

    for buyer_index, changes in enumerate(buyer_changes):
        prices = buyer_prices[buyer_index]
        seen_sequences = set()  

        for i in range(len(changes) - SEQUENCE_LENGTH + 1):
            sequence = tuple(changes[i:i + SEQUENCE_LENGTH])

            if sequence not in seen_sequences:
                seen_sequences.add(sequence)
                sale_price = prices[i + SEQUENCE_LENGTH]
                sequence_totals[sequence] += sale_price

    _, max_bananas = max(sequence_totals.items(), key=lambda x: x[1])
    return sum(results), max_bananas


if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_22.txt")
    initial_secrets = [int(secret[0]) for secret in input_data]
    result, max_bananas = calculate_best_sequence(initial_secrets)
    print(result)
    print(max_bananas)