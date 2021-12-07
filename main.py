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
    index = open("leetcodeindex.txt", "w")
    question_links = []
    update_question_links(question_links)
    i = 1
    for each_question_link in question_links:
        try:
            each_question_link = each_question_link[30:]
            data['variables'] = {"titleSlug": each_question_link}
            r = requests.post('https://leetcode.com/graphql', json=data).json()
            soup = BeautifulSoup(r['data']['question']['content'], 'lxml')
            difficulty = r['data']['question']['difficulty']
            title = r['data']['question']['title']
            question = soup.get_text()
            f.write(str(i))
            f.write(". ")
            f.write(title)
            f.write(
                "\n                                                                                                                                                                         ")
            f.write(difficulty)
            f.write("\n\n")
            f.write(question)
            f.write("\n")
            f.write("\n\n\n-----------------------------------------------\n\n\n")

            index.write(str(i))
            index.write(". ")
            index.write(title)
            index.write(
                "\n                                                                                                                                                                         ")
            index.write(difficulty)
            index.write("\n")
            print(i, "\n")
            i = i + 1

        except:
            i = i + 1
            continue


if __name__ == '__main__':
    print('\n')
    main()
