#!/usr/bin/env python3

import argparse
from base64 import b64encode
from pathlib import Path
import sys

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Create a readfile from a binary application')
    parser.add_argument('binary_path', type=Path, help='Path to the binary application')
    parser.add_argument('readfile_path', type=Path, help='Output path for the readfile')
    parser.add_argument('--args', default='', help='Arguments to pass to the binary')

    args = parser.parse_args()

    # Validate binary exists
    if not args.binary_path.is_file():
        print(f"Error: Binary file '{args.binary_path}' not found", file=sys.stderr)
        sys.exit(1)

    try:
        name = args.binary_path.name
        # Read and encode binary
        encodedBin = b64encode(args.binary_path.read_bytes()).decode()

        # Create command string
        application_command = "\n".join((
            f'echo "Creating binary file {name}"',
            f'echo "{encodedBin}" | base64 -d > {name}',
            f"echo 'Binary file created'",
            f"chmod +x {name}",
            f"m5 exit", # exit to switch CPUs
            f"./{name} {args.args}",
        ))

        # Write readfile
        args.readfile_path.write_text(application_command)

    except IOError as e:
        print(f"Error: Failed to process files: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
