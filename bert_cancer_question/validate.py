import textwrap
from bert_cancer_question.bert_cancer_question_answer import answer_question
from bert_cancer_question.metrics import get_bleu_score, get_rouge_score

# Wrap text to 80 characters.
wrapper = textwrap.TextWrapper(width=160)

bert_abstract = '''Most lung cancers don't cause symptoms until the disease has advanced, in part because the lungs have few nerve endings. When lung cancer does cause signs in its early stages, they may vary from person to person but commonly include:
A new cough that is persistent or worsens, or a change in an existing chronic cough
Cough that produces blood
Pain in the chest, back or shoulders that worsens during coughing, laughing or deep breathing
Shortness of breath that comes on suddenly and occurs during everyday activities
Unexplained weight loss
Feeling that you are tired or weak
Loss of appetite
Lung infections such as bronchitis or pneumonia that won't go away
Hoarseness or wheezing

Less common symptoms of lung cancer may include:
Swelling in the face or neck
Difficulty swallowing or pain while swallowing
Changes in the appearance of fingers, called finger clubbing
Although most of these symptoms are more likely to be caused by something other than lung cancer, it's important to see a doctor. Discovering lung cancer early may mean more treatment options are available.'''

question = "What are Less common symptoms of lung cancer?"
manual_answer = 'Swelling in the face or neck Difficulty swallowing or pain while swallowing Changes in the appearance of fingers, called finger clubbing'
generated_answer = answer_question(question, bert_abstract)

print('--------------------------------------------')
print("Abstract Fed to the QA System")
print('--------------------------------------------')
print(wrapper.fill(bert_abstract))
print('--------------------------------------------')
print("Question Asked to System")
print('--------------------------------------------')
print(question)
print('--------------------------------------------')
print('manual answer given by user')
print('--------------------------------------------')
print(manual_answer)
print('--------------------------------------------')
print('system answer given by user')
print('--------------------------------------------')
print(generated_answer)
print('--------------------------------------------')
print('Rouge Score for the generated answer')
print('--------------------------------------------')
print(get_rouge_score(manual_answer, generated_answer))
print('--------------------------------------------')
print('BLEU Score for the generated answer')
print('--------------------------------------------')
print(get_bleu_score(manual_answer, generated_answer))
