import textwrap
from bert_cancer_question.bert_cancer_question_answer import answer_question
from bert_cancer_question.metrics import get_bleu_score, get_rouge_score

# Wrap text to 80 characters.
wrapper = textwrap.TextWrapper(width=160)

bert_abstract = '''If the UE has more than one EPS bearer active, the MME sends QoS profile for only one EPS bearer to the eNB. 
In this case the MME uses local configuration (e.g. considering table 6.1.7 in TS 23.203 [6], 
the MME chooses the non-GBR EPS bearer with the QCI corresponding to the highest Priority Level) to determine which EPS bearer's QoS to send to the eNB.
 If the MME has no EPS bearers active for the UE, then this fact is indicated to the eNB. '''

question = "who is the sender?"
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
