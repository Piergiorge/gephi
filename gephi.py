import gephi

# Create a Gephi instance
gephi = gephi.Gephi()

# Load a graph into Gephi
gephi.load_graph("graph.gexf")

# Run the Force Atlas 2 layout algorithm
gephi.run_algorithm("ForceAtlas2")

# Save the graph as a PDF
gephi.save_as_pdf("graph.pdf")

# Close the Gephi instance
gephi.close()
