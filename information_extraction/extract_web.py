from bs4 import BeautifulSoup

from information_extraction.web_reader import read_web_content

breast_cancer = ['https://www.mayoclinic.org/diseases-conditions/breast-cancer/symptoms-causes/syc-20352470',
                 'https://www.mayoclinic.org/diseases-conditions/breast-cancer/diagnosis-treatment/drc-20352475']

lung_cancer = ['https://www.mayoclinic.org/diseases-conditions/lung-cancer/symptoms-causes/syc-20374620',
               'https://www.mayoclinic.org/diseases-conditions/lung-cancer/diagnosis-treatment/drc-20374627']

skin_cancer = ['https://www.mayoclinic.org/diseases-conditions/skin-cancer/symptoms-causes/syc-20377605',
               'https://www.mayoclinic.org/diseases-conditions/skin-cancer/symptoms-causes/syc-20377605']

colorectal_cancer = ['https://www.mayoclinic.org/diseases-conditions/colon-cancer/symptoms-causes/syc-20353669',
                     'https://www.mayoclinic.org/diseases-conditions/colon-cancer/diagnosis-treatment/drc-20353674']

prostate_cancer = ['https://www.mayoclinic.org/diseases-conditions/prostate-cancer/symptoms-causes/syc-20353087',
                   'https://www.mayoclinic.org/diseases-conditions/prostate-cancer/diagnosis-treatment/drc-20353093']

cancer_dict = {'breast_cancer': breast_cancer, 'lung_cancer': lung_cancer, 'skin_cancer': skin_cancer,
               'colorectal_cancer': colorectal_cancer, 'prostate_cancer': prostate_cancer}

skip_list = ['colorectal_cancer', 'lung_cancer', 'skin_cancer', 'prostate_cancer.txt']

for key, value in cancer_dict.items():
    final_content = ""
    if key in skip_list:
        continue
    for url in value:
        print('extract from {}'.format(url))
        content = read_web_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        for each in soup.find_all('p'):
            final_content = final_content + '\n' + each.get_text()

    print('writing file {} '.format(key + '.txt'))
    with open(key + '.txt', 'w') as f:
        f.write(final_content)
        f.close()
