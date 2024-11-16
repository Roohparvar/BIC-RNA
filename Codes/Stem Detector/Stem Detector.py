def parse_rna_parentheses(structure, sequence, output_file):
    open_stack = []

    i = 0
    while i < len(structure):
        if structure[i] == '(':
            open_count = 1
            while i + open_count < len(structure) and structure[i + open_count] == '(':
                open_count += 1
            paired_seq = sequence[i:i + open_count]
            open_stack.append((f"S{open_count}", paired_seq))
            i += open_count

        elif structure[i] == ')':
            close_count = 1
            while i + close_count < len(structure) and structure[i + close_count] == ')':
                close_count += 1
            paired_seq = sequence[i:i + close_count]
            i += close_count

            while close_count > 0 and open_stack:
                open_element = open_stack.pop()
                open_count = int(open_element[0][1:])
                open_seq = open_element[1]

                if open_count == close_count:
                    stem_sequence = open_seq + paired_seq[:close_count]
                    output_file.write(f"{stem_sequence}\n")
                    close_count = 0

                elif open_count > close_count:
                    stem_sequence = open_seq[-close_count:] + paired_seq[:close_count]
                    output_file.write(f"{stem_sequence}\n")
                    open_stack.append((f"S{open_count - close_count}", open_seq[:-close_count]))
                    close_count = 0

                elif open_count < close_count:
                    stem_sequence = open_seq + paired_seq[:open_count]
                    output_file.write(f"{stem_sequence}\n")
                    paired_seq = paired_seq[open_count:]
                    close_count -= open_count

        else:
            i += 1


output_filename = "Stem_Sequences.txt"

with open(output_filename, "w") as output_file:
    for i in range(1, 102319):
        print(f"Processing file {i}...")
        filename = f"D:/Github/BIC-RNA/dbnFiles/dbnFiles/ ({i}).dbn"

        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

                sequence = lines[3].strip().upper()
                structure = lines[4].strip().replace('[', '.').replace(']', '.')

                parse_rna_parentheses(structure, sequence, output_file)

        except FileNotFoundError:
            print(f"File {filename} not found. Skipping...")
        except IndexError:
            print(f"File {filename} has an invalid format. Skipping...")
