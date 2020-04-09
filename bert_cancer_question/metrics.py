from nltk import word_tokenize
from nltk.translate.bleu_score import sentence_bleu
from bert_cancer_question.pyrouge import Rouge


# nltk.download('punkt')


def get_bleu_score(reference, candidate):
    print(word_tokenize(reference))
    print(word_tokenize(candidate))
    score = sentence_bleu(word_tokenize(reference), word_tokenize(candidate), weights=[0.5, 0.5])
    return '%f' % score


def get_rouge_score(reference_summary, generated_summary):
    r = Rouge()
    [precision, recall, f_score] = r.rouge_l([generated_summary], [reference_summary])
    print("Precision is :" + str(precision) + "\nRecall is :" + str(recall) + "\nF Score is :" + str(f_score))
    return str(precision), str(recall), str(f_score)


'''

system_generated_summary = "The Kyrgyz President pushed through the law requiring the use of ink during the upcoming Parliamentary and Presidential elections In an effort to live up to its reputation in the 1990s as an island of democracy. The use of ink is one part of a general effort to show commitment towards more open elections. improper use of this type of ink can cause additional problems as the elections in Afghanistan showed. The use of ink and readers by itself is not a panacea for election ills."
manual_summmary = "The use of invisible ink and ultraviolet readers in the elections of the Kyrgyz Republic which is a small, mountainous state of the former Soviet republic, causing both worries and guarded optimism among different sectors of the population. Though the actual technology behind the ink is not complicated, the presence of ultraviolet light (of the kind used to verify money) causes the ink to glow with a neon yellow light. But, this use of the new technology has caused a lot of problems. "

print(str(float(get_bleu_score('it is a cat at room', 'it is a cat inside room'))))
print(get_rouge_score(manual_summmary, system_generated_summary))
'''
