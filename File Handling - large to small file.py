#Create a program to split a large file into smaller files of a specified number of lines each.
def split_file_by_lines(input_file, lines_per_chunk, output_prefix):
    try:
        with open(input_file, "r") as file:
            chunk_number = 1
            lines = []
            for line in file:
                lines.append(line)
                if len(lines) == lines_per_chunk:
                    output_file = f"{output_prefix}_{chunk_number}.txt"
                    with open(output_file, "w") as chunk_file:
                        chunk_file.writelines(lines)
                    print(f"Created {output_file}")
                    lines = []
                    chunk_number += 1
            if lines:
                output_file = f"{output_prefix}_{chunk_number}.txt"
                with open(output_file, "w") as chunk_file:
                    chunk_file.writelines(lines)
                print(f"Created {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
split_file_by_lines("file_name.txt", 1000, "chunk")
