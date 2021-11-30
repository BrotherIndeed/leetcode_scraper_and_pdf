import requests
from bs4 import BeautifulSoup

data = {"operationName": "questionData", "variables": {"titleSlug": "two-sum"}, "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}


def update_question_links(question_links):
    with open('question_links.txt') as f:
        links = f.read()
    links = links.split('\n')

    for each in links:
        if '/problems/' in each:
            question_links.append(each)


def main():
    f = open("leetcode.txt", "w")

    question_links = []
    update_question_links(question_links)
    i = 1
    for each_question_link in question_links:
        try:
            each_question_link = each_question_link[30:]
            data['variables'] = {"titleSlug": each_question_link}
            r = requests.post('https://leetcode.com/graphql', json=data).json()
            soup = BeautifulSoup(r['data']['question']['content'], 'lxml')
            title = r['data']['question']['title']
            question = soup.get_text()
            f.write(str(i))
            f.write(". ")
            f.write(title)
            f.write("\n\n\n")
            f.write(question)
            f.write("\n")
            f.write("\n\n\n-----------------------------------------------\n\n\n")
            print(i, "\n")
            i = i + 1

        except:
            i = i + 1
            continue


if __name__ == '__main__':
    print('\n')
    main()

# open google chrome, navigate to leetcode problems page
# click on inspect, navigate to dev console and paste the commands below.
# copy question links and paste in text file named question_links.txt
# go to next page and repeat till you have all the questions links.
# put python script and question link file in same folder.
# run and wait to compile to text file, the convert to pdf online.
# var x = document.querySelectorAll("a");
# var myarray = []
# for (var i=0; i<x.length; i++){
#   if(x[i].getAttribute('href').indexOf('problem') > -1 && x[i].getAttribute('href').indexOf('solution') == -1 )
#   {
#   var cleanlink = x[i].href;
#   myarray.push([cleanlink]);
#   }

# };
# function make_table() {
#     var table = '<table><thead><th>Links</th></thead><tbody>';
#    for (var i=0; i<myarray.length; i++) {
#             table += '<tr><td>'+ myarray[i][0] ;
#     };

#     var w = window.open("");
# w.document.write(table);
# }
# make_table()
