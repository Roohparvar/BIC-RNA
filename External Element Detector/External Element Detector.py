start_sequences = []
end_sequences = []

for i in range(1, 11):
    filename = f"D:/Github/BIC-RNA/dbnFiles/dbnFiles/ ({i}).dbn"

    with open(filename, 'r') as file:
        lines = file.readlines()

        sequence = lines[3].strip() 
        structure = lines[4].strip() 

        start_dots = 0
        while start_dots < len(structure) and structure[start_dots] == '.':
            start_dots += 1

        end_dots = 0
        while end_dots < len(structure) and structure[-(end_dots + 1)] == '.':
            end_dots += 1

        if start_dots != 0:
            start_sequences.append(sequence[:start_dots])

        if end_dots != 0:
            end_sequences.append(sequence[-end_dots:])

with open("Start_Sequences.txt", "w") as start_file:
    for start_seq in start_sequences:
        start_file.write(f"{start_seq}\n")

with open("End_Sequences.txt", "w") as end_file:
    for end_seq in end_sequences:
        end_file.write(f"{end_seq}\n")