def combine_text():
    
        with open('1.txt', 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open('2.txt', 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open('3.txt', 'r', encoding='utf-8') as f3:
            file3 = f3.readlines()
        with open('out.txt', 'w', encoding='utf-8') as result:

            if len(file1) < len(file2) and len(file1) < len(file3):
                result.write('1.txt' + '\n')
                result.write(str(len(file1)) + '\n')
                result.writelines(file1)
                result.write('\n')
            elif len(file2) < len(file1) and len(file2) < len(file3):
                result.write('2.txt' + '\n')
                result.write(str(len(file2)) + '\n')
                result.writelines(file2)
            elif len(file3) < len(file1) and len(file3) < len(file2):
                result.write('3.txt' + '\n')
                result.write(str(len(file3)) + '\n')
                result.writelines(file3)
                result.write('\n')
            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                    file3):
                result.write('1.txt' + '\n')
                result.write(str(len(file1)) + '\n')
                result.writelines(file1)
                result.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
                    file3):
                result.write('2.txt' + '\n')
                result.write(str(len(file2)) + '\n')
                result.writelines(file2)
                result.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
                    file2):
                result.write('3.txt' + '\n')
                result.write(str(len(file3)) + '\n')
                result.writelines(file3)
                result.write('\n')
            if len(file1) > len(file2) and len(file1) > len(file3):
                result.write('1.txt' + '\n')
                result.write(str(len(file1)) + '\n')
                result.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                result.write('2.txt' + '\n')
                result.write(str(len(file2)) + '\n')
                result.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                result.write('3.txt' + '\n')
                result.write(str(len(file3)) + '\n')
                result.writelines(file3)

if __name__ == '__main__':
    combine_text()
    with open('out.txt', 'r', encoding='utf-8') as out:
            data = out.read()
            print(data)
                

