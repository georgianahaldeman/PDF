def get_fit(small: int, side: str) -> int:
    large = int(input(f"Box {side}? "))
    fit = large // small
    print(f"{fit} Rubik's cubes will fit {side}-wise.")
    return fit
def main() -> None:
    cube_len = int(input("Cube length? "))
    width = get_fit(cube_len, 'width')
    height = get_fit(cube_len, 'height')
    length = get_fit(cube_len, 'length')
    fit = width * height * length
    print(str(fit)+" Rubik's cubes will fit in that container.")
# main()