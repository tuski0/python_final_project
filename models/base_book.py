
class Base_book:
    def __init__ (self, title, writer, isbn):
        self.__title = title
        self.__writer = writer 
        self.__isbn = isbn
        self.__is_borrowed = False

    def get_title(self):
        return self.__title

    def get_writer(self):
        return self.__writer
    
    def get_isbn(self):
        return self.__isbn

    def get_is_borrowed(self):
        return self.__is_borrowed

    def set_is_borrowed(self, borrow):
        if borrow :
            self.__is_borrowed = True
        else :
            self.__is_borrowed = False


    def __str__ (self):
        status = '대출 중' if self.__is_borrowed else '대출 가능'
        return f'제목 : {self.__title}, 저자 : {self.__writer}, ISBN : {self.__isbn}, 대출 여부 : {status}'
        
    # def get_info(self):
    #     status = '대출 중' if self.__is_borrowed else '대출 가능'
    #     return f'제목 : {self.__title}, 저자 : {self.__writer}, ISBN : {self.__isbn}, 대출 여부 : {status}'