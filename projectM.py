#################### For Windows
# ; import multiprocessing

# ; # Функция для фильтрации данных
# ; def filter_data(data_queue, filtered_queue):
# ;     while True:
# ;         data = data_queue.get()
# ;         if data == 'STOP':
# ;             filtered_queue.put('STOP')
# ;             break
# ;         # Применение фильтра к данным
# ;         filtered_data = data.upper()  # Пример фильтрации: преобразование в верхний регистр
# ;         filtered_queue.put(filtered_data)

# ; # Функция для трансформации данных
# ; def transform_data(filtered_queue, output_queue):
# ;     while True:
# ;         data = filtered_queue.get()
# ;         if data == 'STOP':
# ;             output_queue.put('STOP')
# ;             break
# ;         # Применение трансформации к данным
# ;         transformed_data = f"Transformed {data}"  # Пример трансформации
# ;         output_queue.put(transformed_data)

# ; if __name__ == "__main__":
# ;     # Создание очередей для передачи данных между процессами
# ;     data_queue = multiprocessing.Queue()
# ;     filtered_queue = multiprocessing.Queue()
# ;     output_queue = multiprocessing.Queue()

# ;     # Запуск процессов
# ;     filter_process = multiprocessing.Process(target=filter_data, args=(data_queue, filtered_queue))
# ;     transform_process = multiprocessing.Process(target=transform_data, args=(filtered_queue, output_queue))

# ;     filter_process.start()
# ;     transform_process.start()

# ;     # Отправка данных в конвейер
# ;     for i in range(10):
# ;         data_queue.put(f"Data {i}")
# ;     data_queue.put('STOP')

# ;     # Получение и вывод обработанных данных
# ;     while True:
# ;         data = output_queue.get()
# ;         if data == 'STOP':
# ;             break
# ;         print(data)

# ;     # Ожидание завершения процессов
# ;     filter_process.join()
# ;     transform_process.join()

#####################For Linux and OS

# ; import os
# ; import subprocess

# ; # Функция для фильтрации данных
# ; def filter_data(input_data):
# ;     # Здесь может быть ваш код для фильтрации данных
# ;     return input_data

# ; # Функция для трансформации данных
# ; def transform_data(input_data):
# ;     # Здесь может быть ваш код для трансформации данных
# ;     return input_data

# ; # Создание каналов (pipes)
# ; parent_conn, child_conn = os.pipe()

# ; # Создание процесса для фильтрации данных
# ; if os.fork() == 0:
# ;     os.close(parent_conn)
# ;     with os.fdopen(child_conn, 'w') as child_pipe:
# ;         # Получение данных для фильтрации
# ;         data_to_filter = 'raw data here'
# ;         filtered_data = filter_data(data_to_filter)
# ;         child_pipe.write(filtered_data)
# ;     os._exit(0)

# ; # Создание процесса для трансформации данных
# ; if os.fork() == 0:
# ;     os.close(child_conn)
# ;     with os.fdopen(parent_conn, 'r') as parent_pipe:
# ;         data_to_transform = parent_pipe.read()
# ;         transformed_data = transform_data(data_to_transform)
# ;         # Вывод трансформированных данных
# ;         print(transformed_data)
# ;     os._exit(0)

# ; os.close(child_conn)
# ; os.close(parent_conn)
