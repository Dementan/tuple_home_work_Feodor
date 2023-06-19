a = [i for i in range(10)]
print(a)
a1 = tuple(a)
print(a1, sum(a1))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

long_word = ("т", "т", "а", "и", "и", "а", "и", "и", "и", "т", "т", "а", "и", "и", "и", "и", "и", "т", "и")
print("т", "-", long_word.count("т"), "/", len(long_word))
print("а", "-", long_word.count("а"), "/", len(long_word))
print("и", "-", long_word.count("и"), "/", len(long_word))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp)
days = 7
mean_temp = sum_temp/days
print(int(mean_temp))