import json
import os

class Quiz:
    """개별 퀴즈를 하나로 묶어주는 클래스"""
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

class QuizGame:
    """게임 전체를 관리하는 매니저 클래스"""
    def __init__(self):
        self.quizzes = []    # 퀴즈들을 담아둘 리스트 (장바구니)
        self.best_score = 0  # 최고 점수

    def display_menu(self):
        """메뉴를 화면에 보여주는 기능"""
        print("\n========================================")
        print("         나만의 퀴즈 게임 ")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")
        
        choice = input("선택: ") 
        return choice 

    def play_quiz(self):
        """1번: 퀴즈 푸는 기능"""
        pass

    def add_quiz(self):
        """2번: 퀴즈 추가하는 기능"""
        pass

    def show_list(self):
        """3번: 퀴즈 목록 보여주는 기능"""
        pass

    def show_score(self):
        """4번: 최고 점수 보여주는 기능"""
        pass

def main():
    # 프로그램이 시작되면 가장 먼저 실행되는 메인 무대
    game = QuizGame()
    
    while True:
        # 1. 메뉴를 화면에 띄우고, 사용자가 입력한 번호를 choice라는 상자에 담습니다.
        choice = game.display_menu()
        
        # 2. 사용자가 선택한 번호에 따라 다른 행동을 합니다. (조건문 if/elif/else)
        if choice == '1':
            print("\n준비 중인 기능입니다! (퀴즈 풀기)")
        elif choice == '2':
            print("\n준비 중인 기능입니다! (퀴즈 추가)")
        elif choice == '3':
            print("\n준비 중인 기능입니다! (퀴즈 목록)")
        elif choice == '4':
            print("\n준비 중인 기능입니다! (점수 확인)")
        elif choice == '5':
            print("\n게임을 종료합니다. 안녕히 가세요!")
            break  # break를 만나면 while 무한 반복문(루프)을 부수고 밖으로 탈출합니다!
        else:
            print("\n⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")

if __name__ == "__main__":
    main()