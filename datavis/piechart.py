import matplotlib.pyplot as plotter

labels = ['Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl']
sizes = [33, 52, 12, 17, 62, 48]
separated = (0.2, 0, 0, 0.1, 0, 0)

plotter.pie(sizes, labels = labels, autopct='%1.1f%%', explode=separated)
plotter.axis('equal')

plotter.show()