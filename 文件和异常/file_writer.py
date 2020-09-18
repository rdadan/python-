filename = 'tt2.txt'
# 读取模式 （'r' ） 、 写入模式 （'w' ） 、 附加模式 （'a' ） 或让你能够读取和写入文件的模式（'r+' ）
# 默认读取模式
with open(filename, 'w') as file_obj01: # 会覆盖原先的内容
    file_obj01.write('i love python\n')
    file_obj01.write('i love java\n')

# 附件模式
with open(filename, 'a') as file_obj01: # 追加内容
    file_obj01.write('i love c\n')
    file_obj01.write('i love c++\n')