import time

def read_file(filename):
    start_time = time.time()
    with open(filename, 'r') as file:
        content = file.read()
    end_time = time.time()
    print(f"READING-{filename}, Time used: {end_time - start_time} seconds")

time.sleep(0.5)
read_file("small_file.txt")
time.sleep(0.5)
read_file("large_file.txt")
