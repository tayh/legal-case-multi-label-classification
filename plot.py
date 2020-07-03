x = [(v) for v in counts.values()]
labels=[(str(k) + " petições iniciais" ) for k in counts]
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.4)


fig1, ax1 = plt.subplots(figsize=(15, 8), subplot_kw=dict(aspect="equal"))
ax1.set_title("Distribuição de petições iniciais duplicadas por processo")

patches, texts = plt.pie(x, startangle=90, radius=1.2)
sort_legend = True
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, x),
                                          key=lambda x: x[2],
                                          reverse=True))


plt.legend(patches, labels, bbox_to_anchor=(-0.1, 1.),
           fontsize=8)
plt.show()
