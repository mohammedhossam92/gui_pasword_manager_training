try:
    text_file = open("text_file_test.txt", "r")
    text_file.read()
except FileNotFoundError:
    text_file = open("file_to_created_if_error.txt", "w+")
    text_file.write("this is from except code block")
    text_file.seek(0)
    content = text_file.read()
    print(content)
finally:
    text_file.close()