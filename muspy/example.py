import muspy
import matplotlib.pyplot as plt

muspy.download_bravura_font()
music = muspy.load("example.json")
print(music)
muspy.show_pianoroll(music)
muspy.show_score(music)
plt.show()
