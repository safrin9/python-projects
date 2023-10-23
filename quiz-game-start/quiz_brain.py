class QuizBrain:
    def __init__(self,Q_list):
        self.question_number=0
        self.question_list=Q_list
        self.score=0
    def still_has_q(self):
        return self.question_number<len(self.question_list)

    def next_q(self):
        current=self.question_list[self.question_number]
        self.question_number+=1
        ans=input(f"Q.{self.question_number}:{current.text} (True or False): ")
        self.check(ans,current.answer)
    def check(self,user_a,correct_a):
        if user_a.lower()==correct_a.lower():
            print("you got it right")
            self.score+=1

        else:
            print("you got it wrong")
        print(f"correct answer is {correct_a}")
        print(f"your score: {self.score}/{self.question_number}")
        print("\n")
