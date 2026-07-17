import re
import random

# 定义规则库：模式(正则表达式) -> 响应模板列表
rules = {
    r'I need (.*)': [
        "Why do you need {0}?",
        "Would it really help you to get {0}?",
        "Are you sure you need {0}?"
    ],
    r'Why don\'t you (.*)\?': [
        "Do you really think I don't {0}?",
        "Perhaps eventually I will {0}.",
        "Do you really want me to {0}?"
    ],
    r'Why can\'t I (.*)\?': [
        "Do you think you should be able to {0}?",
        "If you could {0}, what would you do?",
        "I don't know -- why can't you {0}?"
    ],
    r'I am (.*)': [
        "Did you come to me because you are {0}?",
        "How long have you been {0}?",
        "How do you feel about being {0}?"
    ],
    r'.* mother .*': [
        "Tell me more about your mother.",
        "What was your relationship with your mother like?",
        "How do you feel about your mother?"
    ],
    r'.* father .*': [
        "Tell me more about your father.",
        "How did your father make you feel?",
        "What has your father taught you?"
    ],
    r'.*': [
        "Please tell me more.",
        "Let's change focus a bit... Tell me about your family.",
        "Can you elaborate on that?"
    ]
}

# 定义代词转换规则
pronoun_swap = {
    "i": "you", "you": "i", "me": "you", "my": "your",
    "am": "are", "are": "am", "was": "were", "i'd": "you would",
    "i've": "you have", "i'll": "you will", "yours": "mine",
    "mine": "yours"
}

def swap_pronouns(phrase):
    """
    对输入短语中的代词进行第一/第二人称转换
    """
    words = phrase.lower().split()
    # get方法用于获取字典中指定键的值，第一个参数是键，第二个参数是默认值，如果键不存在，则返回默认值（这里是原单词）
    swapped_words = [pronoun_swap.get(word, word) for word in words]
    return " ".join(swapped_words)

def respond(user_input):
    """
    根据规则库生成响应
    """
    for pattern, responses in rules.items():
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            # 捕获匹配到的部分
            captured_group = match.group(1) if match.groups() else ''
            # 进行代词转换
            swapped_group = swap_pronouns(captured_group)
            # 从模板中随机选择一个并格式化
            # .format() 是 Python 字符串的格式化方法。
            # 它的作用是把括号里的内容，填进字符串中写着 {0} 的地方。
            response = random.choice(responses).format(swapped_group)
            return response
    # 如果没有匹配任何特定规则，使用最后的通配符规则
    return random.choice(rules[r'.*'])

# 主聊天循环
if __name__ == '__main__':
    print("Therapist: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Therapist: Goodbye. It was nice talking to you.")
            break
        response = respond(user_input)
        print(f"Therapist: {response}")

""" 
if __name__ == '__main__':

1. __name__ 是什么？
在 Python 中，每个文件都有一个内置的特殊变量叫 __name__，它的值会根据你运行这个文件的方式而自动改变。
判断当前这个 Python 文件是被“直接运行”的，还是被“作为模块导入”到别的代码中使用的。

2. 它的两种状态：
情景 A（直接运行）：
假如你在命令行里直接执行这个文件，比如输入 python ELIZA.py，Python 就会把这个文件里的 __name__ 变量的值设置为字符串 '__main__'。这时候，if __name__ == '__main__': 这个条件就成立了，它下面的代码（聊天循环）就会被执行。
情景 B（当做模块导入）：
假设你在另一个文件 app.py 中写了一句 import ELIZA，想要借用 ELIZA 里的 respond 函数。在这个时候，Python 会把 ELIZA.py 里的 __name__ 的值设置为模块的名字，也就是 'ELIZA'。这时候条件不成立，if 下面的代码就会被跳过。
3. 起到什么作用？（为什么要这么写？）

这么写起到了一个**“代码保护/隔离”**的作用。
在这个 ELIZA.py 代码中：
- repond() 函数和 rules 字典是可复用的逻辑。
- while True 的控制台聊天循环是具体的执行动作。
如果你不加 if __name__ == '__main__': 直接把 print 和 while 循环写在外面，当别人（或你在另一个文件）只不过想 import ELIZA 借用一下里面的函数时，就会瞬间触发那个控制台聊天死循环，导致程序卡在终端里。
加上这句话后，代码就变得兼具两面性：
- 自己就是个独立程序：直接双击运行它，它就能启动聊天。
- 也是个百搭的库：被别的文件 import 导入时，它乖乖地只提供函数，不引发额外的副作用（静默导入），绝不喧宾夺主执行多主启动聊天循环。
"""