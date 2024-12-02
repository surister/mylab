def process_chunk(chunk):
    print(f"chunk: {chunk}")


def process_iterator_in_chunks(iterator, chunk_size):
    buffer = []
    last_item_len = -1
    for item in iterator:
        if (last_item_len != len(item) and last_item_len != -1) or len(buffer) == chunk_size:
            process_chunk(buffer)
            buffer = []

        buffer.append(item)

        last_item_len = len(item)

    # remaining items in the buffer
    if buffer:
        process_chunk(buffer)


data = [
    [2],
    [1, 2, 3],
    [2, 3, 4],
    [2, 3, 4],
    [1, 2],
    [1, 2],
    [1, 2],
    [1, 2],
    [1, 2],
]
chunk_size = 5
process_iterator_in_chunks(data, chunk_size)
