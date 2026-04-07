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
        self.quizzes = [
            Quiz("걸그룹 아이브(IVE)의 데뷔곡 제목은?", ["ELEVEN", "LOVE DIVE", "After LIKE", "I AM"], 1),
            Quiz("다음 중 블랙핑크(BLACKPINK)의 멤버가 아닌 사람은?", ["지수", "제니", "로제", "윈터"], 4),
            Quiz("그룹 (여자)아이들의 히트곡 'Super Lady'가 수록된 앨범 이름은?", ["I feel", "I do", "2", "I love"], 3),
            Quiz("그룹 에스파(aespa)의 세계관에서 멤버들의 또 다른 자아를 부르는 명칭은?", ["MY", "ae", "SYNK", "P.O.S"], 2),
            Quiz("그룹 스테이씨(STAYC)의 데뷔곡은?", ["ASAP", "SO BAD", "STEREOTYPE", "Teddy Bear"], 2)
        ]
        self.best_score = 0
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
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        
        # 퀴즈가 하나도 없을 때
        if len(self.quizzes) == 0:
            print("아직 등록된 퀴즈가 없습니다.")
        # 퀴즈가 있을 때 (for 반복문을 써서 하나씩 꺼내옵니다)
        else:
            for i, quiz in enumerate(self.quizzes):
                print(f"[{i+1}] {quiz.question}")
                
        print("-" * 40)

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
            game.show_list()
        elif choice == '4':
            print("\n준비 중인 기능입니다! (점수 확인)")
        elif choice == '5':
            print("\n게임을 종료합니다. 안녕히 가세요!")
            break  # break를 만나면 while 무한 반복문(루프)을 부수고 밖으로 탈출합니다!
        else:
            print("\n⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")

if __name__ == "__main__":
    main()