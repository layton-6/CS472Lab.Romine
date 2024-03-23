# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/text-file-compression-and-decompression-using-huffman-coding/

import heapq
import struct
import sys

def buildHuffmanTree(huffman_codes):
    heap = [[weight, [char, ""]] for char, weight in huffman_codes.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        ro = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in ro[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [lo[0] + ro[0]] + lo[1:] + ro[1:])

    huffman_tree = heapq.heappop(heap)[1:]
    return huffman_tree

def decompress(input_file, output_file):
    with open(input_file, 'rb') as file:
        uncompressed_size = struct.unpack('<I', file.read(4))[0]
        _ = struct.unpack('<I', file.read(4))[0]
        huffman_codes_size = struct.unpack('<I', file.read(4))[0]

        huffman_codes = {}
        for _ in range(huffman_codes_size):
            char = struct.unpack('<I', file.read(4))[0]
            code_length = struct.unpack('<I', file.read(4))[0]
            code = struct.unpack(f'<{code_length}s', file.read(code_length))[0].decode('utf-8')
            huffman_codes[code] = chr(char)

        compressed_size = struct.unpack('<I', file.read(4))[0]

        huffman_tree = buildHuffmanTree(huffman_codes)

        current_node = huffman_tree[0]
        for i in range(compressed_size * 8):
            byte = struct.unpack('<I', file.read(4))[0]
            for _ in range(8):
                if byte & 1 << 7 - i == 0:
                    current_node = current_node[0]
                else:
                    current_node = current_node[1]

                if current_node[1] != "":
                    output_file.write(current_node[1].encode())
                    current_node = huffman_tree[0]

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: huffman_decompress.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    decompress(input_file, output_file)