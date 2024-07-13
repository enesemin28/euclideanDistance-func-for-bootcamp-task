import math

def euclideanDistance():
    points = [(6, 8), (3, 4), (10, 12), (4, 6)]
    distances = []
    
    for i in range(len(points) - 1):
        distance = math.dist(points[i], points[i + 1])
        distances.append(distance)
        print(f"Distance between {points[i]} and {points[i + 1]}: {distance}")

    min_distance = min(distances)
    print("Shortest distance:", min_distance)

euclideanDistance()