
def main():
    with open('file.txt', 'r', encoding='utf-8') as file:
        print(f'Длина файла {len(file.read())}')

    with open('file.txt', 'r', encoding='utf-8') as file:
        count_strings = file.read().split()
        print(f'Количество слов в файле - {len(count_strings)}')

    with open('file.txt', 'r', encoding='utf-8') as file:
        read_file = file.read()
        read_file = read_file.replace('.', '!')
        with open ('regerat2.txt', 'w', encoding='utf-8') as file_write:
            file_write.write(read_file)



if __name__ == "__main__":
    main()