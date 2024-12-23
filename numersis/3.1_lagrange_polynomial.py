x = [0, 10, 20, 30, 40, 50]
y = [179323,	203302,	226542,	249633,	281422,	308746]

m=len(x)
n = m - 1

xp = -10
yp = 0 #sum from 0
for i in range(n + 1):
  p = 1
  for j in range(n + 1):
    if j != i:
      p*=(xp - x[j])/(x[i] - x[j])
  yp += y[i]*p
print("For x = %.3f, y = %.3f" % (xp, yp))

xp = 15
yp = 0 #sum from 0
for i in range(n + 1):
  p = 1
  for j in range(n + 1):
    if j != i:
      p*=(xp - x[j])/(x[i] - x[j])
  yp += y[i]*p
print("For x = %.3f, y = %.3f" % (xp, yp))

xp = 54
yp = 0 #sum from 0
for i in range(n + 1):
  p = 1
  for j in range(n + 1):
    if j != i:
      p*=(xp - x[j])/(x[i] - x[j])
  yp += y[i]*p
print("For x = %.3f, y = %.3f" % (xp, yp))

xp = 60
yp = 0 #sum from 0
for i in range(n + 1):
  p = 1
  for j in range(n + 1):
    if j != i:
      p*=(xp - x[j])/(x[i] - x[j])
  yp += y[i]*p
print("For x = %.3f, y = %.3f" % (xp, yp))
