# import sys
# script, file = sys.argv

# def main(language_file, encoding):
#     line = language_file.readline()

#     if line:
#         prin_line(line, encoding)
#         return main(language_file, encoding)
    
# def prin_line(line, encoding='utf-8'):
#     next_lang = line.strip()
#     raw_bytes = next_lang.encode(encoding)
#     cooked_string = raw_bytes.decode(encoding)

#     print(raw_bytes,'<======>', cooked_string)

# languages = open("languages.txt", encoding='utf-8')

# main(languages, encoding='utf-8')



with open("ex23.py", 'r') as f:
    file = f.read()
    encoded_file = file.encode()
    print(encoded_file)