main_input = """LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLL.LLLLLLLL..LLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLL.LL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
...L.L......L...L..L...L..LL.....L.....L..LLLL..L.LL......LL....L..L.L..L....L.LL....LL..L..L
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLL.LLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLL..LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLL.LLLLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL..LLLLLLLLLLLLLLLLL.LLLLLLLL.LLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL
LLLL.LLLLL.LLLL.LLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
.....L.LLLL....LL..L...LLL.L.LL..LL.L........L....LL...L...L...L.LL....LL...L..L.....LL.L....
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LL.LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LL.LLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL..LLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLL.LLLLL.LLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL..LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLL.LLLLLLLLLL.LLLLL.LL.LLLLLLLLLL
...L......L....L....L......L.L.....L..L.L.L..L.L...LLL.....LLLL.L.......LL.LLL.L.LL....L.....
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLL.L.LLLL.LLL
LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LL.L.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLL
...LL..........L..LLLLL...L.L..........L........L.LL..L..L.LLL.L..L.L.....LL...LL....L..L.L..
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLL.LLLL
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLL..LLLLLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLL.LLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLL.LLL.LLLL.LLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLL.LLLL.LLLLL..LLLLLLL.LLLLLLLLLL
LLLLLLLLL..L.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLL
..LLLL.LL....LLL..L...L..L..L.......L..L...L.L...L..LL.L.L.L.L...L...L.L.L.L.L......LL...L..L
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLL.LLLLL.LLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLL.LLL.LLLLLLLL.L.LLLLLL.LLLL.LLLL.LLLLLLLL.LLLL.LLLLLL.LLLLLL..LLLLLL.LLL
..L...L...L...L..L....L...LL.L.L.L..LL...........LLL.L......L..L.....LL..L..LLL........L....L
LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLL.LL.LLLL.LLLLLLL.L.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLL.L.LLLL.LLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LL.L.LLLLL
..L.L.LL....L....L..L....L.L...L..L..L.L.....L..L...L.LL.....L...............L..............L
LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LL.L.LLLL.LLL.LLLL.LLLLL.LL.LLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LL.L.LLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
L.L.....L.L.L.LL.L......LLL.....L.L.L........L....LL.......L....L.....L....LL..L...LLL......L
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLL.L.LLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLLL..LLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLL.LLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
...L...L.....L....L.L..........L..L.L..L..L..LL.L..L.......L.......L....L....L...LLL..L..L..L
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL
LLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL
..LLL....L.LL....L..............LLL......LL.LLL.....LL..L.L..L........L......L...L.LL..LL..L.
LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLL..LLLLLLLLLLLLLL.LLLLLLLLLL
L.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLL.LLL...LLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLL..LLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLLL.LLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
L...L.LL......L...LLLLLL.L.L.L...L.L..L..L.LL....L......LL..L...LLL....L...LL......L.........
LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLLL.LLL..LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLL.LLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
"""

final_state = """#L#L##L#L#.#L#L.#L#L#L#L#L#L#L#L#L#L#L#L#L#.#L#L#L#L#.L#L#L#L#.#L#L#L#L#L.L#LL#L#L..#L#L#L#LL
LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLLL#LL.LLLLL#LLLLLLLLLL
#L#L#L#L#L#L#L#L#L#L#L#L#.L#L#L#L#.##L#L#L#.#L##.#L##.L#L#L#L#.#L#L#L#L#L.L#L#L#LL.L#L#L#L#LL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLL.LL.LLLLL.LLLLLLLLLL#LLLLLLL#LLLLLLLLLLL
#L#L#L#L#L#L#L#.#L#L#L#L##L#L#L#L#.#L#L#L#L#L#L#.#L#L#L#LL#L#L#L#L#.#L#L#.L#L#L#LLL##L#L#L#LL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL#.LLLLLLLLLL
#L#L#L##.#L##L#.#L#L##L##.#L#L##L#.###L#L#L#L#L#.L#L###L##L#L#.##L#.#L#L#L#L#L#LLL.#L##L#L#LL
...L.L......L...L..L...L..LL.....L.....L..LLLL..#.LL......LL....L..L.L..L....L.L#....LL..L..L
#LLL#L#L#L#L#L#.#L#L#L##L#L#L#L#L#L#.#L#L#L.L#LL.L#L#.#L#L#L#L#L#L#.#L#L#.#L#L#LLL.L#L#L#LLLL
LL#LLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL#LLL#.LLLL.LLLLLLLL.LLLL.LLLL#.LLLLLL#L#LLLLLLL#LL
#LLL#L#L##.#L#..#L#L#L##L#L#L#L#L#.#L#L#L#L.L#LL.#L#L.L#L#L#L#.#L#L#L##LL.#L#L#LLL.L#L#L#LLLL
LL#LLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL#LLL#.LLLL#L#LLLLLL.LLLL.LLLL#.LLLLLL#L#LLLLLLL#LL
LLLL#L#L##.#L#L.L#L#L#LL#.#L#L#L#L.L#L#L#LLLL#LL.#L#L.LLL#L#L#.L#L#.#L#LL.#L#LLLLL.L#L#L#LLLL
#L#LLLLLLL.LLLL#L#L#LLLLL.LLLLLLLL#LLL#L#L##LLL#.LLLL.L#LLLLLLLLLLLL#LL.#LLLLL#L#L.LLLLLLL#LL
LLLL#L#L#L#L#LL..LLLLL#L#L#L#L#L#L.L#LLLLLL.L#L.L#L#L#LLL#L#L##L#L#.LL#LLL#L#LL.LL#L#L#L#LLLL
#L#L.LLLLL.L#L#.#L#.#LLLLLLLLLLL#L.LLL#L#L#.LLL#.LLLL.L#L#LLL#.LLLL.#LLL#L#LLL#L#L.LLLLLLL#LL
.....#.#L##....LL..L...###.#.#L..L#.#........#....#L...L...#...#.#L....LL...#..L.....L#.#....
#L#LLLLLLL.L#L#.#L#L#LLLL.LLLLLLLL.LL.L#L#L#LLL#.LLL#.#L#LLLL#LLLLL#LL#L#.#LLLL#L#.#LLLLLL#LL
LLLL#L#L##.LLLLLLLLLLL#L#.#L#L#LL#.#L#LLLLLLL#LL.#LLLLLLLLL#LL.#L#LLLLLLLLLLL#LLLL.LL.#L#LLLL
#L#LLLLLLL.##L#.#L#L#LLLL.LLLLLLLL.LLLLL#L#.LLL#..L#L#L#L#LLL#.LLLL.#LL#L#L#LLL#L#.#LLLLLL#LL
LLLL#L#L#L.L#LL.#LLLLL#L#.#L#L#LL#L#L#LLLLL.L#LL.#LLLLLLLLL#LL.L#L#.LLLLLLLLLLLLLL.LLL#L#LLLL
LL#LLLLLLL#LLL#.LL#L#LLLL.LLLLLLLL.#LLL#L#L#LLL#.LL#L.#LLLLLL#LLLLLLL.L#L#L#L#L#L#.LLLLLLLLLL
#LLL#L#L#L.L#LL.LLLLLL#L#.#L##L#L#.LLLLLLLLLL#LL.#LLL.LL#L#LLLL#L#L#L#LLL.LLLLLLLLLL#L#L#L#LL
LL#LLLLLLLLLLLL#L##L#LLLL.LLLLLLLL.##L#L#L#.LLL#.LL#L#LLLLLLL#.LLLL.LLLL#.#L#L#LLL#LLLLLLLLLL
#LLL##L#L#L#L#L..##LLL#L#.#L##L#L#.LLLLLLLL.##LL.#LLL.L#L#L#LL.L#L#L#L#LL.LLLLL.#L.L#L#L#L#LL
...L......L....#....#......L.L.....#..#.#.#..L.#...#L#.....LL#L.L.......L#.#L#.#.L#....L.....
#L#L#L#L#L#L#LL.LL#LLL#LL.L#L#L#L#.#L.LLLLLL#LLLL#LLL.LL#L#LLL.#LLL.L#LLL.LLLLLLLL.L.L#L#.#LL
LLLLLLLLLL.LLL#.#LLL#LLLL#LLLLL#L#L#L#L#L##.LL#L.LL.#.#LLLLLL#.#L#L#L#L#L#L#L#L#L#L##LLLLLLLL
LL#L#L#L#L#L#LL.LL#LLL#LL.L#L#LLLL.LLLLLLLLL#LLL#L#LL.LLLLL#LLLLLLL.LLLLLLLLLLLLLL.LLL#L#L#LL
#LLLLL#L#L.L#L#.#LLL#LLL#.LLLLL#L#.#L#L#L#L.#L#L.LLL##L#L#L#L#.L#L#.#L#L#L#L#LL#L#L#LLLLLLLLL
...##..........L..#LLL#...#.#..........L........#.#L..L..L.LLL.L..L.L.....LL...LL....#..#.#..
#LLLLLL#L#.#L#L#LLLL#LLL#LLLLL#L#L.L#L#L#L#.#L#LLLLL#.#L#L#L##L##L#L#L#L#.##L#L#L#.#LLLL.LLLL
LL#LLLLLLL.LLLLLLL#LLL#LLL#L#LLLLL#LLLLLLLL.LLLL#L#LLL..LLLLLL.LLLL.LLLLL.LLLLLLLL.LL##L#L#LL
#LLL#L#L#L#L#L#.#LLL#LLL#.LLLL#L#L.L#L#L#L#.#L#LLLLL#.#L#L#L#L#L#L#.#L#L#.##L#L#L#.#LLLLLLLLL
LL#L.LLLLL.LLLL.LL#LLL#LLL#L#LLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.#LLLL.LLLLLLLL.LL##L#L#LL
#LLL#L#L##.#L#L.#LLL#LLL#.LLLLL#L#.##L#L#L#.#L##L#L#L#L#L#L#L#.L#L#.LL#L#.#L##L#L#.#LLLLLLLLL
LL#LLLLLLLLLLLLLLL#LLL#LL.#L##LLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL.#LLLL.LLLLLLLL.LLLLLLLLLL
#LLL#L#L#L#L#L#.#L#L#LLL#.LLLLL#L#.#L#L#L#L#L#L#.#L#L.#L#L#L#L#L#L#LLL#L#.#L#.L#L#.#L##L#L#LL
LL#LLLLLLL.LLLLLLLLLLLLLL.L##LLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLL.LLLL.#LLLL..LLLLLLL.LLLLLLLLLL
#LLL#L#L#..#.#L#L#L#L#L###LLLL#L#L####L#L#L###L#.##L#.#L#L#L#L#L#L#LLL#L#.#L##L#L#.#L##L#L#LL
..#LLL.LL....LLL..L...L..L..#.......L..L...L.L...L..LL.L.L.L.L...L...L.L.L.L.L......LL...L..L
#LLL#L#L##.#L#L#L##L#L#L#L#LLL.#L#L#L#L#L###L###.##L#.#L#L#L##.##L#.#L#L#.#L#L#.#L###L#L#L#LL
LL#LLLLLLL.LLLLLLLLLLLLLL.LL##LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLL
#LLL#L#L#L##L#L#LL#L#L#L#.#LLLL#L#.L#L#L#L#.#L#L.##L#.#L#L#L#LLL#L#.#L#L#.L#L#L#L#.##L#L#L#LL
LL#LLLLLLLLLLLL.LLLLLLLLL.LL##LLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLL#LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
#LLL#L#L#L#L#L#L#L#L#.#L#.#L##L#L#.#.L#L#L#.#LL#.##L#.#L#L#L#L.L#L#.L#L#L#.##L#L#..#L#L##.#LL
..#...L...L...L..L....L...LL.L.L.L..LL...........LLL.L......L..L.....LL..L..LLL........L....L
#LLL#L#L##.#L#L#L#L#L#L##.#L##L#L#.#L#L#L#L#L#L#.##L#L#L#L##L#.#L##L#L#L#.#L#L##L#.#L#L##L#LL
LL#LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLLLL
#LLL#L#L#L.##L#.#L#L#L#L#L#LL#L#L#.#LL#L#L#L#.#L#L#L#.##L#L#L#.#L#L##L#L#.#L#L#L#L##L##L#L#LL
LL#LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
#LLL#L#L#L#L#L#L#L#L#L#L#.#LL#L#L#.#L#L#L#L#L#L#.#L#L#L#.L#L#L#L#L#.#L#L#L#L#L#L#L#L#L#L#L#LL
LL#LLLL.LL.LLLL.LLLLLLL.L.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
#LLL#L##L#.##L#.#L#L#L#L#.#L#L#L#L.L#L#L#.#.#L##.L#L#.#L#L#L#L#L#L#.#L#L#.##L#L#L#.#L.#.#L#LL
..#.L.LL....L....L..L....L.L...L..#..L.L.....L..L...L.LL.....L...............L..............L
#LLL#L#L#L.#L##L#L##.#L##L#L##L#LL.L#L#L#L#.#L#L#L#L#.##L#L#L#.#LL#.#L#L#.#L#LL#L#.#L#LL#L#LL
LL#LLLLLLLLLLL#.LLLLLLLL#.LLLLLLL#.LLLLLLLLLLLLL.LL.#.LLLL.LLL.LLLL.LLLLL.LL.LLLLL.LLLLLLLLLL
#LLL#L#L#L#L#LL.#L#L#L#LL.#L#L##LL.##L#L#L#.L#L#.##.#.##L#L#L#.#LL#.#L#L#L##L#L#L#.#L#LL#L#LL
LL#LLLLLLL.LLL#LLLLL.LLL#LLLLLLLL#.LLLLLLLL.#LLL.LLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
#LLL#L#LLL.L#LL.#L#L#L#LL.#L#L##LL.#L#L#L##.#L#L#L#L#L#L#L#L#L#L#L#.#L#L#L#L#L#.L#.#L##L#L#LL
LL#LLLLL#L#LLL#.LLLLLLLL#.LLLLLLL#.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
#LLL#L#LLL.L#L#.#L#L#L#L#.#L#L#LLL.###L#L#L#L#L#.#L#L#L#L#L#L#.##L#.#L#L#L#L#L##L#.#L##L#L#LL
L.#.....#.#.L.LL.L......LLL.....#.L.L........L....LL.......L....L.....L....LL..L...LLL......L
#LLL#L#LLL.L#L#L#L#L#L#L#L#L###LLL#L#L#L#L#.##L#.#L#L.L#L#L#LL.L#L#.#L#L#.#L#L#L#L#L#L#L#L#LL
LL#LLLLL#L#LLLL.LL#L#LLLLLLLLL#L#L.LLLLLL.L.LLLL.LLLL#LLLLLLLL#LLLLLLLLLL.LLLLLLLL.LLLLLLLLLL
#LLL#L#LLL.L#L#L#L.LLL#L#.#L#LLLLLL#L#L#L#L#L#L#.#L#L.L#L#L##L.L#L#.#L#L#L#L#L#L#L.L#L#L#L#LL
LL#LLLLL##..LLL.LLLL#LLLL.LLLLL#L#.LLLLLLLLLLLLL.LLLL#LLLLLLLL.LLLLLLLLLLLLLLLLLLL#LLLLLLLLLL
#LLL#L#LLL.##L#.#L#LLL#L#.#L#LLLLL.##L#L#L#.L#L#.#L#L.L#L#L##L#L#L#.#L#L#.#L#L#LLL.L#L#L#L#LL
LL#LLLLL#LLLLLL.LLLL#LLLL.LLLL#LL#.LLLLLLLLLLLLLLLLLL#LLLLLLLL.LLLL.#LLLL.LLLLLLL#.LLLLLLLLLL
#LLLL#LLLL#L#L#L#L#LLL#L#.#L#LLLLL.L#L#L#L#.##L#.#L#L.L#L#.#L#.#L#L.L#L#L###L#L#LL.##L#L#L#LL
...#...#.....L....L.#..........#..#.#..L..L..LL.L..L.......L.......#....L....L...#LL..#..L..L
#LLLLLLLLL#L#LL.#L#LLL#L#.#L#LLLLL.LLLL#L#L#L#L#.#L#L#.#L#L#L#L#L#L.LL#L#L#L##L#LL.##LLL#LLLL
LL#L#L#L#L.L#L#.LLLL#L#L#L#L#L#L#L.L##LLLLL.LLLL.#LLL.LLLLLLLLLLLLLL#L#L#.#LLLLLL#.LLL#LLL#LL
LLLLLLLLLL.LLLL.#L#LLLLLL.LLLLLLLL#LLL#L#L#.#L#L.LLL#.#L#L#L#L#L#L#LLLLLL.LLLLLLLLLLLLLL#LLLL
#L#L#L#L.#L##L#.LL#L#L#L#.#L#L#L#L.L#L#LLLL.LLLL###LL.LLLLLLLLLL#L#.#L#L#.#L#L#L#L#L#L#LLL#LL
..LLL....L.LL....L..............LLL......L#.#L#.....#L..#.#..#........#......L...L.LL..LL..L.
#L#L#L##L#L#L##L#L#L#L#L#.#L#L#L#L#L#L#L#LL.LL#L.L#LL.#LLLLLLL.#LL#.#LLL#.#L##L#L#.##L#L#L#LL
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL#L#LLL#LLL#.LLL#L#L#.LLL..LL#LLLLLLLLLLL.LLLLLLLLLL
#.#L#L#L#L.#L#L#L#L#L#L##L#L#L#LL#LLL#L#L##L#L#L.L#LL.L#LLLLLL.##L#.#LLL#.#L##L#L#.L#L#L#L#LL
LLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLL.#LLLLLLL.LLLL.LLLL#LLL#L#L#.LLL...L#LLLLLLLLLLLLLLLLLLLLLL
#L#L#L#L#L#L#L#L#L#LLL#L#..#L#L#L#LLL#L#L#L#L#L#.#L#L.L#LLLLLL.##L#.#LLL#.#L#L#L#L#L#L#L#L#LL
LLLLLLLLLL.LLLL.LLLL#LLLLLLLLLLLLL.#LLLLLLL.LLLL.LLLL#LLL#L#L#.LLLL.LL#LLL#LLLLLLLLLLLLLLLLLL
#L#L#L#LL#.L#L#.#L#.LL#L#.#L#L#L#L.LL#L#L#L#L#L#.#L#L.L#L#L#L#.#L#L##L#L#.#L#L#L#L#L#L#L#L#LL
LLLLLLLLLLLLLLL.LLLL#LLLL.LLLLLLLL#LLLLLLLL.LLLL.LLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLL
#L#L#L#L#L#L#L#.#L#L#L#L#.#L#L#L#L#L#L#L#L#.##L#.#L#L#L#L#L#L#.##L#.#L#L##L#L#L#L#.##L#L#L#LL
L...L.LL......L...LLLLLL.L.L.L...L.L..L..L.LL....L......LL..L...LLL....L...LL......L.........
#L#L#L##L#.#LL#.#L#L#L#L#.#L#L##L#.##L#L#L#.#L##.##L#.#L#L##L##L#L#.#L#L#.##L#L#L#.L#L#L#L#LL
LLLLLLLLLL.LLL..LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLL#L.LLLLLLLLLLLLLLLLLL
#L#L#L##L#L#L##.#L#L#L#L#.#L#L#L##.##L#L#L#.#L#L.#LL####L#L#L#L#L##.#L#L#L#.L#L#L#L#L#L#L##LL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLL.LLLL
#L#L#L#L#L#L#L#.#L#L#L#L#.#L#L#L#L#L#L#L#L#.#L#L#L#L##L#L#L#L#.#L#L.#L#L##L#L#L#L#.L#L#L#L#LL
"""