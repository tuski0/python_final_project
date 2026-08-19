from models.base_book import Base_book

class PaperBook(Base_book):
    def __init__(self, title, writer, isbn, page_count):
        super().__init__(title, writer, isbn)
        self.__page_count = page_count

    def __str__(self):
        return f'[단행본] {super().__str__()}, 페이지 수 : {self.__page_count}p'

    # def get_info(self):
    #     return f'[단행본] {super().__str__()}, 페이지 수 : {self.__page_count}p'

class Ebook(Base_book):
    def __init__(self, title, writer, isbn, file_size):
        super().__init__(title, writer, isbn)
        self.__file_size = file_size

    def __str__(self):
        return f'[전자책] {super().__str__()}, 파일 크기 : {self.__file_size}mb'
    # def get_info(self):
    #     return f'[전자책] {super().get_info()}, 파일 크기 : {self.__file_size}mb'
