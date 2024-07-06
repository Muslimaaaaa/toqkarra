# def toq_son(n):    #>>>>>>>>>>>generator orqali yaratildi>>>>>>>>>>>
#     i = 0
#     while i <= n:
#       if i%2 == 1:
#         yield i
#       i += 1
#
# gen = toq_son(10)
# for i in gen:
#     print(i)


class OddNumberIterator:        #>>>>>>>>>>>itenator orqali yaratildi>>>>>>>>>>>
  def __init__(self, start=1):
    self.current = start - 1 if start % 2 == 0 else start

  def __iter__(self):
    return self

  def __next__(self):
    num = self.current
    self.current += 2
    return num

odd_iterator = OddNumberIterator(1)
for num in odd_iterator:
  if num > 20:
    break
  print(num)
