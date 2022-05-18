from selenium import webdriver
from selenium.webdriver.common.by import By
from question.QuestionBuilder import QuestionBuilder
from question.Question import Question
import json
import sys

driver = webdriver.Safari()

def question_toJSON(question):
  return json.dumps(question.__dict__)

def get_question() -> Question:
  driver.get("https://egzamin-informatyk.pl/jedno-pytanie-inf02-ee08-sprzet-systemy-sieci/")
  driver.implicitly_wait(7)
  questionIdElem = driver.find_element(By.CLASS_NAME, "onequestion")
  questionTextElem = driver.find_element(By.CLASS_NAME, "tresc")
  answerATextElem = driver.find_element(By.ID, "odpa")
  answerBTextElem = driver.find_element(By.ID, "odpb")
  answerCTextElem = driver.find_element(By.ID, "odpc")
  answerDTextElem = driver.find_element(By.ID, "odpd")

  questionBuilder = QuestionBuilder.create() \
    .with_id_text(questionIdElem.text) \
    .with_question_text(questionTextElem.text) \
    .with_answer_a(answerATextElem.text) \
    .with_answer_b(answerBTextElem.text) \
    .with_answer_c(answerCTextElem.text) \
    .with_answer_d(answerDTextElem.text)


  try:
    imgElem = driver.find_element(By.CLASS_NAME, "img-responsive")
    questionBuilder.with_img_src(imgElem.get_attribute("src"))
  except:
    pass

  answerATextElem.click()

  answerGoodElem = driver.find_element(By.CLASS_NAME, "odpgood")
  questionBuilder.with_correct_answer(answerGoodElem.text[0])

  question = questionBuilder.build()
  return question

while True:
  try:
    qst = get_question()
    print(qst)
    with open(f'data/q{qst.nr}.json', 'w') as outfile:
        json.dump(qst.__dict__, outfile)
  except KeyboardInterrupt:
    print("Stopping...")
    sys.exit()
  except:
    print("Something went wrong")
    continue


