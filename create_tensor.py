# coding: utf-8 
# @Time    : 2022/9/10 16:59
# @Author  : taon
# @Software: PyCharm

import torch

# 通过列表创建tensor
a = torch.Tensor([1, 2, 3])
print(a)
print(a.type())

# 创建高维tensor
b = torch.Tensor([[1, 2], [3, 4]])
print(b)
print(b.type())

# 通过shape创建tensor
c = torch.Tensor(2, 3)
print(c)

# 通过rand模块创建tensor
d = torch.rand(2, 3)
print(d)

# 创建一个正太分布的tensor
e = torch.normal(0.0, std=torch.rand(5))
print(e)

f = torch.normal(mean=torch.rand(5), std=torch.rand(5))
print('f:', f)

# 创建全1或者是全0的tensor
g = torch.ones(3, 3)
print('g:', g)

# 创建均匀分布的tensor
h = torch.Tensor(2, 3).uniform_(-1, 1)
print('h:', h)

# 使用arange创建tensor
i = torch.arange(10)
print('i:', i)

j = torch.linspace(2, 10, 3)
print('j:', j)

# tensor乘法
k = torch.Tensor(2, 3)
m = torch.Tensor(3, 2)
print('@乘法:', k @ m)
print('matmul:', k.matmul(m))
print('mm:', k.mm(m))
print(torch.matmul(k, m))

# 高维tensor乘法
n = torch.Tensor(1, 2, 3, 4)
p = torch.Tensor(1, 2, 4, 3)
print(n.matmul(p).shape)

# 三角函数
r = torch.zeros(3)
print(torch.cos(r))

# 采样，设置随机的种子，保证每次采样的结果是一致的
torch.manual_seed(1)
s = torch.normal(0, 1, (2, 3))
print('s:', s)
