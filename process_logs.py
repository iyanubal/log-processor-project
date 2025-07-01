# process_logs.py

import sys
from collections import Counter

def parse_log_file(log_file_path):
    """Reads a log file and counts occurrences of each log level."""
    log_levels = []
    try:
        # The 'with open(...) as f:' syntax is a Python best practice.
        # It ensures the file is automatically closed even if errors occur.
        with open(log_file_path, 'r') as f:
            for line in f:
                # Split the line into words. 'strip()' removes leading/trailing whitespace.
                parts = line.strip().split()
                
                # Perform a sanity check. If a line is malformed or empty, this prevents an error.
                if len(parts) >= 3:
                    # The log level is the 3rd element (index 2). 
                    # 'strip("[]")' removes the surrounding brackets to get the clean word.
                    log_level = parts[2].strip('[]')
                    log_levels.append(log_level)
    except FileNotFoundError:
        # Robust error handling is crucial for data pipelines.
        # If the input file doesn't exist, we print an informative error and exit gracefully.
        print(f"Error: The file at {log_file_path} was not found.", file=sys.stderr)
        return None
    
    # collections.Counter is a highly efficient, specialized dictionary subclass 
    # for counting hashable objects. It's perfect for this kind of aggregation task.
    return Counter(log_levels)

def print_summary(log_counts):
    """Prints a formatted summary of log counts."""
    print("\n--- Log Analysis Summary ---")
    if log_counts:
        # .items() lets us loop through the keys (log level) and values (count) of the dictionary.
        for level, count in sorted(log_counts.items()):
            print(f"{level:<10} | {count}")
    else:
        print("No log data to analyze.")
    print("--------------------------")

# This is the main entry point of the script when run from the command line.
if __name__ == "__main__":
    # Check if a command-line argument (the file path) was provided.
    # sys.argv is a list containing the script name and its arguments.
    if len(sys.argv) < 2:
        print("Usage: python process_logs.py <path_to_log_file>", file=sys.stderr)
        sys.exit(1) # Exit with a non-zero status code to indicate an error.
        
    # The file path is the first argument after the script name.
    file_path = sys.argv[1]
    
    # Call our main logic function.
    counts = parse_log_file(file_path)
    
    # Only print the summary if the parsing was successful.
    if counts is not None:
        print_summary(counts)