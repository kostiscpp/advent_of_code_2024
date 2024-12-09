def parse_disk_map(disk_map):
    disk = []
    file_id = 0
    is_file = True  # Start with a file
    cont = []
    idx = 0
    for digit in disk_map:
        length = int(digit)
        if is_file:
            cont.append((idx, idx+length-1))
            disk.extend([str(file_id)] * length)
            file_id += 1
        else:
            disk.extend(['.'] * length)
            cont.append((idx, idx+length-1))
        is_file = not is_file
        idx += length
    return disk, cont

def compact_disk(disk, cont):
    leng = len(cont)-1 if disk[cont[-1][0]] != '.' else len(cont)-2 
    for j in range(leng, 1, -2):
        for i in range(1, j, 2):
            if disk[cont[j][0]] != '.' and disk[cont[i][0]] == '.':
                if cont[i][1] - cont[i][0] + 1 >= cont[j][1] - cont[j][0] + 1:
                    for offset in range(cont[j][1] - cont[j][0] + 1):
                        disk[cont[i][0] + offset] = disk[cont[j][0] + offset]
                        disk[cont[j][0] + offset] = '.'
                    cont[i] = (cont[i][0] + cont[j][1] - cont[j][0] + 1, cont[i][1])
    return disk

def calculate_checksum(disk):
    checksum = 0
    for position, block in enumerate(disk):
        if block != '.':
            checksum += position * int(block)
    return checksum

def main():
    with open('9.in', 'r') as file:
        disk_map = next(file).strip('\n')
    
    # Step 1: Parse the disk map
    disk, cont = parse_disk_map(disk_map)
    print("Initial disk layout:")
    print(''.join(disk))
    
    # Step 2: Compact the disk
    disk = compact_disk(disk, cont)
    print("\nCompacted disk layout:")
    print(''.join(disk))
    
    # Step 3: Calculate the checksum
    checksum = calculate_checksum(disk)
    print(f"\nFilesystem checksum: {checksum}")

if __name__ == "__main__":
    main()

