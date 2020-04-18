import re

cancer_text = ['breast_cancer.txt', 'colorectal_cancer.txt', 'lung_cancer.txt', 'prostate_cancer.txt',
               'skin_cancer.txt']

# cancer_text = ['breast_cancer_copy.txt']

for file in cancer_text:
    with open(file, 'r') as f:
        text = f.read()
        f.close()
    with open(file, 'w') as f:
        print('pre-processing the file {}'.format(file))
        text = re.sub("[!@#$+%*:()'-]", ' ', text)
        text = text.lower()
        f.write(text)
        f.close()
