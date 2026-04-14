# K-pop Quiz Game Final Version
import json

class Quiz:
    """개별 퀴즈를 하나로 묶어주는 클래스"""
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def to_dict(self):
        """이 퀴즈를 JSON 장부에 적기 좋게 딕셔너리 모양으로 바꿔주는 기능"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

class QuizGame:
    """게임 전체를 관리하는 매니저 클래스"""
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.data_file = 'state.json'  # 장부 파일 이름
        self.load_data()  # 매니저가 태어나자마자 가장 먼저 장부부터 읽어옵니다!

    def load_data(self):
        """장부 파일 복구 및 초기화 기능"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                data = json.load(file) 
                self.best_score = data.get("best_score", 0)
                for q in data.get("quizzes", []):
                    self.quizzes.append(Quiz(q["question"], q["choices"], q["answer"]))
                    
        except FileNotFoundError:
            print("⚠️ 데이터 파일이 없습니다. 기본 K-pop 퀴즈로 시작합니다.")
            self.set_default_quizzes() # 아래에서 만든 기본 세팅 함수 호출
            
        except json.JSONDecodeError:
            print("⚠️ 데이터 파일이 손상되었습니다! 기본 퀴즈로 복구(초기화)합니다.")
            self.set_default_quizzes() # 파일이 고장 났을 때도 기본값으로 덮어씀
    
    def set_default_quizzes(self):
        """기본 퀴즈 데이터를 세팅하고 저장하는 전용 함수"""
        self.quizzes = [
            Quiz("걸그룹 아이브(IVE)의 데뷔곡 제목은?", ["ELEVEN", "LOVE DIVE", "After LIKE", "I AM"], 1),
            Quiz("다음 중 블랙핑크(BLACKPINK)의 멤버가 아닌 사람은?", ["지수", "제니", "로제", "윈터"], 4),
            Quiz("그룹 (여자)아이들의 히트곡 'Super Lady'가 수록된 앨범 이름은?", ["I feel", "I do", "2", "I love"], 3),
            Quiz("그룹 에스파(aespa)의 세계관에서 멤버들의 또 다른 자아를 부르는 명칭은?", ["MY", "ae", "SYNK", "P.O.S"], 2),
            Quiz("그룹 스테이씨(STAYC)의 데뷔곡은?", ["ASAP", "SO BAD", "STEREOTYPE", "Teddy Bear"], 2)
        ]
        self.save_data() # 세팅 후 즉시 저장하여 파일 복구 완료
    
    def save_data(self):
        """현재 장바구니와 점수를 장부(JSON) 파일에 덮어쓰는 기능"""
        data_to_save = {
            "best_score": self.best_score,
            "quizzes": [quiz.to_dict() for quiz in self.quizzes] 
        }
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(data_to_save, file, ensure_ascii=False, indent=4)

    def get_valid_number(self, prompt_msg, max_num):
        """사용자로부터 안전하게 숫자를 입력받는 전담 도우미 메서드"""
        while True:
            user_input = input(prompt_msg).strip() 
            if user_input == "": 
                print("⚠️ 값을 입력해주세요!")
                continue 
            if not user_input.isdigit():
                print("⚠️ 숫자만 입력해주세요!")
                continue
            num = int(user_input) 
            if num < 1 or num > max_num:
                print(f"⚠️ 1부터 {max_num} 사이의 번호를 선택해주세요.")
                continue
            return num

    def display_menu(self):
        print("\n========================================")
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")
        choice = input("선택: ").strip() 
        return choice

    def play_quiz(self):
        """1번: 퀴즈 푸는 기능"""
        if len(self.quizzes) == 0:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해주세요!")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        print("-" * 40)
        
        score = 0  
        for i, quiz in enumerate(self.quizzes):
            print(f"\n[문제 {i+1}] {quiz.question}")
            for j, choice in enumerate(quiz.choices):
                print(f"{j+1}. {choice}")
            
            user_answer = self.get_valid_number("정답 입력 (1~4): ", 4)
            if int(user_answer) == quiz.answer:
                print("✅ 정답입니다!")
                score += 1  
            else:
                print(f"❌ 틀렸습니다! (정답: {quiz.answer}번)")
        
        print("-" * 40)
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        
        if score > self.best_score:
            print("🎉 새로운 최고 점수입니다!")
            self.best_score = score
            # 👉 [여기가 Step 4 핵심] 최고 점수를 갱신했으니 장부에 바로 적어라!
            self.save_data() 

    def add_quiz(self):
        """2번: 퀴즈 추가하는 기능"""
        print("\n📌 새로운 퀴즈를 추가합니다.")
        
        question = input("문제를 입력하세요: ").strip()
        while question == "":
            print("⚠️ 문제는 비워둘 수 없습니다.")
            question = input("문제를 입력하세요: ").strip()

        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            choices.append(choice)

        answer = self.get_valid_number("정답 번호 (1~4): ", 4)
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        
        print("✅ 퀴즈가 성공적으로 추가되었습니다!")
        # 👉 [여기가 Step 4 핵심] 퀴즈를 새로 하나 추가했으니 장부에 바로 적어라!
        self.save_data() 

    def show_list(self):
        """3번: 퀴즈 목록 보여주는 기능"""
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        if len(self.quizzes) == 0:
            print("아직 등록된 퀴즈가 없습니다.")
        else:
            for i, quiz in enumerate(self.quizzes):
                print(f"[{i+1}] {quiz.question}")
        print("-" * 40)

    def show_score(self):
        """4번: 최고 점수 확인 기능 (보너스 완성!)"""
        print(f"\n🏆 현재 최고 점수는 {self.best_score}점 입니다!")


def main():
    game = QuizGame()
    
    # 튼튼한 에어백(try)으로 게임 전체를 감싸줍니다!
    try:
        while True:
            choice = game.display_menu()
            
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
                break
            else:
                print("\n⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")
                
    # 사용자가 키보드로 Ctrl + C 를 눌러서 강제 종료를 시도할 때!
    except KeyboardInterrupt:
        print("\n\n🚨 강제 종료(Ctrl+C)가 감지되었습니다!")
        print("안전하게 데이터를 장부에 저장하고 게임을 끕니다. 삐빅-")
        game.save_data() # 죽기 직전에 장부에 기록!
        
    # (Mac 등에서 Ctrl + D 를 눌렀을 때를 대비한 추가 방어)
    except EOFError:
        print("\n\n🚨 입력 스트림이 끊겼습니다(EOF).")
        print("안전하게 데이터를 장부에 저장하고 게임을 끕니다. 삐빅-")
        game.save_data()

if __name__ == "__main__":
    main()
