

# def calc_cache(cache, string, cache_size):
#     try:
#         if len(cache) > cache_size:
#             if cache.count(string) == 0:
#                 cache.pop()
#                 cache[0] += 1
#
#             elif cache.count(string) == 1:
#                 cache.remove(string)
#
#         else:
#             if cache.count(string) == 0:
#                 cache[0] += 1
#         cache.insert(1,string)
#
#     except:
#         cache[0] = len(cities)
#     finally:
#         return cache

def solution(cache_size, cities):
    time = 0
    cache_array = [' '] * cache_size

    for city in cities:
        city_lowered = city.lower()
        if city_lowered in cache_array:
            time += 1
            cache_array.remove(city_lowered)
            cache_array.append(city_lowered)
        else:
            time += 5
            cache_array.append(city_lowered)
            cache_array.pop(0)
    return time

print(solution(5,['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))