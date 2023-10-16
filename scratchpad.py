
def main():
    remove_comments_from_script("sample.py")

def remove_comments_from_script(filename: str) -> None:

    with open(filename, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if line.strip().startswith("#"):
            continue
        
        new_lines.append(line.split("#")[0])

    with open(f"new_{filename}", "w") as f:
        f.writelines(new_lines)

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