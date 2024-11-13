def parse_rna_parentheses(structure, sequence):
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
                    print(stem_sequence)
                    close_count = 0

                elif open_count > close_count:
                    stem_sequence = open_seq[-close_count:] + paired_seq[:close_count]
                    print(stem_sequence)
                    open_stack.append((f"S{open_count - close_count}", open_seq[:-close_count]))
                    close_count = 0

                elif open_count < close_count:
                    stem_sequence = open_seq + paired_seq[:open_count]
                    print(stem_sequence)
                    paired_seq = paired_seq[open_count:]
                    close_count -= open_count

        else:
            i += 1

structure = "(((.....))).....((())).....((((((((((((((((((((((((....))...))...))...)))))).(((...(((...))).((((((....))))))....)))..))))))))))))....((())).........(((((..((((((((((..)))))...))...((()))...(((.....)))..)))...)))))...((...(((...((((...(..))))))))))......"
sequence = "SDGSDGSDFGHDSTGLDFNDSOGHPTORW[HOITPORETIHTOKRGEHJGKEJIJJGIWEOFKBJFJFJFJJDJFOKUTUFUUUFERIJSFDGFGKDNJGKDFNJDOKGFDJIKREGJHFIGK]K[OOJPIWOJGPIDWERJOJJJLCNXKLCNBKLSKODJFLIOSGFIDHIJOFIDJOGFIDOGJGGDFDSJFGDKSFGHDHDNHGHSLSFD[PLAO'S;KBV,ZCNBKNBDKBBKTKFJFDJBJCBCVBGG"

parse_rna_parentheses(structure, sequence)
