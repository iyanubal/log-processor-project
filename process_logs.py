# process_logs.py

import sys
from collections import Counter

# Replacement for parse_log_file function
def parse_log_file(log_file_path):
    """Reads a log file, counts occurrences of each log level, and counts total lines."""
    log_levels = []
    line_count = 0
    try:
        with open(log_file_path, 'r') as f:
            for line in f:
                line_count += 1 # Increment for every line we read
                parts = line.strip().split()
                if len(parts) >= 3:
                    log_level = parts[2].strip('[]')
                    log_levels.append(log_level)
    except FileNotFoundError:
        print(f"Error: The file at {log_file_path} was not found.", file=sys.stderr)
        # Return None for both values if the file is not found
        return None, 0
    
    # Return both the Counter object and the total line count as a tuple.
    return Counter(log_levels), line_count


# Replacement for print_summary function
def print_summary(log_counts, total_lines):
    """Prints a formatted summary of log counts and total lines."""
    print("\n--- Log Analysis Summary ---")
    print(f"Total Lines Processed: {total_lines}")
    print("--- Level Counts ---")
    if log_counts:
        for level, count in sorted(log_counts.items()):
            print(f"{level:<10} | {count}")
    else:
        print("No log data to analyze.")
    print("--------------------------")

# This is the main entry point of the script when run from the command line.
# Replacement for the main execution block
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_logs.py <path_to_log_file>", file=sys.stderr)
        sys.exit(1)
        
    file_path = sys.argv[1]
    
    # Unpack the tuple returned by the function into two variables.
    counts, total_lines = parse_log_file(file_path)
    
    if counts is not None:
        # Pass both variables to the summary function.
        print_summary(counts, total_lines)