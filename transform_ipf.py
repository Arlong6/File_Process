import argparse
import os

def process_file(input_file, conversion_factor):
    # split input name and subtitle
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_transformed{ext}"

    with open(input_file, "r") as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 2:
            name, power = parts[0], float(parts[1])
            vdd_line = f'{name} VDD {power:.3e}'
            processed_lines.append(vdd_line)
            current = power / conversion_factor
            processed_lines.append(f'{name} VSS {current:.3e}')

    with open(output_file, "w") as f:
        f.write("\n".join(processed_lines))

    print(f"Processed Done, file name: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Conversion of IPF file format")
    parser.add_argument("-input_file", required=True, help="input file name")
    parser.add_argument("-convert_voltage", type=float, required=True, help="Voltage conversion factor")

    args = parser.parse_args()

    process_file(args.input_file, args.convert_voltage)

