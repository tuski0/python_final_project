from models.specialized_books import Ebook, PaperBook
from utils.helpers import get_string, get_integer, get_float, get_select, pause_and_continue
import datetime as dt

def main():
    books_catalog = {}
    isbns = set()
    stats = []

    while True:
        print('='*50)
        print('1. 도서 등록')
        print('2. 전체 도서 조회')
        print('3. 도서 검색')
        print('4. 대여 / 반납 처리')
        print('5. 통계 조회')
        print('6. 프로그램 종료')
        print('='*50)

        select = get_select('1 ~ 6 사이의 숫자를 입력해주세요 : ')

        if select == 1 :
            print('1. 도서 등록')

            title = get_string('제목 : ')
            writer = get_string('저자 : ')
            isbn = get_string('isbn : ')

            if isbn in isbns :
                print('이미 존재하는 isbn')
                continue

            else :
                choice = get_integer('도서 종류를 입력해주세요 [1. 단행본], [2. 전자책] : ')
                
                if choice == 1:
                    page_count = get_integer('page count : ')
                    new_book = PaperBook(title, writer, isbn, page_count)
                    books_catalog[isbn] = new_book
                    isbns.add(isbn)
                    print(f'[단행본] {title} 도서 등록 성공')

                elif choice == 2 :
                    file_size = get_float('file size : ')
                    new_book = Ebook(title, writer, isbn, file_size)
                    books_catalog[isbn] = new_book
                    isbns.add(isbn)
                    print(f'[전자책] {title} 도서 등록 성공')
            

                else :
                    print('1, 2만 입력해주세요')

            pause_and_continue()
        elif select == 2:
            print('2. 전체 도서 조회')
            for book in books_catalog.values():
                print(book)
            pause_and_continue()
        elif select == 3:
            print('3. 도서 검색')
            
            print('=' * 50)
            print('1. 제목 검색')
            print('2. 저자 검색')
            print('3. ISBN 검색')
            print('=' * 50)
            
            choice = get_integer('1 ~ 3 중에서 입력해주세요 : ')

            if choice == 1:
                keyword = get_string('제목을 입력해주세요 : ')

                found_books = [
                    book for book in books_catalog.values() if keyword in book.get_title()
                ]

            elif choice == 2:
                keyword = get_string('저자를 입력해주세요 : ')

                found_books = [
                    book for book in books_catalog.values() if keyword in book.get_writer()
                ]

            elif choice == 3:
                keyword = get_string('ISBN을 입력해주세요 : ')

                found_books = [
                    book for book in books_catalog.values() if keyword == book.get_isbn()
                ]

            else :
                print('1 ~ 3 중에서 입력해주세요.')

            if found_books:
                for book in found_books:
                    print(book)
            else :
                print('정보가 존재하지 않습니다.')

            pause_and_continue()
        elif select == 4:
            print('도서 대여 / 반납 처리')
            key = get_string('isbn을 입력해주세요 : ')

            if key in books_catalog.keys():
                book = books_catalog[key]
                now = dt.datetime.now()
                stat = book.get_title(), book.get_isbn(), book.get_is_borrowed(), now.strftime('%Y-%m-%d %H:%M:%S')
                if not book.get_is_borrowed():
                    print(f'{book.get_title()} 대출 가능')
                    
                    decision = get_integer('대출 하시겠습니다. 1 : yes, 2: No : ')
                    if decision == 1:
                        book.set_is_borrowed(True)
                        stats.append(stat)
                        print(f'{book.get_title()} 대출 완료')
                    elif decision == 2:
                        print('대출 과정 종료')
                        continue
                    else :
                        print('1 or 2 만 입력해주세요')
                else :
                    print('반납 처리')
                    decision = get_integer('반납 하시겠습니다. 1 : yes, 2: No : ')

                    if decision == 1:
                        book.set_is_borrowed(False)
                        stats.append(stat)
                        print(f'{book.get_title()} 반납 완료')
                    elif decision == 2:
                        print('반납 과정 종료')
                        continue
                    else :
                        print('1 or 2만 입력해주세요')
            else :
                print('존재하지 않는 도서 입니다.')

            pause_and_continue()

        elif select == 5:
            print('5. 통계 조회')
            
            print('='*50)
            print('1. 전체 조회')
            print('2. 월별 조회')
            print('3. 책 제목 별 조회')
            print('='*50)

            choice = get_integer('1 ~ 3 사이의 숫자를 입력해주세요 : ')

            if choice == 1 :
                # 전체 조회 하기
                print('전체 통계 조회')
                for i, book in enumerate(stats, start=1) :
                    borrow = '대출' if not book[2] else '반납'
                    print(f'{i}. 제목 : {book[0]}, ISBN : {book[1]}, 요청 사항 : {borrow}, 처리 시간 : {book[3]}')

            elif choice == 2:
                # 월별 조회 하기
                print('월별 통계 조회')
                find = get_integer('1 ~ 12 사이의 숫자를 입력해주세요 : ')

                month = [ book for book in stats if int(book[3][5:7]) == find ]
                month_best = []
                if len(month) > 0 :
                    print(f'{find}월 기록')
                    for i, book in enumerate(month, start=1):
                        borrow = '대출' if not book[2] else '반납'
                        print(f'{i}. 제목 : {book[0]}, ISBN : {book[1]}, 요청 사항 : {borrow}, 처리 시간 : {book[3]}')
                else :
                    print('조회되는 정보가 없습니다.')
                    

            elif choice == 3:
                # 책 제목 별 조회하기
                print('제목 별 통계 조회')
                keyword = get_string('제목을 입력해주세요 : ')

                found_books = [ book for book in stats if keyword in book[0] ]

                if found_books:
                    for i, book in enumerate(found_books, start=1):
                        borrow = '대출' if not book[2] else '반납'
                        print(f'{i}. 제목 : {book[0]}, ISBN : {book[1]}, 요청 사항 : {borrow}, 처리 시간 : {book[3]}')
                else :
                    print('조회 되는 정보가 없습니다.')

            else :
                print('1 ~ 3 사이의 숫자를 입력해주세요 !!!!!')

            pause_and_continue()
            
        elif select == 6:
            print('종료 합니다.')
            break

        else :
            print('1 ~ 6 사이의 숫자를 입력해주세요')

if __name__ == '__main__' :
    main()