# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/text-file-compression-and-decompression-using-huffman-coding/

import heapq
import struct
import sys
from collections import defaultdict

def buildHuffmanTree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        ro = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in ro[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [lo[0] + ro[0]] + lo[1:] + ro[1:])

    huffman_codes = dict(heapq.heappop(heap)[1:])
    return huffman_codes

def compress(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    huffman_codes = buildHuffmanTree(text)

    with open(output_file, 'wb') as file:
        file.write(struct.pack('<I', len(text)))
        file.write(struct.pack('<I', 0))
        file.write(struct.pack('<I', len(huffman_codes)))

        for char, code in huffman_codes.items():
            file.write(struct.pack('<I', ord(char)))
            file.write(struct.pack('<I', len(code)))
            file.write(struct.pack(f'<{len(code)}s', code.encode('utf-8')))

        compressed_data = ''.join([huffman_codes[char] for char in text])
        file.write(struct.pack('<I', len(compressed_data)))

        for i in range(0, len(compressed_data), 8):
            byte = compressed_data[i:i+8]
            file.write(struct.pack('<I', int(byte, 2)))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: huffman_compress.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    compress(input_file, output_file)