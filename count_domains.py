import csv

def count_individual_endings(filename):
    # Dictionary to store count of individual endings
    individual_endings_count = {}

    try:
        # Open the CSV file
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)

            # Iterate through each row in the CSV file
            for row in reader:
                if len(row) >= 2:  # Ensure there are at least two columns in the row
                    # Split the string in the second column by '.'
                    strings = row[1].split('.')
                    
                    # Extract the ending substring from each string
                    endings = [strings[len(strings)-1]]

                    # Count occurrences of each ending substring
                    for ending in endings:
                        if ending not in individual_endings_count:
                            individual_endings_count[ending] = 1
                        else:
                            individual_endings_count[ending] += 1

        # Print the results
        print("Individual endings count:")
        for ending, count in individual_endings_count.items():
            print(f"{ending}: {count}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    count_individual_endings("download.csv")
