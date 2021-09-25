from random import randint
import copy

story = (
    "Hồi đó {} có quen 1 người tên {}, {} rất là {} và {} rất thích hưởng thụ {}, cho đến khi {} gặp được {} và {} bắt đầu {}"
    # +
    # "We really wanted to see the {} play the {}. So, we {} our {} " +
    # "down to the {} and bought some {}s. We got into the game and " +
    # "it was a lot of fun. We ate some {} {} and drank some {} {}. " +
    # "We had a great time! We plan to go again next year!"
)

# story_story = (
#     "One day my {} friend and I decided to go to the {} game in {}. " +
#     "We really wanted to see the {} play the {}. So, we {} our {} " +
#     "down to the {} and bought some {}s. We got into the game and " +
#     "it was a lot of fun. We ate some {} {} and drank some {} {}. " +
#     "We had a great time! We plan to go again next year!"
# )

# Dictionary
word_dict = {
    'adjective': ['đen', 'lùn', 'ốm', 'xanh'],
    'name': ['Phương', 'Trang', 'Béc', 'Ly'],
    'food': ['Bún bò', 'Bún riêu', 'Capuchino', 'Pizza'],
    'subject': ['cô ấy', 'anh ấy', 'chú ấy', 'bà ấy'],
    # 'action verb':['run','fall','crawl','scurry','cry','watch','swim','jump','bounce'],
    # 'sports noun':['ball','mit','puck','uniform','helmet','scoreboard','player']
}


def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)


def create_story():
    ''' create a random story from word dict '''
    # create a local copy of the dict so that we can pop words as used
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('subject', local_dict),
        get_word('name', local_dict),
        get_word('subject', local_dict),
        get_word('adjective', local_dict),
        get_word('subject', local_dict),
        get_word('food', local_dict),
        get_word('name', local_dict),
        get_word('name', local_dict),
        get_word('name', local_dict),
        get_word('adjective', local_dict)
        # get_word('noun', local_dict),
        # get_word('noun', local_dict),
        # get_word('action verb', local_dict),
        # get_word('noun', local_dict),
        # get_word('noun', local_dict),
        # get_word('noun', local_dict),
        # get_word('adjective', local_dict),
        # get_word('noun', local_dict),
        # get_word('adjective', local_dict),
        # get_word('noun', local_dict)
    )


print("Story1:")
print(create_story())
print()
print("Story2:")
print(create_story())
print()
print("Story3:")
print(create_story())
