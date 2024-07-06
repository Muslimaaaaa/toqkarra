# def karra_table(n, start=1, end=11):
#     """
#     bunda n ga biron son berilsa faqat o'sha sinning karra jadvalini chiqaradi:
#     """
#     for i in range(start, end):
#         yield n, i, n* i
#
# n = 9
# for a, b, natija in karra_table(n):
#     print(f"{a} x {b} = {natija}")


def karra_jadvali(n):
    """
    bunda n ga biron son berilsa shu songacha bo'lgan barcha sonlarning karra jadvalini chiqazadi
    """
    for i in range(1, n+1):
        for j in range(1, n+1):
             yield f"{i} x {j} = {i * j}"
n = 9
for item in karra_jadvali(n):
     print(item)
