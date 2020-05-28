
# менеджер контекста убирает лишние пробельные символы и обрезает строки
import datetime

class ContextDict:

    def __init__(self,initial_file,output_file):
        self.initial_file = initial_file
        self.output_file = output_file

    def cycle_by_temporary_file(self):

        self.dictant = []
        with open(self.initial_file,'r',encoding='utf8') as file:
            self.now1 = datetime.datetime.now()
            self.dictant.append(f'время начала работы программы:{self.now1}\n\n')
            p = 0 #счетчик отступов
            for temp in file:

                if temp == '\n':
                    p+=1
                else:
                    if p != 0:
                        p = 0
                        self.dictant.append('\n')
                    self.dictant.append(f'{temp.strip()}\n')

    def __enter__(self):
        self.file_for_return = open(self.output_file,'w',encoding='utf8')
        return (self)

    def write_file_for_return(self):
        for temp in self.dictant:
            self.file_for_return.write(f' {temp}')

        self.now2 = datetime.datetime.now()
        self.work_time = self.now2 - self.now1
        self.file_for_return.write(f'\n\nвремя конца работы программы :{self.now2}\n\nвремя работы программы: {self.work_time}\n')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_for_return.close()

with ContextDict('COOk','new_cook') as file:
    file.cycle_by_temporary_file()
    file.write_file_for_return()
