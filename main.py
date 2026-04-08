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
        """장부(JSON) 파일에서 기존 데이터를 읽어오는 기능"""
        try: 
            with open(self.data_file, 'r', encoding='utf-8') as file:
                data = json.load(file) 
                
                self.best_score = data["best_score"]
                for q in data["quizzes"]:
                    quiz_obj = Quiz(q["question"], q["choices"], q["answer"])
                    self.quizzes.append(quiz_obj)
                    
                print(f"📂 장부를 성공적으로 불러왔습니다! (퀴즈 {len(self.quizzes)}개)")

        except FileNotFoundError:
            print("📂 장부가 없어서 새로운 K-pop 기본 장부를 생성합니다.")
            self.quizzes = [
                Quiz("걸그룹 아이브(IVE)의 데뷔곡 제목은?", ["ELEVEN", "LOVE DIVE", "After LIKE", "I AM"], 1),
                Quiz("다음 중 블랙핑크(BLACKPINK)의 멤버가 아닌 사람은?", ["지수", "제니", "로제", "윈터"], 4),
                Quiz("그룹 (여자)아이들의 히트곡 'Super Lady'가 수록된 앨범 이름은?", ["I feel", "I do", "2", "I love"], 3),
                Quiz("그룹 에스파(aespa)의 세계관에서 멤버들의 또 다른 자아를 부르는 명칭은?", ["MY", "ae", "SYNK", "P.O.S"], 2),
                Quiz("그룹 스테이씨(STAYC)의 데뷔곡은?", ["ASAP", "SO BAD", "STEREOTYPE", "Teddy Bear"], 2)
            ]
            self.save_data() 

        except json.JSONDecodeError:
            print("⚠️ 장부 파일이 손상되었습니다. 퀴즈가 0개인 상태로 시작합니다.")

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
                print("⚠️ 숫자만 입력해주세요! (예: 1, 2, 3)")
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
        choice = input("선택: ") 
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
            
            user_answer = input("정답 입력 (1~4): ")
            if user_answer == str(quiz.answer):
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

if __name__ == "__main__":
    main()