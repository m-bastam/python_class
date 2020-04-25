from matplotlib import pyplot as plt

# plt.plot([5,6,7,8])
'''
pyplot.plot assumed our single data list to be the y-values;
in the absence of an x-values list, [0, 1, 2, 3] was used instead.
'''
# plt.show()

# plt.plot([0.1, 0.2, 0.3, 0.4], [10, 12, 31, 4])
# plt.show()

# plt.plot([0.1, 0.2, 0.3, 0.4], [1, 2, 3, 4],[0.1, 0.2, 0.3, 0.4], [1, 4, 9, 16])
plt.plot([0.1, 0.2, 0.3, 0.4], [1, 2, 3, 4], 'gx' , label='first plot' )
plt.plot([0.1, 0.2, 0.3, 0.4], [1, 4, 9, 16], 'r-.', label='second plot' )
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Scale (Bananas)")
plt.xlim(0, 1)
plt.ylim(-5, 20)
plt.show()
plt.savefig('the_best_plot.pdf')

plt.bar(range(7), [1, 2, 3, 4, 3, 2, 1])
plt.show()