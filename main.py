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

    def get_valid_number(self, prompt_msg, max_num):
        """
        사용자로부터 안전하게 숫자를 입력받는 전담 도우미 메서드입니다.
        평가 항목: 입력 오류 케이스(공백/문자/범위 밖/빈 입력) 완벽 방어
        """
        while True:
            # 1. 공백 제거 및 빈 입력 방어
            # .strip()은 사용자가 습관적으로 스페이스바를 눌러도 양끝 공백을 싹 지워줍니다.
            user_input = input(prompt_msg).strip() 
            
            if user_input == "": # 빈 입력(엔터만 친 경우)
                print("⚠️ 값을 입력해주세요!")
                continue # 다시 처음(while)으로 돌아가서 입력을 요구합니다.
                
            # 2. 문자 입력 방어
            # .isdigit()는 입력된 값이 순수하게 숫자로만 이루어져 있는지 검사합니다.
            if not user_input.isdigit():
                print("⚠️ 숫자만 입력해주세요! (예: 1, 2, 3)")
                continue
                
            # 3. 범위 밖 입력 방어
            num = int(user_input) # 문자를 진짜 정수(int)로 변환
            if num < 1 or num > max_num:
                print(f"⚠️ 1부터 {max_num} 사이의 번호를 선택해주세요.")
                continue
                
            # 모든 관문을 무사히 통과했다면 그 숫자를 반환합니다!
            return num
        

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
        # 퀴즈가 하나도 없을 때를 대비한 방어막입니다.
        if len(self.quizzes) == 0:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해주세요!")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        print("-" * 40)
        
        score = 0  # 내 점수를 기록할 상자를 0으로 시작합니다.
        
        # 장바구니에서 퀴즈를 하나씩 꺼내옵니다.
        for i, quiz in enumerate(self.quizzes):
            print(f"\n[문제 {i+1}] {quiz.question}")
            
            # 보기 4개도 화면에 하나씩 띄워줍니다.
            for j, choice in enumerate(quiz.choices):
                print(f"{j+1}. {choice}")
            
            # 사용자에게 정답을 입력받습니다.
            user_answer = input("정답 입력 (1~4): ")
            
            # 내가 입력한 답과 실제 정답이 같은지 비교합니다! (input은 문자라서 문자로 비교)
            if user_answer == str(quiz.answer):
                print("✅ 정답입니다!")
                score += 1  # 정답이면 점수를 1점 올립니다.
            else:
                print(f"❌ 틀렸습니다! (정답: {quiz.answer}번)")
        
        print("-" * 40)
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        
        # 최고 점수 갱신 기능
        if score > self.best_score:
            print("🎉 새로운 최고 점수입니다!")
            self.best_score = score

    def add_quiz(self):
        """2번: 퀴즈 추가하는 기능"""
        print("\n📌 새로운 퀴즈를 추가합니다.")
        
        # 문제 입력 받기 (빈칸 방어)
        question = input("문제를 입력하세요: ").strip()
        while question == "":
            print("⚠️ 문제는 비워둘 수 없습니다.")
            question = input("문제를 입력하세요: ").strip()

        # 보기 4개 입력 받기
        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            # 만약 보기도 빈칸을 막고 싶다면 여기에 while문을 추가할 수 있지만, 일단 진행합니다.
            choices.append(choice)

        # 정답 번호 입력 받기 (아까 만든 전용 도우미 사용!)
        # 보기가 4개니까 max_num 자리에 4를 넣어줍니다.
        answer = self.get_valid_number("정답 번호 (1~4): ", 4)

        # 붕어빵 틀(Quiz 클래스)을 이용해 새 퀴즈 객체를 하나 만듭니다.
        new_quiz = Quiz(question, choices, answer)
        
        # 매니저의 장바구니(리스트)에 새 퀴즈를 추가합니다.
        self.quizzes.append(new_quiz)
        print("✅ 퀴즈가 성공적으로 추가되었습니다!")


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
            game.play_quiz()
        elif choice == '2':
            game.add_quiz()
        elif choice == '3':
            game.show_list()
        elif choice == '4':
            game.show_score()
        elif choice == '5':
            print("\n게임을 종료합니다. 안녕히 가세요!")
            break  # break를 만나면 while 무한 반복문(루프)을 부수고 밖으로 탈출합니다!
        else:
            print("\n⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")

if __name__ == "__main__":
    main()