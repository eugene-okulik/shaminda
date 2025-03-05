import os
import sys
import argparse


def find_text_in_logs(log_folder, search_text):
    for filename in os.listdir(log_folder):
        file_path = os.path.join(log_folder, filename)

        if os.path.isfile(file_path) and filename.endswith('.log'):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_number, line in enumerate(file, start=1):
                    if search_text in line:
                        words = line.split()
                        index = line.find(search_text)
                        start_index = max(index - 5 * len(words[0]), 0)
                        end_index = min(index + len(search_text) + 5 * len(words[0]), len(line))
                        context = line[start_index:end_index]
                        print(f'Файл: {filename}, Строка: {line_number}, Контекст: {context}')


def main():
    parser = argparse.ArgumentParser(description='Поиск текста в логах.')
    parser.add_argument('log_folder', type=str, help='Полный путь к папке с логами')
    parser.add_argument('--text', type=str, required=True, help='Текст для поиска')

    args = parser.parse_args()

    find_text_in_logs(args.log_folder, args.text)


if __name__ == '__main__':
    main()
