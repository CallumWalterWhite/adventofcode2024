from util.input import get_input_as_list

def compact_disk(disk_map):
    # Convert disk map to list of alternating file/free space lengths
    lengths = [int(x) for x in disk_map]
    
    # Track file blocks for checksum calculation
    file_blocks = []
    current_pos = 0
    
    # Parse initial disk layout
    for i in range(0, len(lengths), 2):
        file_length = lengths[i]
        free_length = lengths[i+1] if i+1 < len(lengths) else 0
        
        # Add file blocks
        file_blocks.extend([len(file_blocks)] * file_length)
        
        # Add free space blocks
        file_blocks.extend(['.'] * free_length)
    
    # Compact process: move file blocks to leftmost free space
    while '.' in file_blocks:
        # Find rightmost file block and leftmost free space
        right_file_index = len(file_blocks) - 1 - file_blocks[::-1].index(next(x for x in file_blocks[::-1] if x != '.'))
        left_space_index = file_blocks.index('.')
        
        # Move file block
        file_block = file_blocks[right_file_index]
        file_blocks[right_file_index] = '.'
        file_blocks[left_space_index] = file_block
    
    # Calculate checksum
    checksum = sum(i * block for i, block in enumerate(file_blocks) if block != '.')
    
    return checksum


if __name__ == "__main__":
    input_data =     get_input_as_list("inputs/day_9.txt")[0][0]
    print(compact_disk(input_data))
    # size = len(input_data)
    # fs = []
    # new_fs = []
    # x = 0
    # for i in range(size):
    #     if i % 2 == 0:
    #         fs.extend(int(input_data[i]) * str(x))
    #         x+=1
    #     else:
    #         fs.extend(int(input_data[i]) * ".")
    # while len(fs) > 0:
    #     ch = fs.pop()
    #     if ch != ".":
    #         found = False
    #         for i in range(len(fs)):
    #             if fs[i] == ".":
    #                 fs[i] = ch
    #                 found = True
    #                 break
    #         if not found:
    #             fs.append(ch)
    #             break
    # total = 0
    # for i in range(len(fs)):
    #     total += int(fs[i]) * i
    # print(total) 91088873473

# 009981118882777333644655556
# 0099811188827773336446555566..............


# 00...111...2...333.44.5555.6666.777.888899
# 00...111...2...333.44.5555.6666.777.888899
