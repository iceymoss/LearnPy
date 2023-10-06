points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}, 
          {'x': 6, 'y': 0.3},
          {'x': 8, 'y': 3},
          {'x': 10, 'y': 2}, 
          {'x': 12, 'y': 5}]
points.sort(key=lambda i: i['y'])
print(points)

points.sort(key=lambda i: i['x'])
print(points)