class Question:

  def __init__(self, 
      nr: int, 
      question: str, 
      answer1: str, 
      answer2: str, 
      answer3: str, 
      answer4: str, 
      img_src: str,
      correct_answer: str
    ):
    self.nr = nr
    self.question = question
    self.answer1 = answer1
    self.answer2 = answer2
    self.answer3 = answer3
    self.answer4 = answer4
    self.img_src = img_src
    self.correct_answer = correct_answer

  def __str__(self):
    return f"Question ({self.nr}): " + self.question + "\n" + \
      "Answer1: " + self.answer1 + "\n" + \
      "Answer2: " + self.answer2 + "\n" + \
      "Answer3: " + self.answer3 + "\n" + \
      "Answer4: " + self.answer4 + "\n" + \
      "Image: " + self.img_src + "\n" + \
      "Correct answer: " + self.correct_answer + "\n"

  def __repr__(self):
    return {
      "id": self.nr,
      "question": self.question,
      "answer1": self.answer1,
      "answer2": self.answer2,
      "answer3": self.answer3,
      "answer4": self.answer4,
      "img_src": self.img_src,
      "correct_answer": self.correct_answer
    }


