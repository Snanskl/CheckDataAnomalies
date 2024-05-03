def check_line_breaks(file_path):
    line_num = 0

    with open(file_path, 'rb') as file:  # Open in binary mode to accurately check line endings
        for line in file:
            line_num += 1
            # Check if the line ends with a Line Feed '\n' (Unix-style)
            if not line.endswith(b'\n'):
                print(f'Line {line_num}: Incorrect line break detected')

# Example usage
check_line_breaks('C:\\ETLProject\\AirLineData\\Suppdata\\Suppdata\\plane-data.csv')
