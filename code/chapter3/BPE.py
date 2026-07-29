import re, collections                 # 导入正则表达式模块和集合模块

def get_stats(vocab):                  # 定义函数：统计当前词表中相邻词元对的出现频率
    """统计词元对频率"""
    pairs = collections.defaultdict(int)# 创建一个默认值为0的字典用于计数
    for word, freq in vocab.items():   # 遍历词表中的每个单词及其频率
        symbols = word.split()         # 将单词按空格切分成字符或已组合的词元列表
        for i in range(len(symbols)-1):# 遍历这些词元
            pairs[symbols[i],symbols[i+1]] += freq # 统计相邻两个词元组合出现的总频率
    return pairs                       # 返回词元对频率字典

def merge_vocab(pair, v_in):           # 定义函数：将频率最高的词元对在词表中合并
    """合并词元对"""
    v_out = {}                         # 初始化合并后的新词表
    bigram = re.escape(' '.join(pair)) # 将要合并的词元对拼接并进行正则转义处理
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)') # 编译正则表达式：匹配独立的该词元对（两边不能是可见字符）
    for word in v_in:                  # 遍历原始词表中的每个单词
        w_out = p.sub(''.join(pair), word) # 使用正则替换，将空格连接的词元对替换成无空格的合并状态
        v_out[w_out] = v_in[word]      # 将合并后的新单词及原始频率存入新词表
    return v_out                       # 返回更新后的词表

# 准备语料库，每个词末尾加上</w>表示结束，并切分好字符
vocab = {'h u g </w>': 1, 'p u g </w>': 1, 'p u n </w>': 1, 'b u n </w>': 1} # 初始化带有频率信息的字符级词表
num_merges = 4 # 设置合并次数          # 设定我们要执行4次合并操作

for i in range(num_merges):            # 循环进行合并
    pairs = get_stats(vocab)           # 调用统计函数，获取当前的词元对频率
    if not pairs:                      # 如果没有可以合并的词元对
        break                          # 退出循环
    best = max(pairs, key=pairs.get)   # 找出频率最高（字典value最大）的词元对
    vocab = merge_vocab(best, vocab)   # 将这个频率最高的词元对在词库中进行合并
    print(f"第{i+1}次合并: {best} -> {''.join(best)}") # 打印合并过程：如 ('u', 'g') -> 'ug'
    print(f"新词表（部分）: {list(vocab.keys())}")   # 打印当前合并后的新词表形态
    print("-" * 20)                    # 打印分隔符