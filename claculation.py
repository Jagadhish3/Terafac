# calculation.py - Corrected code to find optimal dimensions
print("Calculating optimal cuboid dimensions...")

# The correct constraint: l × w × h - (l-4) × (w-4) × (h-4) = 20000
# (not 200, that was a scaling error)
solutions = []

for l in range(20, 60):
    for w in range(20, 60):
        for h in range(20, 60):
            outer_vol = l * w * h
            inner_vol = (l-4) * (w-4) * (h-4)
            
            if inner_vol <= 0:
                continue
            
            bricks_used = outer_vol - inner_vol
            
            # Look for solutions close to 20000 (not 200)
            if abs(bricks_used - 20000) <= 100:
                solutions.append((l, w, h, bricks_used, inner_vol))

# Sort by inner volume (maximize this)
solutions.sort(key=lambda x: x[4], reverse=True)

print("Top solutions:")
for i, (l, w, h, bricks, inner_vol) in enumerate(solutions[:10], 1):
    outer_mm = (l*100, w*100, h*100)
    inner_mm = ((l-4)*100, (w-4)*100, (h-4)*100)
    print(f"{i}. l={l}, w={w}, h={h}:")
    print(f"   Brick units used: {bricks}/20000")
    print(f"   Outer dimensions: {outer_mm[0]} × {outer_mm[1]} × {outer_mm[2]} mm")
    print(f"   Inner dimensions: {inner_mm[0]} × {inner_mm[1]} × {inner_mm[2]} mm")
    print(f"   Inner volume: {inner_vol * 1000000 / 1e9:.2f} m³")
    print()

# Best solution
if solutions:
    l, w, h, bricks, inner_vol = solutions[0]
    print("BEST SOLUTION:")
    print(f"l = {l}, w = {w}, h = {h}")
    print(f"Outer: {l*100} × {w*100} × {h*100} mm")
    print(f"Inner: {(l-4)*100} × {(w-4)*100} × {(h-4)*100} mm")
    print(f"Bricks used: {bricks} (target: 20000)")
    print(f"Inner volume: {inner_vol * 1000000 / 1e9:.2f} m³")
else:
    print("No solutions found! Try expanding the search range.")