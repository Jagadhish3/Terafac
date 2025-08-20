import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# Optimal dimensions
outer_dims = (4200, 4300, 4400)
inner_dims = (3800, 3900, 4000)
wall_thickness = 200

# Create simple and clear visualization
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# ==================== SIMPLE TOP VIEW ====================
ax1.add_patch(Rectangle((0, 0), outer_dims[0], outer_dims[1], 
                       fill=False, edgecolor='blue', linewidth=3))
ax1.add_patch(Rectangle((wall_thickness, wall_thickness), inner_dims[0], inner_dims[1],
                       fill=True, edgecolor='red', facecolor='red', alpha=0.2))

# Show brick arrangement clearly
for x in np.arange(0, outer_dims[0], 200):  # Show every 2nd brick for clarity
    for y in np.arange(0, outer_dims[1], 100):
        if (x < wall_thickness or x > outer_dims[0]-wall_thickness or 
            y < wall_thickness or y > outer_dims[1]-wall_thickness):
            # Horizontal bricks (lying flat)
            ax1.add_patch(Rectangle((x, y), 200, 100, fill=True, 
                                  facecolor='red', edgecolor='darkred', alpha=0.7))
            ax1.text(x+100, y+50, '→', ha='center', va='center', fontsize=8, 
                    fontweight='bold', color='white')

ax1.set_xlim(-100, outer_dims[0]+100)
ax1.set_ylim(-100, outer_dims[1]+100)
ax1.set_aspect('equal')
ax1.set_title('TOP VIEW - How Bricks Are Laid\n(Arrows show brick orientation)', fontweight='bold', fontsize=12)
ax1.set_xlabel('Length (mm)')
ax1.set_ylabel('Width (mm)')
ax1.grid(True, alpha=0.3)

# ==================== SIMPLE SIDE VIEW ====================
ax2.add_patch(Rectangle((0, 0), outer_dims[0], outer_dims[2], 
                       fill=False, edgecolor='blue', linewidth=3))
ax2.add_patch(Rectangle((wall_thickness, wall_thickness), inner_dims[0], inner_dims[2],
                       fill=True, edgecolor='red', facecolor='red', alpha=0.2))

# Show vertical brick arrangement
for x in np.arange(0, outer_dims[0], 200):
    for z in np.arange(0, outer_dims[2], 100):
        if (x < wall_thickness or x > outer_dims[0]-wall_thickness or 
            z < wall_thickness or z > outer_dims[2]-wall_thickness):
            # Vertical bricks (standing up)
            ax2.add_patch(Rectangle((x, z), 200, 100, fill=True, 
                                  facecolor='red', edgecolor='darkred', alpha=0.7))
            ax2.text(x+100, z+50, '↑', ha='center', va='center', fontsize=8, 
                    fontweight='bold', color='white')

ax2.set_xlim(-100, outer_dims[0]+100)
ax2.set_ylim(-100, outer_dims[2]+100)
ax2.set_aspect('equal')
ax2.set_title('SIDE VIEW - Vertical Bricks\n(Arrows show height direction)', fontweight='bold', fontsize=12)
ax2.set_xlabel('Length (mm)')
ax2.set_ylabel('Height (mm)')
ax2.grid(True, alpha=0.3)

# ==================== BRICK ORIENTATION GUIDE ====================
ax3.axis('off')

# Title
ax3.text(0.5, 0.95, 'BRICK ORIENTATION GUIDE', ha='center', va='center', 
        fontweight='bold', fontsize=14, color='darkred')

# Explanation
explanations = [
    "BRICK SIZE: 200mm × 100mm × 100mm",
    "",
    "TWO MAIN ORIENTATIONS:",
    "",
    "1. HORIZONTAL BRICKS (Top/Bottom):",
    "   • 200mm side VERTICAL (up/down)",
    "   • 100mm sides horizontal",
    "   • Used for floor and ceiling",
    "",
    "2. VERTICAL BRICKS (Walls):",
    "   • 200mm side HORIZONTAL (facing out)",
    "   • 100mm sides: one vertical, one horizontal",
    "   • Used for side walls",
    "",
    "CORNER BRICKS:",
    "   • Special orientation",
    "   • Maintain 200mm wall thickness",
    "   • Interlock with both directions"
]

for i, text in enumerate(explanations):
    y_pos = 0.85 - i * 0.05
    if "BRICK SIZE" in text:
        ax3.text(0.5, y_pos, text, ha='center', va='center', fontweight='bold', 
                fontsize=11, color='blue')
    elif "TWO MAIN" in text:
        ax3.text(0.5, y_pos, text, ha='center', va='center', fontweight='bold', 
                fontsize=11, color='darkgreen')
    elif "HORIZONTAL" in text or "VERTICAL" in text:
        ax3.text(0.1, y_pos, text, ha='left', va='center', fontweight='bold', 
                fontsize=10, color='black')
    elif "CORNER" in text:
        ax3.text(0.5, y_pos, text, ha='center', va='center', fontweight='bold', 
                fontsize=11, color='purple')
    else:
        ax3.text(0.1, y_pos, text, ha='left', va='center', fontsize=9, color='black')

# Add simple diagrams for orientation
ax3.add_patch(Rectangle((0.2, 0.4), 0.15, 0.1, facecolor='red', alpha=0.7))
ax3.text(0.275, 0.45, '→\n200mm', ha='center', va='center', fontsize=8)
ax3.text(0.2, 0.35, 'Horizontal Brick\n(200mm side down)', ha='center', va='top', fontsize=8)

ax3.add_patch(Rectangle((0.6, 0.4), 0.1, 0.15, facecolor='red', alpha=0.7))
ax3.text(0.65, 0.475, '↑\n200mm', ha='center', va='center', fontsize=8)
ax3.text(0.6, 0.35, 'Vertical Brick\n(200mm side out)', ha='center', va='top', fontsize=8)

plt.tight_layout()
plt.savefig('simple_brick_arrangement_guide.png', dpi=300, bbox_inches='tight')
plt.show()

print("="*60)
print("SIMPLIFIED EXPLANATION:")
print("="*60)
print("1. OUTER SHELL: 4200mm × 4300mm × 4400mm")
print("2. INNER HOLE:   3800mm × 3900mm × 4000mm") 
print("3. WALL THICKNESS: 200mm everywhere")
print("")
print("HOW BRICKS ARE ARRANGED:")
print("- Top & Bottom: Bricks laid FLAT (200mm vertical)")
print("- Side Walls:   Bricks stood UP (200mm horizontal)")
print("- Corners:      Special arrangement for strength")
print("")
print("ARROWS SHOW:")
print("→ 200mm direction for horizontal bricks")  
print("↑ 200mm direction for vertical bricks")
print("="*60)