import numpy as np                     # 导入 Numpy 库进行矩阵和向量运算

# 假设我们已经学习到了简化的二维词向量
embeddings = {                         # 用一个字典模拟已经训练好的词向量模型（此处为了简化，降维到二维）
    "king": np.array([0.9, 0.8]),      # 国王的向量
    "queen": np.array([0.9, 0.2]),     # 皇后的向量
    "man": np.array([0.7, 0.9]),       # 男人的向量
    "woman": np.array([0.7, 0.3])      # 女人的向量
}

def cosine_similarity(vec1, vec2):     # 定义计算向量余弦相似度的函数
    dot_product = np.dot(vec1, vec2)   # 计算两个向量的点积（内积）
    norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2) # 分别计算两个向量的正则化范数（长度）并相乘
    return dot_product / norm_product  # 余弦相似度 = 点积 / (范数乘积)，值域[-1, 1]，越接近1相似度越高

# king - man + woman
result_vec = embeddings["king"] - embeddings["man"] + embeddings["woman"] # 词向量代数运算，模拟推断概念："剥离男性特征并加入女性特征的国王"

# 计算结果向量与 "queen" 的相似度
sim = cosine_similarity(result_vec, embeddings["queen"]) # 计算刚刚代数运算出的坐标，跟字典内现有的 "queen" 的坐标的相似程度

print(f"king - man + woman 的结果向量: {result_vec}") # 打印推导出的目标向量坐标（这里运算得出是 [0.9, 0.2]）
print(f"该结果与 'queen' 的相似度: {sim:.4f}")      # 打印结果：在此简化例子中完全重合，相似度为1.0