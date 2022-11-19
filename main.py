# списки
questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

# запускаем счетчик
counter = 0

# приветствие, знакомство и начало теста
print("Привет! Предлагаю проверить свои знания английского!")
print("Наберите ready, чтобы начать!")
user_start = input()
if user_start == "ready":

    # запуск основного цикла из списка questions
    for i in range(len(questions)):
        print(questions[0])
        user_answer = input()
        # сравнение и условие проверки ответа юзера с верным ответом
        correct_answer = answers[0]
        if user_answer == correct_answer:
            counter += 1
            print("Ответ верный!")
        else:
            print(f"Неправильно. Правильный ответ: {answers[0]}")

        print(questions[1])
        user_answer = input()
        correct_answer = answers[1]
        if user_answer == correct_answer:
            counter += 1
            print("Ответ верный!")
        else:
            print(f"Неправильно. Правильный ответ: {answers[1]}")

        print(questions[2])
        user_answer = input()
        correct_answer = answers[2]
        if user_answer == correct_answer:
            counter += 1
            print("Ответ верный!")
        else:
            print(f"Неправильно. Правильный ответ: {answers[2]}")
        break

else:
    print("Кажется, вы не хотите играть. Очень жаль.")

# добавлю round для округления, иначе много знаков после запятой
score_percent = round(counter / 3 * 100)

# итоги
print(f"Вот и все! Вы ответили на {len(questions)} вопросов из них {counter} верно, это {score_percent} процентов.")
