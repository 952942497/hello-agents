import collections                     # 导入集合模块用于计数

# 示例语料库，与上方案例讲解中的语料库保持一致
corpus = "datawhale agent learns datawhale agent works" # 定义一段简单的语料库字符串
tokens = corpus.split()                # 按空格将语料切割成单个单词列表（Token）
total_tokens = len(tokens)             # 计算语料库中总共有多少个单词

# --- 第一步：计算 P(datawhale) ---
count_datawhale = tokens.count('datawhale') # 统计单词 'datawhale' 出现的次数
p_datawhale = count_datawhale / total_tokens # 计算先验概率：'datawhale' 出现次数 / 总词数
print(f"第一步: P(datawhale) = {count_datawhale}/{total_tokens} = {p_datawhale:.3f}") # 打印结果

# --- 第二步：计算 P(agent|datawhale) ---
# 先计算 bigrams 用于后续步骤
bigrams = zip(tokens, tokens[1:])      # 将单词列表与向后错位一位的列表进行zip打包，生成相邻词对（Bigrams）
bigram_counts = collections.Counter(bigrams) # 统计每种词对出现的次数
count_datawhale_agent = bigram_counts[('datawhale', 'agent')] # 获取 'datawhale' 后面紧跟 'agent' 的次数
# count_datawhale 已在第一步计算         # （已经算过）
p_agent_given_datawhale = count_datawhale_agent / count_datawhale # 条件概率：在'datawhale'出现的前提下，下一个词是'agent'的概率
print(f"第二步: P(agent|datawhale) = {count_datawhale_agent}/{count_datawhale} = {p_agent_given_datawhale:.3f}") # 打印

# --- 第三步：计算 P(learns|agent) ---
count_agent_learns = bigram_counts[('agent', 'learns')] # 获取 'agent' 后面紧跟 'learns' 的次数
count_agent = tokens.count('agent')    # 统计独立单词 'agent' 出现的总次数
p_learns_given_agent = count_agent_learns / count_agent # 条件概率：在'agent'出现的前提下，下一个词是'learns'的概率
print(f"第三步: P(learns|agent) = {count_agent_learns}/{count_agent} = {p_learns_given_agent:.3f}") # 打印

# --- 最后：将概率连乘 ---
p_sentence = p_datawhale * p_agent_given_datawhale * p_learns_given_agent # 连乘计算得到整个句子 "datawhale agent learns" 出现的联合概率
print(f"最后: P('datawhale agent learns') ≈ {p_datawhale:.3f} * {p_agent_given_datawhale:.3f} * {p_learns_given_agent:.3f} = {p_sentence:.3f}") # 打印最终预测结果