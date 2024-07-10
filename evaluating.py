import matplotlib.pyplot as plt
import matplotlib

ev = regressor.evaluate(
    input_fn=lambda: input_fn_new(testing_set, training=True), steps=1
)
loss_score = ev["loss"]
print("Final Loss on the testing set: {0:f}".format(loss_score))

reality = pd.DataFrame(
    prepro.inverse_transform(testing_set.select_dtypes(exclude=["object"])),
    columns=[COLUMNS],
).SalePrice
y = regressor.predict(input_fn=lambda: input_fn_new(testing_set))
predictions = list(itertools.islice(y, testing_set.shape[0]))
predictions = pd.DataFrame(
    prepro_y.inverse_transform(np.array(predictions).reshape(263, 1))
)

matplotlib.rc("xtick", labelsize=30)
matplotlib.rc("ytick", labelsize=30)
fig, ax = plt.subplots(figsize=(15, 12))
plt.style.use("ggplot")
plt.plot(predictions.values, reality.values, "ro")
plt.xlabel("Predictions", fontsize=30)
plt.ylabel("Reality", fontsize=30)
plt.title("Predictions x Reality on dataset Test", fontsize=30)
ax.plot([reality.min(), reality.max()], [reality.min(), reality.max()], "k--", lw=4)
plt.show()