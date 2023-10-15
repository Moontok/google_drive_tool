
def main():
    print(process_cell_pair("1"))
    print(process_cell_pair("A1"))
    print(process_cell_pair("AA1"))
    print(process_cell_pair("BA100"))
    print(process_cell_pair("CA3"))

def process_cell_pair(pair: str) -> list:
    """Process a cell pair into a list of two elements

    Args:
        pair (str): A cell pair. Ex: "A1"

    Returns:
        list: A list of two elements [0, 0]
    """

    pair = pair.upper()
    row_digits = ""
    col = 0
    for letter in pair:
        if letter.isalpha():
            col *= 26
            col += ord(letter) - ord('A') + 1
        elif letter.isdigit():
            row_digits += letter
    col -= 1 if col > 0 else 0
    row = int(row_digits) - 1
    return [col, row]

if __name__ == "__main__":
    main()