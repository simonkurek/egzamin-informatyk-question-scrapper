from question.Question import Question


class QuestionBuilder:
  question_id: int = -1
  question: str = ""
  answer_a: str = ""
  answer_b: str = ""
  answer_c: str = ""
  answer_d: str = ""
  correct_answer: str = ""
  img_src: str = ""

  @staticmethod
  def create():
    return QuestionBuilder()

  def with_id_text(self, id_text: str):
    try:
      q_id = int(id_text.split(' ')[3])
      self.question_id = q_id
    except:
      print("Something went wrong with question id parsing to int")
    return self

  def with_question_text(self, question_text: str):
    self.question = question_text
    return self

  def with_answer_a(self, answer_a_text: str):
    self.answer_a = answer_a_text
    return self

  def with_answer_b(self, answer_b_text: str):
    self.answer_b = answer_b_text
    return self

  def with_answer_c(self, answer_c_text: str):
    self.answer_c = answer_c_text
    return self

  def with_answer_d(self, answer_d_text: str):
    self.answer_d = answer_d_text
    return self

  def with_img_src(self, img_src: str):
    self.img_src = img_src
    return self

  def with_correct_answer(self, answer_correct_text: str):
    self.correct_answer = answer_correct_text
    return self

  def build(self):
    return Question(
      self.question_id,
      self.question,
      self.answer_a,
      self.answer_b,
      self.answer_c,
      self.answer_d,
      self.img_src,
      self.correct_answer
    )
