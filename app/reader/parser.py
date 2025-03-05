import json

def parse(file_path):
    print(f"File_path: {file_path}")
    card_list = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print("||Opened!")
            prev_line: str = "empty"

            card_index: int = 1

            for line in file:
                stripped_line = line.strip()  # Убираем пробелы в начале и конце строки
                if stripped_line:  # Проверяем, что строка не пустая

                    if prev_line != "" and prev_line[-1] == "?" and stripped_line[-1] != "?":  # если предыдущая строка это вопрос, то читаемая это ответ, тогда посылаем как объект "вопрос - ответ"
                        question:str = prev_line
                        answer:str = stripped_line.lower().replace("ответ", "")
                        answer:str = answer.strip(" :.")

                        card = {'index': card_index, 'question': question, 'answer': answer}
                        card_list.append(card)

                        card_index = card_index + 1

                prev_line = stripped_line


    except FileNotFoundError:
        print(f"Файл по пути {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    print("File_path closed")
    print("Card_list: ", card_list)

    with open("cards_dumped.json", "w", encoding='utf-8') as write:
        json.dump(card_list, write, ensure_ascii=False, indent=4)



        #сделать джсон создаваемым





