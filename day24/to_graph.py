#!/usr/bin/env python3

import sys

def parse_circuit_file(filename):
    """
    Reads the file and returns (wire_inits, gates).

    Expects a format like:
      x00: 0
      x01: 1
      ...
      [blank line]
      x00 AND y00 -> z05
      x01 AND y01 -> z02
      ...
    """
    wire_inits = {}
    gates = []

    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    # Separate the file into two sections:
    # 1) Wire initial values (until blank line)
    # 2) Gate definitions (after the blank line)
    blank_line_index = None
    for i, line in enumerate(lines):
        if line == "":
            blank_line_index = i
            break

    # If there's no blank line, we treat it as all wire inits first, 
    # then no gates, or we might decide an error.
    if blank_line_index is None:
        # No blank line found, let's assume everything is wires or everything is gates.
        # But typically there's at least one blank line. 
        # We'll guess there's no gates if no blank line.
        wire_init_lines = lines
        gate_lines = []
    else:
        wire_init_lines = lines[:blank_line_index]
        gate_lines = lines[blank_line_index+1:]  # everything after blank line

    # Parse wire_init_lines
    # Format:  x00: 1
    for line in wire_init_lines:
        if not line:
            continue  # skip blanks
        # e.g. "x00: 1"
        if ":" not in line:
            continue  # skip malformed
        left, right = line.split(":", 1)
        wire_name = left.strip()
        value = right.strip()
        wire_inits[wire_name] = value  # '0' or '1' or possibly something else

    # Parse gate_lines
    # Format:  x00 AND y00 -> z05
    #   input1   op  input2  ->  output
    for line in gate_lines:
        if not line:
            continue
        # Example: "x00 AND y00 -> z05"
        if "->" not in line:
            continue  # skip malformed
        left, arrow_right = line.split("->")
        left = left.strip()
        out_wire = arrow_right.strip()
        # left should be like "x00 AND y00"
        parts = left.split()
        if len(parts) != 3:
            # e.g. [in1, op, in2]
            continue
        in1, op, in2 = parts
        gates.append((in1, op.upper(), in2, out_wire))
    return wire_inits, gates


def write_circuit_dot(gates, wire_inits, dot_filename="circuit.dot"):
    """
    gates: list of tuples (inputWire1, operation, inputWire2, outputWire)
    wire_inits: dict { wireName: '0' or '1' or None }, representing initial values
    dot_filename: name of the .dot file to write
    """
    with open(dot_filename, "w") as f:
        f.write("digraph Circuit {\n")
        f.write("  rankdir=LR;\n")  # Left-to-right layout (common for circuits)

        # Collect all wires by scanning the gates
        wire_names = set()
        for (in1, op, in2, outw) in gates:
            wire_names.add(in1)
            wire_names.add(in2)
            wire_names.add(outw)

        # Also include wires that appear in wire_inits but might not appear in gates
        wire_names.update(wire_inits.keys())

        # Create a node for each wire
        # Color wires differently if they start with x, y, or z
        for w in sorted(wire_names):
            if w.startswith("x"):
                color = "lightblue"
            elif w.startswith("y"):
                color = "lightgreen"
            elif w.startswith("z"):
                color = "lightcoral"
            else:
                color = "white"

            # If a wire has an initial value, mark it (doublecircle shape)
            val = wire_inits.get(w, None)
            if val in ("0", "1"):
                shape = "doublecircle"
                label = f"{w}={val}"
            else:
                shape = "circle"
                label = w

            f.write(f'  "{w}" [label="{label}", style=filled, fillcolor="{color}", shape="{shape}"];\n')

        # Create a node for each gate
        # We'll name them G0, G1, G2, etc., and label with gate operation
        for i, (in1, op, in2, outw) in enumerate(gates):
            gate_name = f"G{i}"
            f.write(f'  "{gate_name}" [label="{op}", shape=box, style="filled", fillcolor="white"];\n')

        # Add edges: wire -> gate, and gate -> output wire
        for i, (in1, op, in2, outw) in enumerate(gates):
            gate_name = f"G{i}"
            # Input wires to the gate
            f.write(f'  "{in1}" -> "{gate_name}";\n')
            f.write(f'  "{in2}" -> "{gate_name}";\n')
            # Gate output to the output wire
            f.write(f'  "{gate_name}" -> "{outw}";\n')

        f.write("}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python visualize_circuit.py <circuit_input.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    wire_inits, gates = parse_circuit_file(input_file)

    # Write out the .dot file
    dot_filename = "circuit.dot"
    write_circuit_dot(gates, wire_inits, dot_filename=dot_filename)

    print(f"DOT file '{dot_filename}' generated.")
    print("Use Graphviz to render, for example:")
    print(f"  dot -Tpng {dot_filename} -o circuit.png")

if __name__ == "__main__":
    main()

