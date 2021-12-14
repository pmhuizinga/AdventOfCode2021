from general_functions import read_data

day = 10
data = read_data(day, test=True)

chunk_bits = ['[', ']', '{', '}', '<', '>', '(', ')']

def question_10_a(ata):

    for row in data:
        chunk_count = []
        for chunk in chunk_bits:
            chunk_count.append(row.count(chunk))
    return chunk_count

print(question_10_a(data))