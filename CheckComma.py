def check_file_abnormalities(file_path, expected_num_fields):
    expected_num_commas = expected_num_fields - 1  # Expected commas are one less than the number of fields
    line_num = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line_num += 1
            # Count commas in the line
            actual_num_commas = line.count(',')

            # Check if the count of commas is as expected
            if actual_num_commas != expected_num_commas:
                print(f'Line {line_num}: Unexpected number of commas. Found {actual_num_commas}, expected {expected_num_commas}.')

            # Check for non-LF line endings
            if not line.endswith('\n'):
                print(f'Line {line_num}: Non-LF line ending detected')

# Example usage
check_file_abnormalities('C:\\ETLProject\\AirLineData\\Suppdata\\Suppdata\\plane-data.csv', expected_num_fields=9)
