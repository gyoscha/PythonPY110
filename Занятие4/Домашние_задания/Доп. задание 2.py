# Написать регулярку для проверки валидности ip адреса.
# Как правило, адрес записывается в виде четырёх десятичных чисел значением
# от 0 до 255, разделённых точками, например, 192.168.0.3.
#
# правильные ip
# 192.168.0.1
# 10.0.0.1
# 172.16.0.0
# 255.255.255.0
# 232.12.0.14
# 111.111.111.111
# 0.0.0.0
#
# неправильные ip адреса
# 256.257.258.259
# 2516.257.258.259
# 1921.168.0.1
# 10.1233.0.1
# 172.16.7890.0
# 255.255.255.68779
# 232.0.14
# 111.111.111.111.123