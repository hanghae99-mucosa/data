# -*- coding: utf-8 -*-
from model.Category import Category

class CategoryFaker():
    def create_catogory_dataset(self):
        categroy_class_list = []

        category_list = [(None, None),
                            ("상의", None), ("바지", None), ("아우터", None), ("원피스", None), ("스커트", None), ("스니커즈", None), ("신발", None), ("가방", None),
                            ("반소매 티셔츠", 1), ("긴소매 티셔츠", 1), ("민소매 티셔츠", 1), ("셔츠/블라우스", 1), ("피케/카라 티셔츠", 1), ("맨투맨/스웨트셔츠", 1), ("후드 티셔츠", 1), ("니트/스웨터", 1), ("기타 상의", 1),
                            ("데님 팬츠", 2), ("코튼 팬츠", 2), ("슈트 팬츠/슬랙스", 2), ("트레이닝/조거 팬츠", 2), ("숏 팬츠", 2), ("레깅스", 2), ("점프 슈트/오버올", 2), ("기타 바지", 2),
                            ("후드 집업", 3), ("블루종/MA-1", 3), ("레더/라이더스 재킷", 3), ("무스탕/퍼", 3), ("트러커 재킷", 3), ("슈트/블레이저 재킷", 3), ("카디건", 3), ("아노락 재킷", 3), ("플리스/뽀글이", 3), ("트레이닝 재킷", 3), ("스타디움 재킷", 3), ("환절기 코트", 3), ("겨울 싱글 코트", 3), ("겨울 더블 코트", 3), ("겨울 기타 코트", 3), ("롱패딩/롱헤비 아우터", 3), ("숏패딩/숏헤비 아우터", 3), ("패딩 베스트", 3), ("베스트", 3), ("사파리/헌팅 재킷", 3), ("나일론/코치 재킷", 3), ("기타 아우터", 3),
                            ("미니 원피스", 4), ("미디 원피스", 4), ("맥시 원피스", 4),
                            ("미니 스커트", 5), ("미디스커트", 5), ("롱스커트", 5),
                            ("캔버스/단화", 6), ("패션스니커즈화", 6), ("기타 스니커즈", 6),
                            ("구두", 7), ("로퍼", 7), ("힐/펌프스", 7), ("플랫 슈즈", 7), ("블로퍼", 7), ("샌들", 7), ("슬리퍼", 7), ("기타 신발", 7), ("모카신/보트 슈즈", 7), ("부츠", 7), ("신발 용품", 7),
                            ("백팩", 8), ("메신저/크로스 백", 8), ("숄더백", 8), ("토트백", 8), ("에코백", 8), ("보스턴/드럼/더플백", 8), ("웨이스트 백", 8), ("파우치 백", 8), ("브리프케이스", 8), ("캐리어", 8), ("가방 소품", 8), ("지갑/머니클립", 8), ("클러치 백", 8)]


        for i, ele in enumerate(category_list):
            if i == 0 :
                continue
            category = Category(i, ele[0], ele[1])
            categroy_class_list.append(category)

        return categroy_class_list


if __name__ == "__main__":

    category_faker = CategoryFaker()
    categroy_class_list = category_faker.create_catogory_dataset()

    for category in categroy_class_list:
        print(category)
