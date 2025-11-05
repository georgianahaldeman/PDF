cube_len = int(input("Cube length? "))
box_w = int(input("Box width? "))
box_h = int(input("Box height? "))
box_l = int(input("Box length? "))

fit_w = box_w // cube_len
fit_h = box_h // cube_len
fit_l = box_l // cube_len

print(str(fit_w)+" Rubik's cubes will fit width-wise.")
print(str(fit_h)+" Rubik's cubes will fit height-wise.")
print(str(fit_l)+" Rubik's cubes will fit length-wise.")

res = fit_w * fit_h * fit_l
print(str(res)+" Rubik's cubes will fit in that container.")