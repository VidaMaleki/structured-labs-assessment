from preswald import text, plotly, connect, get_df, table, slider, query
import plotly.express as px

# Add heading
text("# Vida's Iris Data App")
text("Interactive app to explore the Iris dataset.")

# Connect and load data
connect()
df = get_df("iris")

sql = "SELECT * FROM iris WHERE petal_length > 3"
filtered_df = query(sql, "iris")
table(filtered_df, title="Filtered Data (petal_length > 3)")

# Slider to filter by sepal length
threshold = slider("Minimum Sepal Length", min_val=4.0, max_val=8.0, default=5.0)
dynamic_df = df[df["sepal_length"] > threshold]
table(dynamic_df, title="Dynamic Data View (Slider)")

fig = px.scatter(
    dynamic_df,
    x="sepal_length",
    y="sepal_width",
    color="species",
    title="Sepal Length vs Sepal Width by Species"
)
plotly(fig)
