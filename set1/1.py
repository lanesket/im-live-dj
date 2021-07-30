# 31.7.21

d1 >> play("x x ")
d2 >> play("*   ")

d2 >> play("* **" + " " * 8)
d1 >> play(P["x x "] & P[" -"] & P["o   "])
d1 >> play(P["x x "] & P[" -"])
d1 >> play(P["x x "] & P["--"] & P["=   "])
d1 >> play(P["x x "] & P["--"] & P[" "], dur=[1/2, 1/2, 1/2, 1/2])

d1.stop()
d2.stop()

d1.solo()
d2.solo()

d3 >> play("  xx", dur=[1, 1, 3/4, 3/4], amp=[0, 0, 3, 7])
d3.stop()

d4 >> play("----", dur=[1/2, 3/4, 3/4, 1], amp=[1, 2, 1, 2])
p1 >> play("fK  ", dur=[1/2, 1/2, 1/2, 3/4])
p1 >> play(P["f  K"] & P[" " * 6 + "+"])
p3 >> play("HH", dur=1/4)
p3 >> play(" p")
p1 >> play("X   " * 4, dur=0.5)
p3.stop()
p2 >> play("t" * 6 + " ")
