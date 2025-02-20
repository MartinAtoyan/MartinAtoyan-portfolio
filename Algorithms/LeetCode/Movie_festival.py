import sys

def sortFnc(p):
    return p[1]

def solve(movies):
    movies.sort(key=sortFnc)

    timeElapsed = 0
    moviesWatched = 0

    for movie in movies:
        if movie[0] >= timeElapsed:
            moviesWatched += 1
            timeElapsed = movie[1]
    
    return moviesWatched

def main():
    n = int(sys.stdin.readline().strip())  
    movies = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

    print(solve(movies))

if __name__ == "__main__":
    main()
